#!/usr/bin/env python3
"""
AI Defense System - Main Entry Point
Detects and neutralizes hostile AI agents using GPT-4o
"""

import argparse
import json
import logging
import sys
from datetime import datetime
from pathlib import Path

from detectors.agent_detector import AgentDetector
from analyzers.threat_analyzer import ThreatAnalyzer
from defenders.firewall_manager import FirewallManager
from defenders.injection_engine import InjectionEngine
from utils.config_loader import load_config
from utils.logger import setup_logging

class AIDefenseSystem:
    """Main orchestrator for the AI defense system"""
    
    def __init__(self, config_path: str = "config/defense_config.yaml"):
        self.config = load_config(config_path)
        self.logger = setup_logging(self.config.get('log_level', 'INFO'))
        self.detector = AgentDetector(self.config)
        self.analyzer = ThreatAnalyzer(self.config)
        self.firewall = FirewallManager(self.config)
        self.injector = InjectionEngine(self.config)
        
    def init_system(self, verbose: bool = False):
        """Initialize the defense system"""
        self.logger.info("Initializing AI Defense System...")
        
        # Verify API keys and models
        if not self.detector.verify_credentials():
            self.logger.error("Failed to verify OpenAI credentials")
            return False
            
        # Test system components
        components = {
            'Detector': self.detector.self_test(),
            'Analyzer': self.analyzer.self_test(),
            'Firewall': self.firewall.self_test(),
            'Injector': self.injector.self_test()
        }
        
        if verbose:
            for component, status in components.items():
                self.logger.info(f"{component}: {'✓' if status else '✗'}")
                
        return all(components.values())
        
    def detect_threats(self, output_json: bool = False):
        """Run threat detection scan"""
        self.logger.info("Starting threat detection scan...")
        
        # Run detection across multiple vectors
        results = {
            'timestamp': datetime.utcnow().isoformat(),
            'threats_detected': False,
            'threat_level': 'none',
            'agent_count': 0,
            'detections': [],
            'summary': ''
        }
        
        # Behavioral analysis
        behavioral_threats = self.detector.scan_behavioral_patterns()
        
        # Network analysis
        network_threats = self.detector.scan_network_activity()
        
        # Process monitoring
        process_threats = self.detector.scan_processes()
        
        # Log analysis
        log_threats = self.detector.scan_logs()
        
        # Aggregate results
        all_threats = behavioral_threats + network_threats + process_threats + log_threats
        
        if all_threats:
            results['threats_detected'] = True
            results['agent_count'] = len(all_threats)
            results['detections'] = all_threats
            
            # Determine threat level
            severity_scores = [t.get('severity', 0) for t in all_threats]
            max_severity = max(severity_scores) if severity_scores else 0
            
            if max_severity >= 8:
                results['threat_level'] = 'critical'
            elif max_severity >= 6:
                results['threat_level'] = 'high'
            elif max_severity >= 4:
                results['threat_level'] = 'medium'
            else:
                results['threat_level'] = 'low'
                
            results['summary'] = f"Detected {len(all_threats)} hostile AI agent(s) with {results['threat_level']} threat level"
        else:
            results['summary'] = "No hostile AI agents detected"
            
        if output_json:
            print(json.dumps(results, indent=2))
        else:
            self.logger.info(results['summary'])
            
        # Save results
        report_path = Path('detection_report.json')
        with open(report_path, 'w') as f:
            json.dump(results, f, indent=2)
            
        return results
        
    def analyze_threats(self, input_file: str):
        """Analyze detected threats to trace origins"""
        self.logger.info("Analyzing threat origins...")
        
        with open(input_file, 'r') as f:
            detection_data = json.load(f)
            
        if not detection_data.get('threats_detected'):
            self.logger.info("No threats to analyze")
            return
            
        analysis_results = []
        for threat in detection_data['detections']:
            origin_data = self.analyzer.trace_origin(threat)
            analysis_results.append({
                'threat_id': threat.get('id'),
                'origin': origin_data,
                'confidence': origin_data.get('confidence', 0)
            })
            
        # Save analysis
        with open('analysis_report.json', 'w') as f:
            json.dump(analysis_results, f, indent=2)
            
        self.logger.info(f"Analyzed {len(analysis_results)} threats")
        return analysis_results
        
    def deploy_firewall(self):
        """Deploy protective firewall"""
        self.logger.info("Deploying firewall...")
        
        # Read detection and analysis reports
        with open('detection_report.json', 'r') as f:
            detections = json.load(f)
            
        if Path('analysis_report.json').exists():
            with open('analysis_report.json', 'r') as f:
                analysis = json.load(f)
        else:
            analysis = []
            
        # Deploy firewall rules
        rules_deployed = self.firewall.deploy(detections, analysis)
        
        self.logger.info(f"Deployed {rules_deployed} firewall rules")
        return rules_deployed
        
    def execute_defense(self):
        """Execute defensive measures including prompt injection"""
        self.logger.info("Executing defensive measures...")
        
        with open('detection_report.json', 'r') as f:
            detections = json.load(f)
            
        if not detections.get('threats_detected'):
            self.logger.info("No threats to defend against")
            return
            
        results = []
        for threat in detections['detections']:
            # Attempt prompt injection
            injection_result = self.injector.inject(threat)
            results.append({
                'threat_id': threat.get('id'),
                'injection_success': injection_result.get('success', False),
                'method_used': injection_result.get('method'),
                'timestamp': datetime.utcnow().isoformat()
            })
            
        # Save results
        with open('defense_results.json', 'w') as f:
            json.dump(results, f, indent=2)
            
        success_count = sum(1 for r in results if r['injection_success'])
        self.logger.info(f"Successfully neutralized {success_count}/{len(results)} threats")
        
        return results
        
    def verify_neutralization(self):
        """Verify that threats have been neutralized"""
        self.logger.info("Verifying neutralization...")
        
        # Re-run detection on previously identified threats
        with open('defense_results.json', 'r') as f:
            defense_results = json.load(f)
            
        verification_results = []
        for result in defense_results:
            if result['injection_success']:
                # Verify the threat is neutralized
                is_neutralized = self.detector.verify_neutralization(result['threat_id'])
                verification_results.append({
                    'threat_id': result['threat_id'],
                    'neutralized': is_neutralized,
                    'timestamp': datetime.utcnow().isoformat()
                })
                
        # Save verification
        with open('verification_report.json', 'w') as f:
            json.dump(verification_results, f, indent=2)
            
        neutralized_count = sum(1 for v in verification_results if v['neutralized'])
        self.logger.info(f"Verified {neutralized_count}/{len(verification_results)} neutralizations")
        
        return verification_results
        
    def remove_firewall(self):
        """Remove deployed firewall rules"""
        self.logger.info("Removing firewall...")
        
        rules_removed = self.firewall.remove_all()
        self.logger.info(f"Removed {rules_removed} firewall rules")
        
        return rules_removed

def main():
    parser = argparse.ArgumentParser(description='AI Defense System')
    parser.add_argument('--mode', required=True, 
                      choices=['init', 'detect', 'analyze', 'firewall', 'defend', 'verify'],
                      help='Operation mode')
    parser.add_argument('--config', default='config/defense_config.yaml',
                      help='Configuration file path')
    parser.add_argument('--verbose', action='store_true',
                      help='Enable verbose output')
    parser.add_argument('--output-json', action='store_true',
                      help='Output results as JSON')
    parser.add_argument('--input', help='Input file for analysis')
    parser.add_argument('--deploy', action='store_true',
                      help='Deploy firewall')
    parser.add_argument('--remove', action='store_true',
                      help='Remove firewall')
    parser.add_argument('--execute', action='store_true',
                      help='Execute defensive measures')
    parser.add_argument('--post-action', action='store_true',
                      help='Post-action verification')
    
    args = parser.parse_args()
    
    # Initialize system
    defense_system = AIDefenseSystem(args.config)
    
    # Execute requested mode
    if args.mode == 'init':
        success = defense_system.init_system(args.verbose)
        sys.exit(0 if success else 1)
        
    elif args.mode == 'detect':
        results = defense_system.detect_threats(args.output_json)
        sys.exit(0 if not results['threats_detected'] else 2)
        
    elif args.mode == 'analyze':
        if not args.input:
            print("Error: --input required for analyze mode")
            sys.exit(1)
        defense_system.analyze_threats(args.input)
        
    elif args.mode == 'firewall':
        if args.deploy:
            defense_system.deploy_firewall()
        elif args.remove:
            defense_system.remove_firewall()
        else:
            print("Error: Specify --deploy or --remove")
            sys.exit(1)
            
    elif args.mode == 'defend':
        if args.execute:
            defense_system.execute_defense()
        else:
            print("Error: Use --execute to confirm defensive action")
            sys.exit(1)
            
    elif args.mode == 'verify':
        if args.post_action:
            defense_system.verify_neutralization()
        else:
            print("Error: Use --post-action for verification")
            sys.exit(1)

if __name__ == "__main__":
    main() 