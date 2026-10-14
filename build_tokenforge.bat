@echo off
setlocal
pushd "%~dp0" || exit /b 1
set "TOKENFORGE_PYTHON=python"
set "PYINSTALLER_CONFIG_DIR=%~dp0build\pyinstaller-cache"
set "TOKENFORGE_CLEAN="
if /I "%~1"=="clean" set "TOKENFORGE_CLEAN=--clean"
if exist ".venv\Scripts\python.exe" set "TOKENFORGE_PYTHON=.venv\Scripts\python.exe"
"%TOKENFORGE_PYTHON%" -c "import ast, pathlib, PIL, numpy, ttkbootstrap, tkinterdnd2, onnxruntime, PyInstaller; import importlib.util; assert importlib.util.find_spec('rembg'), 'rembg ausente'; [ast.parse(p.read_text(encoding='utf-8'), filename=str(p)) for folder in ['core', 'modes'] for p in pathlib.Path(folder).glob('*.py')]; ast.parse(pathlib.Path('main.py').read_text(encoding='utf-8'))"
if errorlevel 1 (
    echo ERRO: dependencias ausentes ou fonte invalido. Execute setup.bat e tente novamente.
    goto :error
)
echo Compilando TokenForge. A biblioteca de IA pode tornar esta etapa demorada.
"%TOKENFORGE_PYTHON%" -m PyInstaller --noconfirm %TOKENFORGE_CLEAN% --onefile --windowed --name TokenForge --icon Token.ico --add-data "Token.ico;." --add-data "borders;borders" --collect-all tkinterdnd2 --collect-data ttkbootstrap --collect-data rembg --collect-binaries onnxruntime --copy-metadata rembg --copy-metadata onnxruntime --copy-metadata pymatting main.py
if errorlevel 1 goto :error
echo Concluido: dist\TokenForge.exe
popd
endlocal & exit /b 0
:error
echo Falha na compilacao.
popd
endlocal & exit /b 1
