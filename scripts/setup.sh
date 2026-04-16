#!/bin/bash
# Sovereign Infinity - Ubuntu 24.04.3 Ignition
echo "Initializing Sovereign Engine on Ubuntu..."

# 1. Update and Install Essentials
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-venv git ffmpeg build-essential libssl-dev -y

# 2. Setup Active Memory Persistence
python3 -m venv venv
source venv/bin/activate

# 3. Install 2026 Sovereign Stack
pip install --upgrade pip
pip install -r requirements.txt

# 4. Final Permissions
chmod +x autonomous_orchestrator.py

echo "Ubuntu Ignition Complete. Sovereign Engine is ready for the Global Blitz."
