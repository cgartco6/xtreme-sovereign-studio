@echo off
title XTREME SOVEREIGN STUDIO - LOCAL TEST
echo [SYSTEM] Starting Sovereign Orchestrator...
call .\venv\Scripts\activate
python autonomous_orchestrator.py
pause
