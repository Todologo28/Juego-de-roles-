"""
Datos de armas, pociones y objetos del juego
"""

from data.game_data import Weapon, Potion

# ============================================================================
# ARMAS ÉPICAS
# ============================================================================

WEAPONS = {
    "espada_hierro": Weapon(
        name="Espada de Hierro",
        attack=8,
        rarity="común",
        icon="⚔️",
        description="Una espada básica pero confiable de hierro forjado."
    ),
    "espada_elfica": Weapon(
        name="Hoja Élfica",
        attack=15,
        rarity="rara",
        icon="🗡️",
        description="Espada ligera forjada por elfos, increíblemente afilada."
    ),
    "excalibur": Weapon(
        name="Excálibur",
        attack=30,
        rarity="legendaria",
        icon="⚡",
        description="La espada legendaria de los reyes. Brilla con poder divino."
    ),
    "baston_arcano": Weapon(
        name="Bastón Arcano",
        attack=5,
        magic=20,
        rarity="común",
        icon="🪄",
        description="Bastón básico que canaliza energía mágica."
    ),
    "vara_poder": Weapon(
        name="Vara del Poder Supremo",
        attack=12,
        magic=40,
        rarity="legendaria",
        icon="🔮",
        description="Vara legendaria que contiene el poder de mil magos."
    ),
    "daga_sombras": Weapon(
        name="Daga de las Sombras",
        attack=18,
        rarity="épica",
        icon="🗡️",
        description="Daga que se oculta en las sombras. Críticos más frecuentes."
    ),
    "martillo_titan": Weapon(
        name="Martillo del Titán",
        attack=35,
        rarity="legendaria",
        icon="🔨",
        description="Martillo de guerra que puede quebrar montañas."
    ),
    "arco_lunar": Weapon(
        name="Arco Lunar",
        attack=22,
        magic=10,
        rarity="épica",
        icon="🏹",
        description="Arco bendecido por la luna. Sus flechas nunca fallan."
    )
}

# ============================================================================
# POCIONES MÁGICAS
# ============================================================================

POTIONS = {
    "pocion_vida": Potion(
        name="Poción de Vida",
        heal=50,
        icon="❤️",
        description="Restaura 50 puntos de vida al instante."
    ),
    "pocion_mana": Potion(
        name="Poción de Maná",
        mana=40,
        icon="🔵",
        description="Restaura 40 puntos de maná mágico."
    ),
    "elixir_supremo": Potion(
        name="Elixir Supremo",
        heal=100,
        mana=60,
        icon="✨",
        description="Poción legendaria que restaura vida y maná completamente."
    ),
    "pocion_fuerza": Potion(
        name="Poción de Fuerza",
        heal=0,
        mana=0,
        icon="💪",
        description="Aumenta temporalmente el ataque en combate."
    ),
    "pocion_resistencia": Potion(
        name="Poción de Resistencia",
        heal=25,
        mana=0,
        icon="🛡️",
        description="Restaura vida y aumenta defensa temporalmente."
    ),
    "agua_bendita": Potion(
        name="Agua Bendita",
        heal=30,
        mana=20,
        icon="💧",
        description="Agua sagrada que purifica y cura."
    )
}

# ============================================================================
# SETS DE ARMAS POR CLASE
# ============================================================================

MAGE_WEAPONS = ["baston_arcano", "vara_poder", "arco_lunar"]
KNIGHT_WEAPONS = ["espada_hierro", "espada_elfica", "excalibur", "daga_sombras", "martillo_titan"]

# ============================================================================
# FUNCIONES DE UTILIDAD
# ============================================================================

def get_random_weapon(character_class=None):
    """Obtener un arma aleatoria, opcionalmente filtrada por clase"""
    import random

    if character_class == "mago":
        weapon_keys = MAGE_WEAPONS
    elif character_class == "caballero":
        weapon_keys = KNIGHT_WEAPONS
    else:
        weapon_keys = list(WEAPONS.keys())

    weapon_key = random.choice(weapon_keys)
    return WEAPONS[weapon_key].to_dict()

def get_random_potion():
    """Obtener una poción aleatoria"""
    import random

    potion_key = random.choice(list(POTIONS.keys()))
    return POTIONS[potion_key].to_dict()

def get_weapon_by_name(name):
    """Obtener arma por nombre"""
    for weapon in WEAPONS.values():
        if weapon.name == name:
            return weapon.to_dict()
    return None

def get_potion_by_name(name):
    """Obtener poción por nombre"""
    for potion in POTIONS.values():
        if potion.name == name:
            return potion.to_dict()
    return None

def get_starter_weapon(character_class):
    """Obtener arma inicial según la clase"""
    if character_class == "mago":
        return WEAPONS["baston_arcano"].to_dict()
    elif character_class == "caballero":
        return WEAPONS["espada_hierro"].to_dict()
    else:
        return WEAPONS["espada_hierro"].to_dict()

def get_starter_potions():
    """Obtener pociones iniciales"""
    return [
        POTIONS["pocion_vida"].to_dict(),
        POTIONS["pocion_mana"].to_dict()
    ]

# ============================================================================
# SISTEMA DE RAREZA Y PROBABILIDADES
# ============================================================================

RARITY_COLORS = {
    "común": (200, 200, 200),      # Gris
    "rara": (0, 150, 255),         # Azul
    "épica": (163, 53, 238),       # Púrpura
    "legendaria": (255, 215, 0)    # Dorado
}

RARITY_CHANCES = {
    "común": 0.60,       # 60%
    "rara": 0.25,        # 25%
    "épica": 0.12,       # 12%
    "legendaria": 0.03   # 3%
}

def get_random_loot(character_class=None, bonus_chance=0.0):
    """
    Generar loot aleatorio con sistema de rareza
    bonus_chance: bonificación para obtener objetos mejores
    """
    import random

    loot = []

    # Probabilidad de obtener poción (70% base)
    if random.random() < 0.7:
        loot.append(get_random_potion())

    # Probabilidad de obtener arma (30% base + bonus)
    weapon_chance = 0.3 + bonus_chance
    if random.random() < weapon_chance:
        # Determinar rareza
        roll = random.random()
        cumulative = 0

        for rarity, chance in RARITY_CHANCES.items():
            cumulative += chance
            if roll <= cumulative:
                # Buscar arma de esta rareza
                available_weapons = [w for w in WEAPONS.values() if w.rarity == rarity]
                if character_class:
                    if character_class == "mago":
                        available_weapons = [w for w in available_weapons if w.magic > 0 or w.name in ["Arco Lunar"]]
                    elif character_class == "caballero":
                        available_weapons = [w for w in available_weapons if w.magic == 0 or w.name in ["Arco Lunar"]]

                if available_weapons:
                    weapon = random.choice(available_weapons)
                    loot.append(weapon.to_dict())
                break

    return loot