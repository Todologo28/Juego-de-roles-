#!/usr/bin/env python3
import sys
import os

def check_dependencies():
    print("🔍 Verificando dependencias...")
    missing_deps = []
    required = ['pygame', 'OpenGL', 'numpy', 'PIL']

    for package in required:
        try:
            __import__(package)
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package}")
            missing_deps.append(package)

    if missing_deps:
        print(f"⚠️ Dependencias faltantes: {missing_deps}")
        print("💡 Instalar con: pip install pygame PyOpenGL numpy pillow")
        return False
    else:
        print("🎉 ¡Todas las dependencias están instaladas!")
        return True

def setup_dev_environment():
    print("🛠️ Configurando entorno...")

    dirs = ["src", "src/core", "src/models", "src/data", "src/ui", "assets", "config", "saves", "tests"]
    for directory in dirs:
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
            print(f"📁 Creado: {directory}")
        else:
            print(f"✅ Existe: {directory}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1]

        if command == "check":
            check_dependencies()
        elif command == "dev-setup":
            setup_dev_environment()
        else:
            print("Comandos: check, dev-setup")
    else:
        print("🎮 RPG 3D Épico Setup")
        print("Uso: python setup.py [check|dev-setup]")