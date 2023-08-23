@echo off
:: BatchGotAdmin
net session >nul 2>&1
if %errorLevel% == 0 (
   goto :isAdmin
) else (
   powershell start -verb runas "%~dp0\security_manager.py"
   exit /B
)
:isAdmin
