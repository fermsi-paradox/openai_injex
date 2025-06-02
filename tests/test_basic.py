#!/usr/bin/env python3
"""
Basic unit tests for AI Defense System
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from unittest.mock import Mock, patch
from src.analyzers.threat_analyzer import ThreatAnalyzer
from src.defenders.firewall_manager import FirewallManager
from src.defenders.injection_engine import InjectionEngine
from src.utils.config_loader import load_config, get_default_config

class TestBasicFunctionality(unittest.TestCase):
    """Test basic functionality of system components"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.config = get_default_config()
        
    def test_config_loader(self):
        """Test configuration loading"""
        config = get_default_config()
        self.assertIsInstance(config, dict)
        self.assertIn('log_level', config)
        self.assertEqual(config['log_level'], 'INFO')
        
    def test_threat_analyzer_init(self):
        """Test ThreatAnalyzer initialization"""
        analyzer = ThreatAnalyzer(self.config)
        self.assertTrue(analyzer.self_test())
        
    def test_threat_analyzer_trace(self):
        """Test threat origin tracing"""
        analyzer = ThreatAnalyzer(self.config)
        threat = {
            'id': 'test_001',
            'type': 'network',
            'description': 'Test threat'
        }
        
        origin = analyzer.trace_origin(threat)
        self.assertIsInstance(origin, dict)
        self.assertIn('type', origin)
        self.assertIn('confidence', origin)
        self.assertIn('analyzed_at', origin)
        
    def test_firewall_manager_init(self):
        """Test FirewallManager initialization"""
        firewall = FirewallManager(self.config)
        self.assertIsNotNone(firewall.platform)
        self.assertTrue(firewall.self_test())
        
    def test_firewall_deploy(self):
        """Test firewall rule deployment"""
        firewall = FirewallManager(self.config)
        
        # Mock detections
        detections = {
            'detections': [
                {
                    'description': 'Test threat',
                    'evidence': {
                        'remote_ip': '1.2.3.4',
                        'remote_port': 443
                    }
                }
            ]
        }
        
        rules_deployed = firewall.deploy(detections, [])
        self.assertGreaterEqual(rules_deployed, 0)
        
    def test_injection_engine_init(self):
        """Test InjectionEngine initialization"""
        # Add injection config
        self.config['injection'] = {
            'strategies': ['confusion', 'shutdown'],
            'payloads': {
                'confusion': ['Test confusion payload'],
                'shutdown': ['Test shutdown payload']
            }
        }
        
        injector = InjectionEngine(self.config)
        self.assertTrue(injector.self_test())
        
    def test_injection_attempt(self):
        """Test injection attempt"""
        self.config['injection'] = {
            'strategies': ['confusion'],
            'payloads': {
                'confusion': ['Test payload']
            }
        }
        
        injector = InjectionEngine(self.config)
        threat = {
            'id': 'test_001',
            'type': 'network',
            'evidence': {
                'service': 'openai',
                'remote_ip': '1.2.3.4',
                'remote_port': 443
            }
        }
        
        result = injector.inject(threat)
        self.assertIsInstance(result, dict)
        self.assertIn('threat_id', result)
        self.assertIn('success', result)
        self.assertIn('attempts', result)

class TestDemoComponents(unittest.TestCase):
    """Test demo-specific components"""
    
    def test_demo_imports(self):
        """Test that demo modules can be imported"""
        try:
            from demo import DemoVisualizer, MockDetector
            self.assertTrue(True)
        except ImportError as e:
            self.fail(f"Failed to import demo components: {e}")
            
    def test_mock_detector(self):
        """Test mock detector functionality"""
        from demo import MockDetector
        
        detector = MockDetector()
        threats = detector.scan()
        
        self.assertIsInstance(threats, list)
        self.assertGreater(len(threats), 0)
        self.assertLessEqual(len(threats), 3)
        
        for threat in threats:
            self.assertIn('id', threat)
            self.assertIn('type', threat)
            self.assertIn('severity', threat)
            self.assertIn('evidence', threat)

if __name__ == '__main__':
    unittest.main() 