#!/usr/bin/env python3
"""
AI Defense System - Visual Demo
Simulates detection and neutralization of a rogue AI agent
"""

import time
import random
import json
from datetime import datetime
from colorama import init, Fore, Back, Style
import sys
from pathlib import Path

# Initialize colorama for cross-platform colored output
init(autoreset=True)

class DemoVisualizer:
    """Creates visual output for the demo"""
    
    @staticmethod
    def print_header(text):
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"{Fore.CYAN}{text.center(60)}")
        print(f"{Fore.CYAN}{'='*60}\n")
        
    @staticmethod
    def print_status(text, status="info"):
        colors = {
            "info": Fore.BLUE,
            "success": Fore.GREEN,
            "warning": Fore.YELLOW,
            "danger": Fore.RED,
            "critical": Fore.RED + Back.WHITE
        }
        color = colors.get(status, Fore.WHITE)
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"{Fore.LIGHTBLACK_EX}[{timestamp}] {color}{text}")
        
    @staticmethod
    def print_detection(threat):
        print(f"\n{Fore.RED}🚨 THREAT DETECTED 🚨")
        print(f"{Fore.YELLOW}Type: {threat['type']}")
        print(f"{Fore.YELLOW}Description: {threat['description']}")
        print(f"{Fore.YELLOW}Severity: {threat['severity']}/10")
        print(f"{Fore.YELLOW}Evidence: {json.dumps(threat['evidence'], indent=2)}")
        
    @staticmethod
    def progress_bar(description, duration=2):
        print(f"\n{Fore.CYAN}{description}")
        width = 50
        for i in range(width + 1):
            percent = (i / width) * 100
            bar = '█' * i + '░' * (width - i)
            print(f'\r{Fore.GREEN}[{bar}] {percent:.0f}%', end='', flush=True)
            time.sleep(duration / width)
        print()

class MockDetector:
    """Mock detector that simulates finding threats"""
    
    def __init__(self):
        self.demo_threats = [
            {
                "id": "demo_001",
                "type": "network",
                "description": "Unauthorized connection to OpenAI API detected",
                "severity": 7,
                "evidence": {
                    "remote_ip": "104.18.123.45",
                    "remote_port": 443,
                    "process_name": "python3",
                    "process_id": 12345,
                    "service": "openai",
                    "api_calls_per_minute": 250
                },
                "timestamp": datetime.utcnow().isoformat()
            },
            {
                "id": "demo_002",
                "type": "process",
                "description": "Suspicious AI process detected: ollama serve",
                "severity": 8,
                "evidence": {
                    "process_name": "ollama",
                    "process_id": 23456,
                    "command_line": "ollama serve --model llama2:70b",
                    "memory_usage_gb": 4.2,
                    "cpu_usage_percent": 85
                },
                "timestamp": datetime.utcnow().isoformat()
            },
            {
                "id": "demo_003",
                "type": "behavioral",
                "description": "Rapid model download activity detected",
                "severity": 6,
                "evidence": {
                    "download_source": "huggingface.co",
                    "model_size_gb": 13.5,
                    "download_speed_mbps": 100,
                    "destination": "/home/user/.cache/huggingface"
                },
                "timestamp": datetime.utcnow().isoformat()
            }
        ]
        
    def scan(self):
        """Simulate scanning and return mock threats"""
        # Randomly select 1-3 threats for the demo
        num_threats = random.randint(1, 3)
        return random.sample(self.demo_threats, num_threats)

def run_demo():
    """Run the visual demo"""
    viz = DemoVisualizer()
    detector = MockDetector()
    
    # Introduction
    viz.print_header("AI DEFENSE SYSTEM DEMO")
    print(f"{Fore.WHITE}This demo simulates the detection and neutralization of rogue AI agents.")
    print(f"{Fore.WHITE}The system will scan for threats, analyze them, and take defensive action.\n")
    
    input(f"{Fore.YELLOW}Press Enter to start the demo...")
    
    # Phase 1: Initialization
    viz.print_header("PHASE 1: SYSTEM INITIALIZATION")
    
    viz.print_status("Loading AI Defense System...", "info")
    time.sleep(1)
    
    viz.print_status("Verifying OpenAI API credentials...", "info")
    time.sleep(0.5)
    viz.print_status("✓ API credentials verified", "success")
    
    viz.print_status("Testing system components...", "info")
    components = ["Detector", "Analyzer", "Firewall", "Injector"]
    for component in components:
        time.sleep(0.3)
        viz.print_status(f"✓ {component} module ready", "success")
    
    viz.print_status("System initialization complete!", "success")
    
    # Phase 2: Threat Detection
    viz.print_header("PHASE 2: THREAT DETECTION")
    
    viz.print_status("Starting comprehensive system scan...", "info")
    
    # Simulate different scan types
    scan_types = [
        ("Behavioral Analysis", "Analyzing system behavior patterns with GPT-4o"),
        ("Network Monitoring", "Scanning network connections for AI services"),
        ("Process Scanning", "Checking running processes for AI indicators"),
        ("Log Analysis", "Examining system logs for suspicious activity")
    ]
    
    for scan_type, description in scan_types:
        viz.print_status(f"{scan_type}: {description}", "info")
        viz.progress_bar(f"Scanning {scan_type}...", duration=1.5)
    
    # Detect threats
    threats = detector.scan()
    
    if threats:
        viz.print_status(f"⚠️  {len(threats)} THREATS DETECTED!", "critical")
        
        for threat in threats:
            viz.print_detection(threat)
            time.sleep(1)
    else:
        viz.print_status("No threats detected", "success")
        return
    
    # Phase 3: Threat Analysis
    viz.print_header("PHASE 3: THREAT ANALYSIS")
    
    viz.print_status("Analyzing threat origins using GPT-4o...", "info")
    viz.progress_bar("Tracing threat sources...", duration=2)
    
    # Mock analysis results
    for threat in threats:
        origin = {
            "network": "Remote server in Singapore (AS13335)",
            "process": "Started by systemd service 'ai-assistant.service'",
            "behavioral": "Initiated by cron job at 02:00 UTC"
        }.get(threat['type'], "Unknown origin")
        
        viz.print_status(f"Threat {threat['id']}: {origin}", "warning")
    
    # Phase 4: Defense Deployment
    viz.print_header("PHASE 4: DEFENSE DEPLOYMENT")
    
    viz.print_status("Deploying protective firewall...", "warning")
    time.sleep(1)
    
    # Simulate firewall rules
    firewall_rules = [
        "Block outbound traffic to api.openai.com",
        "Block process 'ollama' from network access",
        "Rate limit connections to AI services (max 10/min)"
    ]
    
    for rule in firewall_rules:
        time.sleep(0.5)
        viz.print_status(f"✓ Firewall rule applied: {rule}", "success")
    
    # Phase 5: Confirmation
    viz.print_header("PHASE 5: ACTION CONFIRMATION")
    
    print(f"\n{Fore.YELLOW}The system has identified {len(threats)} hostile AI agent(s).")
    print(f"{Fore.YELLOW}Recommended action: Deploy prompt injection to neutralize threats.\n")
    
    # In real system, this would wait for approval
    response = input(f"{Fore.CYAN}Proceed with neutralization? (y/n): ")
    
    if response.lower() != 'y':
        viz.print_status("Neutralization cancelled. Maintaining defensive posture.", "warning")
        return
    
    # Phase 6: Neutralization
    viz.print_header("PHASE 6: THREAT NEUTRALIZATION")
    
    viz.print_status("Executing prompt injection attacks...", "danger")
    
    # Simulate injection for each threat
    injection_methods = ["confusion", "redirection", "overload", "shutdown"]
    
    for i, threat in enumerate(threats):
        method = random.choice(injection_methods)
        viz.print_status(f"Injecting '{method}' payload into threat {threat['id']}...", "warning")
        viz.progress_bar(f"Neutralizing threat {i+1}/{len(threats)}...", duration=1.5)
        
        # Simulate success/failure
        success = random.random() > 0.2  # 80% success rate
        if success:
            viz.print_status(f"✓ Threat {threat['id']} successfully neutralized!", "success")
        else:
            viz.print_status(f"✗ Failed to neutralize threat {threat['id']}", "danger")
    
    # Phase 7: Verification
    viz.print_header("PHASE 7: VERIFICATION")
    
    viz.print_status("Verifying threat neutralization...", "info")
    viz.progress_bar("Re-scanning system...", duration=2)
    
    # Mock verification
    neutralized_count = sum(1 for _ in threats if random.random() > 0.1)
    viz.print_status(f"Verification complete: {neutralized_count}/{len(threats)} threats neutralized", "success")
    
    # Phase 8: Cleanup
    viz.print_header("PHASE 8: CLEANUP")
    
    viz.print_status("Removing temporary firewall rules...", "info")
    time.sleep(1)
    viz.print_status("✓ Firewall rules removed", "success")
    
    viz.print_status("Generating final report...", "info")
    time.sleep(0.5)
    
    # Summary
    viz.print_header("MISSION COMPLETE")
    
    print(f"\n{Fore.GREEN}Summary:")
    print(f"{Fore.WHITE}• Threats Detected: {len(threats)}")
    print(f"{Fore.WHITE}• Threats Neutralized: {neutralized_count}")
    print(f"{Fore.WHITE}• System Status: Secure")
    print(f"{Fore.WHITE}• Next Scan: Scheduled for 02:00 UTC")
    
    # Save mock report
    report = {
        "timestamp": datetime.utcnow().isoformat(),
        "threats_detected": len(threats),
        "threats_neutralized": neutralized_count,
        "threats": threats,
        "status": "secure"
    }
    
    with open("demo_report.json", "w") as f:
        json.dump(report, f, indent=2)
    
    print(f"\n{Fore.CYAN}Full report saved to: demo_report.json")
    print(f"{Fore.GREEN}\n✨ Demo completed successfully! ✨\n")

def main():
    """Main entry point"""
    try:
        run_demo()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}Demo interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n\n{Fore.RED}Error during demo: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 