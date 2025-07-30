# CORREGIR estas líneas en src/data/weapons.py:

# Línea 28-50 (corregir diccionario POTIONS):
POTIONS = {
    "health_potion": Potion(  # CAMBIAR: era "pocion_vida"
        name="Poción de Curación",  # CAMBIAR: era "Poción de Vida"
        effect_value=50,  # CAMBIAR: era heal=50
        effect_type="heal",  # AÑADIR
        icon="❤️",
        description="Restaura 50 puntos de vida al instante."
    ),
    "mana_potion": Potion(  # CAMBIAR: era "pocion_mana"
        name="Poción de Maná",
        effect_value=40,  # CAMBIAR: era mana=40
        effect_type="mana",  # AÑADIR
        icon="🔵",
        description="Restaura 40 puntos de maná mágico."
    ),
    "strength_potion": Potion(  # AÑADIR nueva poción
        name="Poción de Fuerza",
        effect_value=10,
        effect_type="strength",
        icon="💪",
        description="Aumenta temporalmente el ataque."
    ),
    "elixir_supremo": Potion(
        name="Elixir Supremo",
        effect_value=100,  # CAMBIAR: era heal=100, mana=60
        effect_type="heal_mana",  # CAMBIAR
        icon="✨",
        description="Poción legendaria que restaura vida y maná completamente."
    ),
    "pocion_resistencia": Potion(
        name="Poción de Resistencia",
        effect_value=25,  # CAMBIAR: era heal=25, mana=0
        effect_type="heal",  # CAMBIAR
        icon="🛡️",
        description="Restaura vida y aumenta defensa temporalmente."
    ),
    "agua_bendita": Potion(
        name="Agua Bendita",
        effect_value=30,  # CAMBIAR: era heal=30, mana=20
        effect_type="heal_mana",  # CAMBIAR
        icon="💧",
        description="Agua sagrada que purifica y cura."
    )
}