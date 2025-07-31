#!/usr/bin/env python3
"""
🎮 RPG 3D Épico - Script Principal
"""

import sys
import os
import traceback

# Añadir src al path
current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(current_dir, 'src')
sys.path.insert(0, src_path)

def main():
    """Función principal"""
    print("🎮 Iniciando RPG 3D Épico...")
    print("=" * 50)

    # Verificar Python
    if sys.version_info < (3, 8):
        print("❌ Error: Se requiere Python 3.8+")
        sys.exit(1)

    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")

    # Verificar dependencias básicas
    try:
        import pygame
        import OpenGL.GL
        import numpy
        print("✅ Todas las dependencias encontradas")
    except ImportError as e:
        print(f"❌ Dependencia faltante: {e}")
        print("💡 Instalar con: pip install pygame PyOpenGL numpy pillow")
        sys.exit(1)

    print("🚀 Iniciando juego...")
    print("=" * 50)

    try:
        # Importar el motor del juego
        from core.game_engine import GameEngine

        # Crear y ejecutar el juego
        game = GameEngine()
        game.run()

    except ImportError as e:
        print(f"❌ Error importando módulos: {e}")
        print("📁 Verificando archivos necesarios:")

        # Mostrar qué archivos faltan
        required_files = [
            ('src/core/game_engine.py', 'Motor del juego'),
            ('src/data/game_data.py', 'Datos del juego'),
            ('src/data/weapons.py', 'Armas y pociones'),
            ('src/data/enemies.py', 'Configuración enemigos')
        ]

        for file_path, description in required_files:
            if os.path.exists(file_path):
                print(f"   ✅ {file_path} - {description}")
            else:
                print(f"   ❌ {file_path} - {description}")

        print("\n💡 Crea los archivos faltantes y vuelve a intentar")
        traceback.print_exc()
        sys.exit(1)

    except Exception as e:
        print(f"❌ Error durante la ejecución: {e}")
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()