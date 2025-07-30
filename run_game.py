#!/usr/bin/env python3
"""
Script para ejecutar RPG 3D Épico
"""

import sys
import os

# Añadir src al path para imports
project_root = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(project_root, 'src')
sys.path.insert(0, src_path)

def main():
    """Ejecutar el juego"""
    print("🎮 Iniciando RPG 3D Épico...")
    print("🔥 Preparando batalla épica...")

    try:
        from core.game_engine import GameEngine
        game = GameEngine()
        game.run()
    except ImportError as e:
        print(f"❌ Error de importación: {e}")
        print("🔧 Asegúrate de que todas las dependencias estén instaladas:")
        print("   pip install pygame PyOpenGL PyOpenGL_accelerate numpy pillow")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error crítico: {e}")
        print("📝 Revisa la consola para más detalles")
        sys.exit(1)

if __name__ == "__main__":
    main()