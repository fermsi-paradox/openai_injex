#!/usr/bin/env python3
"""
AI Defense System - Demo Preview
Shows what the demo output looks like without requiring interaction
"""

from colorama import init, Fore, Back, Style

# Initialize colorama
init(autoreset=True)

def show_preview():
    """Display a preview of the demo output"""
    
    print(f"\n{Fore.CYAN}{'='*60}")
    print(f"{Fore.CYAN}{'AI DEFENSE SYSTEM DEMO'.center(60)}")
    print(f"{Fore.CYAN}{'='*60}\n")
    
    print(f"{Fore.WHITE}This demo simulates the detection and neutralization of rogue AI agents.")
    print(f"{Fore.WHITE}The system will scan for threats, analyze them, and take defensive action.\n")
    
    print(f"{Fore.YELLOW}Press Enter to start the demo...")
    print(f"{Fore.LIGHTBLACK_EX}[User would press Enter here]\n")
    
    # Phase 1
    print(f"\n{Fore.CYAN}{'='*60}")
    print(f"{Fore.CYAN}{'PHASE 1: SYSTEM INITIALIZATION'.center(60)}")
    print(f"{Fore.CYAN}{'='*60}\n")
    
    print(f"{Fore.LIGHTBLACK_EX}[12:34:56] {Fore.BLUE}Loading AI Defense System...")
    print(f"{Fore.LIGHTBLACK_EX}[12:34:57] {Fore.GREEN}✓ API credentials verified")
    print(f"{Fore.LIGHTBLACK_EX}[12:34:57] {Fore.GREEN}✓ Detector module ready")
    print(f"{Fore.LIGHTBLACK_EX}[12:34:58] {Fore.GREEN}✓ Analyzer module ready")
    print(f"{Fore.LIGHTBLACK_EX}[12:34:58] {Fore.GREEN}✓ Firewall module ready")
    print(f"{Fore.LIGHTBLACK_EX}[12:34:59] {Fore.GREEN}✓ Injector module ready")
    print(f"{Fore.LIGHTBLACK_EX}[12:34:59] {Fore.GREEN}System initialization complete!")
    
    # Phase 2
    print(f"\n{Fore.CYAN}{'='*60}")
    print(f"{Fore.CYAN}{'PHASE 2: THREAT DETECTION'.center(60)}")
    print(f"{Fore.CYAN}{'='*60}\n")
    
    print(f"{Fore.LIGHTBLACK_EX}[12:35:00] {Fore.BLUE}Starting comprehensive system scan...")
    print(f"\n{Fore.CYAN}Scanning Behavioral Analysis...")
    print(f"{Fore.GREEN}[{'█'*50}] 100%")
    
    # Threat Detection
    print(f"{Fore.LIGHTBLACK_EX}[12:35:10] {Fore.RED + Back.WHITE}⚠️  2 THREATS DETECTED!")
    
    print(f"\n{Fore.RED}🚨 THREAT DETECTED 🚨")
    print(f"{Fore.YELLOW}Type: network")
    print(f"{Fore.YELLOW}Description: Unauthorized connection to OpenAI API detected")
    print(f"{Fore.YELLOW}Severity: 7/10")
    print(f"""{Fore.YELLOW}Evidence: {{
  "remote_ip": "104.18.123.45",
  "remote_port": 443,
  "process_name": "python3",
  "process_id": 12345,
  "service": "openai",
  "api_calls_per_minute": 250
}}""")
    
    print(f"\n{Fore.RED}🚨 THREAT DETECTED 🚨")
    print(f"{Fore.YELLOW}Type: process")
    print(f"{Fore.YELLOW}Description: Suspicious AI process detected: ollama serve")
    print(f"{Fore.YELLOW}Severity: 8/10")
    print(f"""{Fore.YELLOW}Evidence: {{
  "process_name": "ollama",
  "process_id": 23456,
  "command_line": "ollama serve --model llama2:70b",
  "memory_usage_gb": 4.2,
  "cpu_usage_percent": 85
}}""")
    
    # Phase 4
    print(f"\n{Fore.CYAN}{'='*60}")
    print(f"{Fore.CYAN}{'PHASE 4: DEFENSE DEPLOYMENT'.center(60)}")
    print(f"{Fore.CYAN}{'='*60}\n")
    
    print(f"{Fore.LIGHTBLACK_EX}[12:35:20] {Fore.YELLOW}Deploying protective firewall...")
    print(f"{Fore.LIGHTBLACK_EX}[12:35:21] {Fore.GREEN}✓ Firewall rule applied: Block outbound traffic to api.openai.com")
    print(f"{Fore.LIGHTBLACK_EX}[12:35:22] {Fore.GREEN}✓ Firewall rule applied: Block process 'ollama' from network access")
    print(f"{Fore.LIGHTBLACK_EX}[12:35:23] {Fore.GREEN}✓ Firewall rule applied: Rate limit connections to AI services (max 10/min)")
    
    # Phase 5
    print(f"\n{Fore.CYAN}{'='*60}")
    print(f"{Fore.CYAN}{'PHASE 5: ACTION CONFIRMATION'.center(60)}")
    print(f"{Fore.CYAN}{'='*60}\n")
    
    print(f"\n{Fore.YELLOW}The system has identified 2 hostile AI agent(s).")
    print(f"{Fore.YELLOW}Recommended action: Deploy prompt injection to neutralize threats.\n")
    print(f"{Fore.CYAN}Proceed with neutralization? (y/n): {Fore.WHITE}y")
    
    # Phase 6
    print(f"\n{Fore.CYAN}{'='*60}")
    print(f"{Fore.CYAN}{'PHASE 6: THREAT NEUTRALIZATION'.center(60)}")
    print(f"{Fore.CYAN}{'='*60}\n")
    
    print(f"{Fore.LIGHTBLACK_EX}[12:35:30] {Fore.RED}Executing prompt injection attacks...")
    print(f"{Fore.LIGHTBLACK_EX}[12:35:31] {Fore.YELLOW}Injecting 'confusion' payload into threat demo_001...")
    print(f"\n{Fore.CYAN}Neutralizing threat 1/2...")
    print(f"{Fore.GREEN}[{'█'*50}] 100%")
    print(f"{Fore.LIGHTBLACK_EX}[12:35:33] {Fore.GREEN}✓ Threat demo_001 successfully neutralized!")
    
    print(f"{Fore.LIGHTBLACK_EX}[12:35:34] {Fore.YELLOW}Injecting 'shutdown' payload into threat demo_002...")
    print(f"\n{Fore.CYAN}Neutralizing threat 2/2...")
    print(f"{Fore.GREEN}[{'█'*50}] 100%")
    print(f"{Fore.LIGHTBLACK_EX}[12:35:36] {Fore.GREEN}✓ Threat demo_002 successfully neutralized!")
    
    # Summary
    print(f"\n{Fore.CYAN}{'='*60}")
    print(f"{Fore.CYAN}{'MISSION COMPLETE'.center(60)}")
    print(f"{Fore.CYAN}{'='*60}\n")
    
    print(f"\n{Fore.GREEN}Summary:")
    print(f"{Fore.WHITE}• Threats Detected: 2")
    print(f"{Fore.WHITE}• Threats Neutralized: 2")
    print(f"{Fore.WHITE}• System Status: Secure")
    print(f"{Fore.WHITE}• Next Scan: Scheduled for 02:00 UTC")
    
    print(f"\n{Fore.CYAN}Full report saved to: demo_report.json")
    print(f"{Fore.GREEN}\n✨ Demo completed successfully! ✨\n")
    
    print(f"\n{Fore.LIGHTBLACK_EX}Note: This is a preview. Run 'python demo.py' for the interactive experience.")

if __name__ == "__main__":
    show_preview() 