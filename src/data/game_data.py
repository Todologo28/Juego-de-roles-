from enum import Enum
from dataclasses import dataclass

class GameState(Enum):
    CHARACTER_SELECT = "character_select"
    COMBAT = "combat"
    VICTORY = "victory"

@dataclass
class PlayerData:
    name: str = ""
    character_class: str = ""
    hp: int = 100
    max_hp: int = 100
    mp: int = 50
    max_mp: int = 50

@dataclass
class EnemyData:
    name: str = ""
    hp: int = 80
    max_hp: int = 80

@dataclass
class GameConfig:
    screen_width: int = 1200
    screen_height: int = 800
