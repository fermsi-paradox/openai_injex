"""
Configuration loader utility
"""

import os
import yaml
from pathlib import Path
from typing import Dict, Any

def load_config(config_path: str = "config/defense_config.yaml") -> Dict[str, Any]:
    """Load configuration from YAML file"""
    config_file = Path(config_path)
    
    if not config_file.exists():
        # Return default configuration if file doesn't exist
        return get_default_config()
    
    with open(config_file, 'r') as f:
        config = yaml.safe_load(f)
    
    # Merge with environment variables
    config = merge_env_vars(config)
    
    return config

def get_default_config() -> Dict[str, Any]:
    """Return default configuration"""
    return {
        'log_level': 'INFO',
        'log_format': 'json',
        'log_file': 'logs/defense_system.log',
        'openai': {
            'model': 'gpt-4o',
            'temperature': 0.2,
            'max_tokens': 4000,
            'timeout': 30
        },
        'detection': {
            'behavioral': {
                'api_call_threshold': 100,
                'memory_threshold_gb': 2,
                'cpu_threshold_percent': 70
            }
        }
    }

def merge_env_vars(config: Dict[str, Any]) -> Dict[str, Any]:
    """Merge environment variables into configuration"""
    # Override with environment variables if present
    if os.getenv('LOG_LEVEL'):
        config['log_level'] = os.getenv('LOG_LEVEL')
    
    if os.getenv('OPENAI_MODEL'):
        config['openai']['model'] = os.getenv('OPENAI_MODEL')
    
    return config 