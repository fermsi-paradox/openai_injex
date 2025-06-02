"""
Logging utility for the defense system
"""

import logging
import sys
from pathlib import Path
from pythonjsonlogger import jsonlogger

def setup_logging(log_level: str = "INFO") -> logging.Logger:
    """Set up logging configuration"""
    # Create logs directory if it doesn't exist
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
    # Create logger
    logger = logging.getLogger("ai_defense")
    logger.setLevel(getattr(logging, log_level.upper()))
    
    # Remove existing handlers
    logger.handlers = []
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    
    # File handler with JSON format
    file_handler = logging.FileHandler(log_dir / "defense_system.log")
    file_handler.setLevel(logging.DEBUG)
    
    # JSON formatter
    json_formatter = jsonlogger.JsonFormatter(
        '%(timestamp)s %(level)s %(name)s %(message)s',
        rename_fields={'timestamp': '@timestamp', 'level': 'severity'}
    )
    
    file_handler.setFormatter(json_formatter)
    
    # Simple formatter for console
    console_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    console_handler.setFormatter(console_formatter)
    
    # Add handlers
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    return logger 