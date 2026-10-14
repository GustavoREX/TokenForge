@echo off
setlocal
pushd "%~dp0" || exit /b 1
set "TOKENFORGE_PYTHON=python"
if exist ".venv\Scripts\python.exe" set "TOKENFORGE_PYTHON=.venv\Scripts\python.exe"
"%TOKENFORGE_PYTHON%" main.py
set "RESULT=%ERRORLEVEL%"
if not "%RESULT%"=="0" echo Execute setup.bat para instalar as dependencias.
popd
endlocal & exit /b %RESULT%
