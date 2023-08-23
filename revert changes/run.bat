@echo off
:: BatchGotAdmin
net session >nul 2>&1
if %errorLevel% == 0 (
   goto :isAdmin
) else (
   powershell start -verb runas "%~dp0\revert_changes.py"
   exit /B
)
:isAdmin