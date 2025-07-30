#!/usr/bin/env python3
"""
RPG 3D Épico - Batalla Definitiva
Punto de entrada principal del juego
"""

import sys
import os

# Añadir src al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from core.game_engine import GameEngine

def main():
    """Función principal"""
    print("🎮 Iniciando RPG 3D Épico...")

    try:
        game = GameEngine()
        game.run()
    except Exception as e:
        print(f"❌ Error crítico: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()