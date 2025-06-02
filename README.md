# AI Defense System - OpenAI Hackathon

## Overview

This project implements an AI-powered defense system that detects and neutralizes hostile AI agents using OpenAI's GPT-4o model. The system operates through GitHub Actions with daily scheduled scans to identify, trace, and neutralize rogue AI agents.

## Features

- **Hostile Agent Detection**: Fine-tuned GPT-4o model to identify malicious AI behavior patterns
- **Origin Tracing**: Advanced analysis to determine the source of hostile agents
- **Dynamic Firewall**: Automated protective barriers against detected threats
- **Prompt Injection Defense**: Counter-offensive capabilities to neutralize or redirect hostile agents
- **Automated Workflow**: GitHub Actions integration for scheduled security scans

## Architecture

```
├── src/
│   ├── detectors/      # AI agent detection modules
│   ├── analyzers/      # Threat analysis and tracing
│   ├── defenders/      # Firewall and injection mechanisms
│   └── utils/          # Helper functions and utilities
├── config/             # Configuration files
├── tests/              # Test suites
├── logs/               # System logs
└── .github/workflows/  # GitHub Actions workflows
```

## Setup

1. Clone the repository
2. Set up GitHub Secrets:
   - `OPENAI_API_KEY`: Your OpenAI API key
   - `DEFENDER_MODEL_ID`: Fine-tuned model ID
   - `NOTIFICATION_WEBHOOK`: Webhook for alerts
   - `SECURITY_TOKEN`: Authentication token

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Detection Methods

The system employs multiple detection strategies:

1. **Behavioral Analysis**: Monitoring API call patterns and response characteristics
2. **Network Traffic Analysis**: Detecting unusual communication patterns
3. **Process Monitoring**: Identifying suspicious process spawning
4. **Log Analysis**: Scanning system logs for AI agent fingerprints
5. **Memory Pattern Detection**: Identifying AI model artifacts in memory

## Security Workflow

1. **Daily Scan Activation** (via GitHub Actions)
2. **Multi-vector Detection** (behavioral, network, process)
3. **Threat Origin Analysis**
4. **Firewall Deployment**
5. **Confirmation Request**
6. **Prompt Injection Attack**
7. **Success Verification**
8. **Firewall Removal**

## Usage

Run the detection system manually:
```bash
python src/main.py --mode detect
```

Run full defense cycle:
```bash
python src/main.py --mode defend --auto-confirm
```

## Safety Considerations

This system is designed for defensive purposes only. Always:
- Obtain proper authorization before deployment
- Test in isolated environments first
- Review logs before confirming actions
- Maintain audit trails of all operations

## License

MIT License - See LICENSE file for details 