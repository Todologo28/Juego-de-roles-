"""
Clases de datos del juego RPG 3D Épico
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional
from enum import Enum
import json

class GameState(Enum):
    LOADING = "loading"
    CHARACTER_SELECT = "character_select"
    ENEMY_SELECT = "enemy_select"
    COMBAT = "combat"
    VICTORY = "victory"
    DEFEAT = "defeat"
    FINAL_SCREEN = "final_screen"

class CharacterClass(Enum):
    MAGE = "mago"
    KNIGHT = "caballero"

class EnemyType(Enum):
    GOBLIN = "duende"
    OGRE = "ogro"
    DRAGON = "dragon"

@dataclass
class Weapon:
    name: str
    attack: int
    magic: int = 0
    rarity: str = "común"
    icon: str = "⚔️"
    description: str = ""

    def to_dict(self):
        return {
            'name': self.name,
            'attack': self.attack,
            'magic': self.magic,
            'rarity': self.rarity,
            'icon': self.icon,
            'description': self.description
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

@dataclass
class Potion:
    name: str
    heal: int = 0
    mana: int = 0
    icon: str = "🧪"
    description: str = ""

    def to_dict(self):
        return {
            'name': self.name,
            'heal': self.heal,
            'mana': self.mana,
            'icon': self.icon,
            'description': self.description
        }

@dataclass
class PlayerData:
    name: str = ""
    class_type: str = ""
    level: int = 1
    hp: int = 100
    max_hp: int = 100
    mp: int = 50
    max_mp: int = 50
    xp: int = 0
    attack: int = 20
    defense: int = 10
    gold: int = 0
    inventory: List[Dict] = field(default_factory=list)
    equipped_weapon: Optional[Dict] = None
    defeated_enemies: List[str] = field(default_factory=list)
    win_streak: int = 0
    total_victories: int = 0

    def add_xp(self, amount):
        """Añadir experiencia y manejar subida de nivel"""
        self.xp += amount
        levels_gained = 0

        while self.xp >= 100:
            self.level += 1
            levels_gained += 1
            self.xp -= 100

            # Mejoras por nivel
            hp_bonus = 25 + (self.level * 5)
            mp_bonus = 15 + (self.level * 3)
            attack_bonus = 6 + (self.level * 2)
            defense_bonus = 4 + self.level

            self.max_hp += hp_bonus
            self.hp = self.max_hp  # Curación completa
            self.max_mp += mp_bonus
            self.mp = self.max_mp
            self.attack += attack_bonus
            self.defense += defense_bonus

        return levels_gained

    def equip_weapon(self, weapon_dict):
        """Equipar un arma"""
        if self.equipped_weapon:
            # Quitar stats del arma anterior
            self.attack -= self.equipped_weapon.get('attack', 0)

        self.equipped_weapon = weapon_dict
        self.attack += weapon_dict.get('attack', 0)

    def to_dict(self):
        return {
            'name': self.name,
            'class_type': self.class_type,
            'level': self.level,
            'hp': self.hp,
            'max_hp': self.max_hp,
            'mp': self.mp,
            'max_mp': self.max_mp,
            'xp': self.xp,
            'attack': self.attack,
            'defense': self.defense,
            'gold': self.gold,
            'inventory': self.inventory,
            'equipped_weapon': self.equipped_weapon,
            'defeated_enemies': self.defeated_enemies,
            'win_streak': self.win_streak,
            'total_victories': self.total_victories
        }

@dataclass
class EnemyData:
    name: str = ""
    type: str = ""
    level: int = 1
    hp: int = 80
    max_hp: int = 80
    attack: int = 15
    defense: int = 5
    dialogue: List[str] = field(default_factory=list)

    def reset_hp(self):
        """Restaurar HP completo"""
        self.hp = self.max_hp

@dataclass
class Quest:
    name: str
    description: str
    type: str  # 'defeat_all', 'win_streak', etc.
    progress: int = 0
    target: int = 1
    reward_gold: int = 0
    reward_xp: int = 0
    completed: bool = False

    def update_progress(self, amount=1):
        """Actualizar progreso de la misión"""
        self.progress = min(self.progress + amount, self.target)
        if self.progress >= self.target:
            self.completed = True
        return self.completed

# Colores del juego
class Colors:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GOLD = (255, 215, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 100, 255)
    PURPLE = (138, 43, 226)
    ORANGE = (255, 165, 0)
    DARK_BLUE = (0, 0, 139)
    LIME = (50, 205, 50)
    CYAN = (0, 255, 255)
    MAGENTA = (255, 0, 255)
    DARK_GREEN = (0, 100, 0)
    DARK_RED = (139, 0, 0)
    SILVER = (192, 192, 192)

# Configuración del juego
class GameConfig:
    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 800
    FPS = 60

    # Configuración de combate
    CRITICAL_CHANCE = 0.15  # 15% de crítico
    CRITICAL_MULTIPLIER = 2.5

    # Configuración de XP
    XP_PER_LEVEL = 100

    # Archivos
    SAVE_FILE = "saves/player_data.json"
    CONFIG_FILE = "config/settings.json"