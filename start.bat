@echo off
title TokenForge Studio Launcher

echo =====================================
echo     Iniciando TokenForge Studio
echo =====================================

py launcher.py

if errorlevel 1 (
    python launcher.py
)

pause