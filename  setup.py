# 🔧 Crear setup.py paso a paso

## 📝 **OPCIÓN 1: Crear con PowerShell**

```powershell
# En tu carpeta RPG_3D_Epic, ejecuta:
New-Item -Path "setup.py" -ItemType File
```

Luego copia y pega el contenido del artefacto "setup.py" en el archivo.

## 📝 **OPCIÓN 2: Crear con comando echo (RECOMENDADO)**

```powershell
# Navega a tu carpeta
cd C:\Users\eynar\IdeaProjects\RPG_3D_Epic

# Crear setup.py básico
@"
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

    init_files = ["src/__init__.py", "src/core/__init__.py", "src/models/__init__.py",
                  "src/data/__init__.py", "src/ui/__init__.py", "tests/__init__.py"]

    for init_file in init_files:
        if not os.path.exists(init_file):
            with open(init_file, 'w') as f:
                f.write('"""Módulo"""\n')
            print(f"📄 Creado: {init_file}")

def print_info():
    print("🎮 RPG 3D Épico - Información del Proyecto")
    print("=" * 50)
    print("📦 Nombre: RPG 3D Épico")
    print("🔢 Versión: 1.0.0")
    print("🐍 Python requerido: >=3.8")
    print("👨‍💻 Desarrollador: Epic Games Studio")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1]

        if command == "check":
            check_dependencies()
        elif command == "dev-setup":
            setup_dev_environment()
        elif command == "info":
            print_info()
        else:
            print("Comandos: check, dev-setup, info")
    else:
        print("🎮 RPG 3D Épico Setup")
        print("Uso: python setup.py [check|dev-setup|info]")
"@ | Out-File -FilePath "setup.py" -Encoding UTF8
```

## 📝 **OPCIÓN 3: Usando el IDE (MÁS FÁCIL)**

1. **En IntelliJ IDEA o tu editor:**
- Clic derecho en la carpeta raíz `RPG_3D_Epic`
- `New` → `File`
- Nombre: `setup.py`

2. **Copia y pega este contenido:**

```python
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

    init_files = ["src/__init__.py", "src/core/__init__.py", "src/models/__init__.py",
                  "src/data/__init__.py", "src/ui/__init__.py", "tests/__init__.py"]

    for init_file in init_files:
        if not os.path.exists(init_file):
            with open(init_file, 'w') as f:
                f.write('"""Módulo"""\n')
            print(f"📄 Creado: {init_file}")

def print_info():
    print("🎮 RPG 3D Épico - Información del Proyecto")
    print("=" * 50)
    print("📦 Nombre: RPG 3D Épico")
    print("🔢 Versión: 1.0.0")
    print("🐍 Python requerido: >=3.8")
    print("👨‍💻 Desarrollador: Epic Games Studio")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1]

        if command == "check":
            check_dependencies()
        elif command == "dev-setup":
            setup_dev_environment()
        elif command == "info":
            print_info()
        else:
            print("Comandos: check, dev-setup, info")
    else:
        print("🎮 RPG 3D Épico Setup")
        print("Uso: python setup.py [check|dev-setup|info]")
```

## 🚀 **Después de crear setup.py:**

```powershell
# 1. Verificar dependencias
python setup.py check

# 2. Configurar proyecto
python setup.py dev-setup

# 3. ¡Ejecutar el juego!
python run_game.py
```