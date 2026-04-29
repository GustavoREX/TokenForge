# -*- coding: utf-8 -*-
import subprocess
import sys
import os
import traceback

# pacote pip : modulo importado
CHECKS = {
    "ttkbootstrap": "ttkbootstrap",
    "pillow": "PIL",
    "rembg": "rembg",
    "onnxruntime": "onnxruntime",
    "tkinterdnd2": "tkinterdnd2"
}

def print_line():
    print("=" * 50)

def ensure_pip():
    try:
        import pip
    except Exception:
        print("pip não encontrado.")
        sys.exit(1)

def install_requirements():
    print_line()
    print("Verificando dependências...")
    print_line()

    for package, module in CHECKS.items():
        try:
            __import__(module)
            print(f"[OK] {package}")
        except Exception:
            print(f"[INSTALL] {package}")
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", package]
            )

def ensure_folders():
    folders = ["borders", "core", "modes"]

    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder, exist_ok=True)

def run_app():
    print_line()
    print("Iniciando TokenForge Studio...")
    print_line()

    subprocess.call([sys.executable, "main.py"])

def main():
    try:
        ensure_pip()
        ensure_folders()
        install_requirements()
        run_app()

    except Exception:
        print_line()
        print("Erro ao iniciar:")
        print(traceback.format_exc())
        input("Pressione ENTER para sair...")

if __name__ == "__main__":
    main()