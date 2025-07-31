"""
Datos y estructuras principales del juego RPG 3D Épico
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Dict, Optional

# Estados del juego
class GameState(Enum):
    LOADING = "loading"
    CHARACTER_SELECT = "character_select"
    ENEMY_SELECT = "enemy_select"
    COMBAT = "combat"
    VICTORY = "victory"
    DEFEAT = "defeat"
    FINAL_VICTORY = "final_victory"

# Colores para la interfaz
class Colors:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    PURPLE = (128, 0, 128)
    ORANGE = (255, 165, 0)
    CYAN = (0, 255, 255)
    MAGENTA = (255, 0, 255)
    LIME = (0, 255, 0)
    GOLD = (255, 215, 0)
    SILVER = (192, 192, 192)

@dataclass
class Weapon:
    name: str
    attack: int = 0
    magic_power: int = 0
    rarity: str = "común"
    icon: str = "⚔️"
    description: str = ""

    def to_dict(self):
        return {
            'name': self.name,
            'attack': self.attack,
            'magic_power': self.magic_power,
            'rarity': self.rarity,
            'icon': self.icon,
            'description': self.description
        }

@dataclass
class Potion:
    name: str
    effect_value: int = 0
    effect_type: str = "heal"
    icon: str = "🧪"
    description: str = ""

    def to_dict(self):
        return {
            'name': self.name,
            'effect_value': self.effect_value,
            'effect_type': self.effect_type,
            'icon': self.icon,
            'description': self.description
        }

@dataclass
class PlayerData:
    name: str = ""
    character_class: str = ""
    level: int = 1
    hp: int = 100
    max_hp: int = 100
    mp: int = 50
    max_mp: int = 50
    experience: int = 0
    attack: int = 20
    defense: int = 10
    gold: int = 0
    inventory: List = field(default_factory=list)
    equipped_weapon: Optional[Dict] = None
    defeated_enemies: List[str] = field(default_factory=list)
    win_streak: int = 0
    total_victories: int = 0

@dataclass
class EnemyData:
    name: str = ""
    enemy_type: str = ""
    level: int = 1
    hp: int = 80
    max_hp: int = 80
    attack: int = 15
    defense: int = 5
    dialogue: List[str] = field(default_factory=list)

@dataclass
class GameConfig:
    screen_width: int = 1200
    screen_height: int = 800
    fps: int = 60
    volume: float = 0.7
    debug_mode: bool = False