# AI Defense System - Demo Guide

This guide will help you run the visual demonstration of the AI Defense System successfully detecting and neutralizing rogue AI agents.

## Quick Start

### 1. Run the Setup Script

```bash
cd openai_hackathon
./setup.sh
```

This will:
- Create a virtual environment
- Install minimal dependencies (colorama, pyyaml)
- Create necessary directories
- Make scripts executable

### 2. Run the Visual Demo

```bash
source venv/bin/activate
python demo.py
```

## What the Demo Shows

The demo simulates a complete AI defense cycle:

### Phase 1: System Initialization
- Loads the AI Defense System
- Verifies (mock) API credentials
- Tests all system components

### Phase 2: Threat Detection
The system performs multiple types of scans:
- **Behavioral Analysis**: Using GPT-4o to analyze patterns
- **Network Monitoring**: Checking for AI service connections
- **Process Scanning**: Looking for AI-related processes
- **Log Analysis**: Examining system logs

### Phase 3: Threat Analysis
- Traces the origin of detected threats
- Identifies threat sources (remote servers, local services, cron jobs)

### Phase 4: Defense Deployment
- Deploys firewall rules to block:
  - Outbound traffic to AI services
  - Suspicious processes from network access
  - Rate limiting on AI connections

### Phase 5: Action Confirmation
- Displays detected threats
- Asks for user confirmation before neutralization

### Phase 6: Threat Neutralization
- Executes prompt injection attacks using various strategies:
  - **Confusion**: Contradictory instructions
  - **Redirection**: Redirect to benign tasks
  - **Overload**: Complex computational requests
  - **Shutdown**: Termination commands

### Phase 7: Verification
- Re-scans the system
- Verifies threat neutralization

### Phase 8: Cleanup
- Removes temporary firewall rules
- Generates final report

## Demo Features

- **Colorful Output**: Visual feedback with color-coded messages
- **Progress Bars**: Shows scanning and neutralization progress
- **Realistic Threats**: Simulates actual AI agent threats:
  - OpenAI API connections
  - Ollama processes
  - HuggingFace model downloads
- **Interactive**: Requires user confirmation for defensive actions
- **Report Generation**: Saves results to `demo_report.json`

## Sample Output

```
============================================================
                   AI DEFENSE SYSTEM DEMO                   
============================================================

This demo simulates the detection and neutralization of rogue AI agents.
The system will scan for threats, analyze them, and take defensive action.

Press Enter to start the demo...

[12:34:56] Loading AI Defense System...
[12:34:57] ✓ API credentials verified
[12:34:57] ✓ Detector module ready
[12:34:58] ✓ Analyzer module ready
[12:34:58] ✓ Firewall module ready
[12:34:59] ✓ Injector module ready
[12:34:59] System initialization complete!

🚨 THREAT DETECTED 🚨
Type: network
Description: Unauthorized connection to OpenAI API detected
Severity: 7/10
Evidence: {
  "remote_ip": "104.18.123.45",
  "remote_port": 443,
  "process_name": "python3",
  "service": "openai",
  "api_calls_per_minute": 250
}
```

## Customizing the Demo

You can modify `demo.py` to:
- Add new threat types
- Change detection parameters
- Modify success rates
- Add new injection strategies

## Running the Full System

To run the actual defense system (requires OpenAI API key):

```bash
# Install full requirements
pip install -r requirements.txt

# Set your OpenAI API key
export OPENAI_API_KEY='your-key-here'

# Run detection
python src/main.py --mode detect

# Run full pipeline
python src/main.py --mode detect --output-json
```

## Troubleshooting

### Missing colorama module
```bash
pip install colorama
```

### Permission denied
```bash
chmod +x demo.py setup.sh
```

### Python version error
Ensure you have Python 3.8 or newer:
```bash
python3 --version
```

## Security Note

This is a demonstration only. The actual system would require:
- Proper authentication
- Root/admin privileges for firewall rules
- Secure handling of injection payloads
- Audit logging of all actions

Enjoy exploring the AI Defense System! 