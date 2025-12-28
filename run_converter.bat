@echo off
pushd "%~dp0"
echo Starting PDF to JPG Converter...
python scripts/converter.py
echo.
echo ===================================================
echo Execution finished. Press any key to close window.
echo ===================================================
pause >nul
popd
