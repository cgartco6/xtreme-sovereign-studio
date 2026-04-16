# Sovereign Infinity - Windows Ignition Script
Write-Host "Initializing Sovereign Environment on Windows 10 Pro..." -ForegroundColor Cyan

# 1. Install Chocolatey (Package Manager) if not present
if (!(Get-Command choco -ErrorAction SilentlyContinue)) {
    Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
}

# 2. Install Python, Git, and FFmpeg (for Media Engine)
choco install python git ffmpeg -y

# 3. Setup Virtual Environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# 4. Install Requirements
pip install -r requirements.txt

Write-Host "Windows Ignition Complete. Populate your .env and run autonomous_orchestrator.py" -ForegroundColor Green
