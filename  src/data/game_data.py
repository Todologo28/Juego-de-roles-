# CORREGIR estas líneas en src/data/game_data.py:

# Línea 11-12 (corregir enum):
class GameState(Enum):
    LOADING = "loading"
    CHARACTER_SELECT = "character_select"  # Era "character_selecsrc" (cortado)
    ENEMY_SELECT = "enemy_select"
    COMBAT = "combat"
    VICTORY = "victory"
    DEFEAT = "defeat"
    FINAL_VICTORY = "final_victory"  # AÑADIR esta línea

# Línea 34-40 (corregir clase Potion):
@dataclass
class Potion:
    name: str
    effect_value: int = 0  # CAMBIAR: era heal/mana separados
    effect_type: str = "heal"  # AÑADIR: nuevo campo
    icon: str = "🧪"
    description: str = ""

    def to_dict(self):
        return {
            'name': self.name,
            'effect_value': self.effect_value,  # CAMBIAR
            'effect_type': self.effect_type,    # AÑADIR
            'icon': self.icon,
            'description': self.description
        }

# Línea 60-70 (corregir clase PlayerData):
@dataclass
class PlayerData:
    name: str = ""
    character_class: str = ""  # CAMBIAR: era class_type
    level: int = 1
    hp: int = 100
    max_hp: int = 100
    mp: int = 50
    max_mp: int = 50
    experience: int = 0  # CAMBIAR: era xp
    attack: int = 20
    defense: int = 10
    gold: int = 0
    inventory: List = field(default_factory=list)  # CAMBIAR: no Dict
    equipped_weapon: Optional[Dict] = None
    defeated_enemies: List[str] = field(default_factory=list)
    win_streak: int = 0
    total_victories: int = 0

# Línea 102 (corregir clase EnemyData):
@dataclass
class EnemyData:
    name: str = ""
    enemy_type: str = ""  # CAMBIAR: era type
    level: int = 1
    hp: int = 80
    max_hp: int = 80
    attack: int = 15
    defense: int = 5
    dialogue: List[str] = field(default_factory=list)