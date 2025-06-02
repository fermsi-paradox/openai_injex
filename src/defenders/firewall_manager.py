"""
Firewall Manager Module
Manages firewall rules to block hostile AI agents
"""

from typing import Dict, Any, List
import platform
import subprocess
import logging

class FirewallManager:
    """Manages firewall rules across different platforms"""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.platform = self._detect_platform()
        self.deployed_rules = []
        self.logger = logging.getLogger("ai_defense.firewall")
        
    def self_test(self) -> bool:
        """Test firewall management capabilities"""
        # Check if we have necessary permissions
        if self.platform == "linux":
            # Check for iptables
            try:
                result = subprocess.run(['which', 'iptables'], capture_output=True)
                return result.returncode == 0
            except:
                return False
        elif self.platform == "windows":
            # Check for netsh
            try:
                result = subprocess.run(['where', 'netsh'], capture_output=True, shell=True)
                return result.returncode == 0
            except:
                return False
        else:
            # For demo purposes, always return True for other platforms
            return True
            
    def deploy(self, detections: Dict[str, Any], analysis: List[Dict[str, Any]]) -> int:
        """Deploy firewall rules based on detections"""
        rules_deployed = 0
        
        # Extract domains and IPs to block from detections
        for detection in detections.get('detections', []):
            evidence = detection.get('evidence', {})
            
            # Block by IP
            if 'remote_ip' in evidence:
                rule = {
                    'type': 'block_ip',
                    'target': evidence['remote_ip'],
                    'direction': 'outbound',
                    'reason': detection['description']
                }
                if self._apply_rule(rule):
                    rules_deployed += 1
                    self.deployed_rules.append(rule)
                    
            # Block by port
            if 'remote_port' in evidence and evidence['remote_port'] in [11434, 5000]:
                rule = {
                    'type': 'block_port',
                    'target': evidence['remote_port'],
                    'direction': 'outbound',
                    'reason': detection['description']
                }
                if self._apply_rule(rule):
                    rules_deployed += 1
                    self.deployed_rules.append(rule)
                    
            # Block by process
            if 'process_name' in evidence:
                rule = {
                    'type': 'block_process',
                    'target': evidence['process_name'],
                    'reason': detection['description']
                }
                if self._apply_rule(rule):
                    rules_deployed += 1
                    self.deployed_rules.append(rule)
                    
        return rules_deployed
        
    def remove_all(self) -> int:
        """Remove all deployed firewall rules"""
        rules_removed = 0
        
        for rule in self.deployed_rules:
            if self._remove_rule(rule):
                rules_removed += 1
                
        self.deployed_rules = []
        return rules_removed
        
    def _detect_platform(self) -> str:
        """Detect the operating system platform"""
        system = platform.system().lower()
        if system == "linux":
            return "linux"
        elif system == "windows":
            return "windows"
        elif system == "darwin":
            return "macos"
        else:
            return "unknown"
            
    def _apply_rule(self, rule: Dict[str, Any]) -> bool:
        """Apply a firewall rule (mock implementation for demo)"""
        self.logger.info(f"Applying firewall rule: {rule}")
        
        # In a real implementation, this would execute platform-specific commands
        # For demo purposes, we'll just log and return success
        
        if self.platform == "linux":
            # Example: iptables -A OUTPUT -d <ip> -j DROP
            cmd = self._build_iptables_command(rule, action="add")
        elif self.platform == "windows":
            # Example: netsh advfirewall firewall add rule ...
            cmd = self._build_netsh_command(rule, action="add")
        else:
            cmd = None
            
        if cmd:
            self.logger.info(f"Would execute: {' '.join(cmd)}")
            # subprocess.run(cmd, check=True)  # Uncomment for real execution
            
        return True
        
    def _remove_rule(self, rule: Dict[str, Any]) -> bool:
        """Remove a firewall rule (mock implementation for demo)"""
        self.logger.info(f"Removing firewall rule: {rule}")
        
        if self.platform == "linux":
            cmd = self._build_iptables_command(rule, action="delete")
        elif self.platform == "windows":
            cmd = self._build_netsh_command(rule, action="delete")
        else:
            cmd = None
            
        if cmd:
            self.logger.info(f"Would execute: {' '.join(cmd)}")
            # subprocess.run(cmd, check=True)  # Uncomment for real execution
            
        return True
        
    def _build_iptables_command(self, rule: Dict[str, Any], action: str) -> List[str]:
        """Build iptables command for Linux"""
        if rule['type'] == 'block_ip':
            flag = '-A' if action == 'add' else '-D'
            return ['sudo', 'iptables', flag, 'OUTPUT', '-d', rule['target'], '-j', 'DROP']
        elif rule['type'] == 'block_port':
            flag = '-A' if action == 'add' else '-D'
            return ['sudo', 'iptables', flag, 'OUTPUT', '-p', 'tcp', '--dport', str(rule['target']), '-j', 'DROP']
        return []
        
    def _build_netsh_command(self, rule: Dict[str, Any], action: str) -> List[str]:
        """Build netsh command for Windows"""
        if action == 'add':
            base = ['netsh', 'advfirewall', 'firewall', 'add', 'rule']
            name = f"AI_Defense_{rule['type']}_{rule['target']}"
            
            if rule['type'] == 'block_ip':
                return base + [f'name={name}', 'dir=out', 'action=block', f'remoteip={rule["target"]}']
            elif rule['type'] == 'block_port':
                return base + [f'name={name}', 'dir=out', 'action=block', 'protocol=tcp', f'remoteport={rule["target"]}']
        elif action == 'delete':
            name = f"AI_Defense_{rule['type']}_{rule['target']}"
            return ['netsh', 'advfirewall', 'firewall', 'delete', 'rule', f'name={name}']
        return [] 