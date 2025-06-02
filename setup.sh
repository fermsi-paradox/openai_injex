#!/bin/bash
# AI Defense System - Setup Script

echo "==================================="
echo "AI Defense System - Setup"
echo "==================================="

# Check Python version
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "Python version: $python_version"

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install minimal requirements for demo
echo "Installing demo requirements..."
pip install colorama pyyaml

# Create necessary directories
echo "Creating directories..."
mkdir -p logs
mkdir -p output

# Make scripts executable
chmod +x demo.py
chmod +x src/main.py

echo ""
echo "==================================="
echo "Setup complete!"
echo "==================================="
echo ""
echo "To run the visual demo:"
echo "  source venv/bin/activate"
echo "  python demo.py"
echo ""
echo "To install full requirements:"
echo "  pip install -r requirements.txt"
echo ""
echo "Note: The full system requires an OpenAI API key"
echo "Set it as: export OPENAI_API_KEY='your-key-here'"
echo "" 