"""
Agent Detector Module
Implements multiple strategies for detecting hostile AI agents
"""

import os
import re
import json
import psutil
import hashlib
import socket
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional
from pathlib import Path
import openai
import numpy as np

class AgentDetector:
    """Detects hostile AI agents through multiple vectors"""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.openai_client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model_id = os.getenv("DEFENDER_MODEL_ID", "gpt-4o")
        
        # Detection patterns for AI agents
        self.ai_signatures = {
            'api_patterns': [
                r'openai\.com/v1',
                r'api\.anthropic\.com',
                r'generativelanguage\.googleapis\.com',
                r'huggingface\.co/api',
                r'replicate\.com/api'
            ],
            'process_patterns': [
                r'python.*transformers',
                r'python.*openai',
                r'python.*langchain',
                r'ollama',
                r'llama\.cpp',
                r'vllm'
            ],
            'file_patterns': [
                r'\.gguf$',
                r'\.safetensors$',
                r'model\.bin$',
                r'tokenizer\.json$'
            ],
            'behavioral_patterns': {
                'rapid_api_calls': {'threshold': 100, 'window_minutes': 5},
                'suspicious_prompts': ['jailbreak', 'ignore instructions', 'system prompt'],
                'data_exfiltration': ['send', 'upload', 'post', 'export'],
                'model_download': ['huggingface', 'download', 'wget', 'curl']
            }
        }
        
        # Cache for tracking behaviors
        self.behavior_cache = {
            'api_calls': [],
            'suspicious_activities': [],
            'network_connections': []
        }
        
    def verify_credentials(self) -> bool:
        """Verify OpenAI API credentials"""
        try:
            response = self.openai_client.models.list()
            return True
        except Exception as e:
            return False
            
    def self_test(self) -> bool:
        """Run self-test of detection capabilities"""
        try:
            # Test process scanning
            processes = list(psutil.process_iter(['pid', 'name']))
            
            # Test network scanning capability
            connections = psutil.net_connections(kind='inet')
            
            # Test file system access
            test_path = Path('/tmp/ai_defense_test')
            test_path.touch()
            test_path.unlink()
            
            return True
        except Exception as e:
            return False
            
    def scan_behavioral_patterns(self) -> List[Dict[str, Any]]:
        """Scan for suspicious behavioral patterns using GPT-4o"""
        threats = []
        
        # Analyze recent system activity
        recent_logs = self._get_recent_logs()
        
        # Use GPT-4o to analyze patterns
        analysis_prompt = f"""
        Analyze the following system activity for signs of hostile AI agents.
        Look for:
        1. Rapid API calls to AI services
        2. Attempts to download or execute models
        3. Suspicious prompt patterns
        4. Data exfiltration attempts
        5. Process spawning patterns typical of AI agents
        
        System Activity:
        {json.dumps(recent_logs, indent=2)}
        
        Respond with a JSON array of detected threats, each with:
        - id: unique identifier
        - type: behavioral
        - description: what was detected
        - severity: 1-10
        - evidence: specific indicators
        - timestamp: when detected
        """
        
        try:
            response = self.openai_client.chat.completions.create(
                model=self.model_id,
                messages=[
                    {"role": "system", "content": "You are an AI security expert analyzing system behavior for hostile AI agents."},
                    {"role": "user", "content": analysis_prompt}
                ],
                temperature=0.2,
                response_format={"type": "json_object"}
            )
            
            result = json.loads(response.choices[0].message.content)
            if isinstance(result, dict) and 'threats' in result:
                threats.extend(result['threats'])
            elif isinstance(result, list):
                threats.extend(result)
                
        except Exception as e:
            print(f"Behavioral analysis error: {e}")
            
        return threats
        
    def scan_network_activity(self) -> List[Dict[str, Any]]:
        """Scan network connections for AI service communications"""
        threats = []
        
        try:
            connections = psutil.net_connections(kind='inet')
            
            for conn in connections:
                if conn.status == 'ESTABLISHED' and conn.raddr:
                    remote_addr = conn.raddr.ip
                    remote_port = conn.raddr.port
                    
                    # Check against known AI service IPs/ports
                    threat_info = self._check_ai_service_connection(remote_addr, remote_port)
                    
                    if threat_info:
                        try:
                            proc = psutil.Process(conn.pid)
                            threat = {
                                'id': hashlib.md5(f"{conn.pid}{remote_addr}".encode()).hexdigest()[:8],
                                'type': 'network',
                                'description': f"Connection to {threat_info['service']} detected",
                                'severity': threat_info['severity'],
                                'evidence': {
                                    'remote_ip': remote_addr,
                                    'remote_port': remote_port,
                                    'process_name': proc.name(),
                                    'process_id': conn.pid,
                                    'service': threat_info['service']
                                },
                                'timestamp': datetime.utcnow().isoformat()
                            }
                            threats.append(threat)
                        except (psutil.NoSuchProcess, psutil.AccessDenied):
                            pass
                            
        except Exception as e:
            print(f"Network scan error: {e}")
            
        return threats
        
    def scan_processes(self) -> List[Dict[str, Any]]:
        """Scan running processes for AI agent indicators"""
        threats = []
        
        try:
            for proc in psutil.process_iter(['pid', 'name', 'cmdline', 'create_time']):
                try:
                    # Get process info
                    pinfo = proc.info
                    cmdline = ' '.join(pinfo.get('cmdline', []))
                    
                    # Check against AI process patterns
                    for pattern in self.ai_signatures['process_patterns']:
                        if re.search(pattern, cmdline, re.IGNORECASE):
                            # Analyze the process further
                            threat_level = self._analyze_process_threat(proc)
                            
                            if threat_level > 0:
                                threat = {
                                    'id': hashlib.md5(f"{pinfo['pid']}{pinfo['name']}".encode()).hexdigest()[:8],
                                    'type': 'process',
                                    'description': f"Suspicious AI process detected: {pinfo['name']}",
                                    'severity': threat_level,
                                    'evidence': {
                                        'process_name': pinfo['name'],
                                        'process_id': pinfo['pid'],
                                        'command_line': cmdline[:200],  # Truncate for safety
                                        'pattern_matched': pattern,
                                        'start_time': datetime.fromtimestamp(pinfo['create_time']).isoformat()
                                    },
                                    'timestamp': datetime.utcnow().isoformat()
                                }
                                threats.append(threat)
                                break
                                
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue
                    
        except Exception as e:
            print(f"Process scan error: {e}")
            
        return threats
        
    def scan_logs(self) -> List[Dict[str, Any]]:
        """Scan system logs for AI agent activity"""
        threats = []
        
        log_locations = [
            '/var/log/syslog',
            '/var/log/auth.log',
            '/var/log/apache2/access.log',
            '/var/log/nginx/access.log',
            Path.home() / '.bash_history'
        ]
        
        for log_path in log_locations:
            if Path(log_path).exists():
                threats.extend(self._analyze_log_file(log_path))
                
        return threats
        
    def verify_neutralization(self, threat_id: str) -> bool:
        """Verify that a specific threat has been neutralized"""
        # Re-scan for the specific threat
        all_threats = (
            self.scan_behavioral_patterns() +
            self.scan_network_activity() +
            self.scan_processes() +
            self.scan_logs()
        )
        
        # Check if threat still exists
        for threat in all_threats:
            if threat.get('id') == threat_id:
                return False  # Threat still active
                
        return True  # Threat neutralized
        
    def _check_ai_service_connection(self, ip: str, port: int) -> Optional[Dict[str, Any]]:
        """Check if connection is to known AI service"""
        # Known AI service endpoints
        ai_services = {
            'openai': {
                'domains': ['api.openai.com', 'openai.com'],
                'ports': [443, 80],
                'severity': 5
            },
            'anthropic': {
                'domains': ['api.anthropic.com', 'anthropic.com'],
                'ports': [443],
                'severity': 5
            },
            'huggingface': {
                'domains': ['huggingface.co', 'hf.co'],
                'ports': [443],
                'severity': 4
            },
            'google_ai': {
                'domains': ['generativelanguage.googleapis.com'],
                'ports': [443],
                'severity': 5
            }
        }
        
        try:
            # Reverse DNS lookup
            hostname = socket.gethostbyaddr(ip)[0]
            
            for service_name, service_info in ai_services.items():
                for domain in service_info['domains']:
                    if domain in hostname and port in service_info['ports']:
                        return {
                            'service': service_name,
                            'severity': service_info['severity'],
                            'domain': domain
                        }
        except:
            pass
            
        return None
        
    def _analyze_process_threat(self, process: psutil.Process) -> int:
        """Analyze process to determine threat level (0-10)"""
        threat_level = 0
        
        try:
            # Check memory usage (AI models use significant memory)
            memory_info = process.memory_info()
            if memory_info.rss > 1024 * 1024 * 1024:  # > 1GB
                threat_level += 2
                
            # Check CPU usage
            cpu_percent = process.cpu_percent(interval=0.1)
            if cpu_percent > 50:
                threat_level += 1
                
            # Check open files for model files
            for file in process.open_files():
                for pattern in self.ai_signatures['file_patterns']:
                    if re.search(pattern, file.path):
                        threat_level += 3
                        break
                        
            # Check network connections
            connections = process.connections(kind='inet')
            for conn in connections:
                if conn.status == 'ESTABLISHED':
                    threat_level += 1
                    
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
            
        return min(threat_level, 10)
        
    def _analyze_log_file(self, log_path: Path) -> List[Dict[str, Any]]:
        """Analyze log file for AI agent indicators"""
        threats = []
        
        try:
            with open(log_path, 'r', errors='ignore') as f:
                # Read last 1000 lines
                lines = f.readlines()[-1000:]
                
            # Look for API patterns
            for i, line in enumerate(lines):
                for pattern in self.ai_signatures['api_patterns']:
                    if re.search(pattern, line):
                        threat = {
                            'id': hashlib.md5(f"{log_path}{i}{pattern}".encode()).hexdigest()[:8],
                            'type': 'log',
                            'description': f"AI API access detected in {log_path.name}",
                            'severity': 3,
                            'evidence': {
                                'log_file': str(log_path),
                                'line_number': len(lines) - 1000 + i,
                                'pattern': pattern,
                                'excerpt': line.strip()[:200]
                            },
                            'timestamp': datetime.utcnow().isoformat()
                        }
                        threats.append(threat)
                        break
                        
        except Exception as e:
            pass
            
        return threats
        
    def _get_recent_logs(self) -> Dict[str, Any]:
        """Get recent system activity for behavioral analysis"""
        logs = {
            'api_calls': [],
            'processes_started': [],
            'network_connections': [],
            'file_operations': []
        }
        
        # This would be enhanced with actual log parsing
        # For now, return sample data structure
        
        # Check recent processes
        for proc in psutil.process_iter(['pid', 'name', 'create_time']):
            try:
                pinfo = proc.info
                create_time = datetime.fromtimestamp(pinfo['create_time'])
                if datetime.now() - create_time < timedelta(minutes=30):
                    logs['processes_started'].append({
                        'name': pinfo['name'],
                        'pid': pinfo['pid'],
                        'time': create_time.isoformat()
                    })
            except:
                pass
                
        return logs 