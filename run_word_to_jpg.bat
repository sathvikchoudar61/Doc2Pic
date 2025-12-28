@echo off
pushd "%~dp0"
echo Starting Word to JPG Converter...
echo Please ensure your Word files are in the "input_word" folder.
python scripts/word_to_jpg.py
echo.
echo ===================================================
echo Execution finished. Press any key to close window.
echo ===================================================
pause >nul
popd
