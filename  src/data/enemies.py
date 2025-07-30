# CORREGIR estas líneas en src/data/enemies.py:

# Línea 8-10 (corregir diccionario ENEMY_CONFIGS):
ENEMY_CONFIGS = {
    "goblin": {  # CAMBIAR: era "duende"
        "name": "🧌 Duende Siniestro",
        "level": 1,
        "hp": 80,
        "max_hp": 80,
        "attack": 18,
        "defense": 8,
        "xp_reward": 60,
        "gold_reward": 75,
        "description": "Un duende ágil y astuto de las sombras del bosque.",
        "special_attacks": ["ataque_sombra", "combo_dagas"],
        "resistances": ["poison"],
        "weaknesses": ["light"]
    },
    "ogre": {  # CAMBIAR: era "ogro"
        "name": "👹 Ogro Devastador",
        "level": 2,
        "hp": 150,
        "max_hp": 150,
        "attack": 28,
        "defense": 15,
        "xp_reward": 100,
        "gold_reward": 120,
        "description": "Un ogro masivo de las montañas con una maza destructiva.",
        "special_attacks": ["golpe_devastador", "grito_guerra"],
        "resistances": ["physical"],
        "weaknesses": ["magic"]
    },
    "dragon": {  # YA ERA "dragon" - NO CAMBIAR
        "name": "🐉 Dragón Sombrío",
        "level": 3,
        "hp": 250,
        "max_hp": 250,
        "attack": 40,
        "defense": 25,
        "xp_reward": 200,
        "gold_reward": 300,
        "description": "El señor ancestral del fuego eterno. Jefe final épico.",
        "special_attacks": ["aliento_fuego", "lluvia_llamas", "rugido_dragon"],
        "resistances": ["fire", "physical"],
        "weaknesses": ["ice", "holy"]
    }
}

# Línea 40-50 (corregir diccionario ENEMY_DIALOGUES):
ENEMY_DIALOGUES = {
    "goblin": [  # CAMBIAR: era "duende"
        "¡No saldrás vivo de aquí, intruso!",
        "¡Mi daga probará tu sangre!",
        "¡Las sombras me protegen!",
        "¡Eres más débil de lo que pensaba!",
        "¡Esto no ha terminado!",
        "¡El bosque vengará mi muerte!",
        "¡Jejeje... caerás como todos los demás!",
        "¡Mis hermanos escucharán de esto!"
    ],
    "ogre": [  # CAMBIAR: era "ogro"
        "¡OGRO APLASTARÁ HUESOS!",
        "¡TÚ SER COMIDA PARA OGRO!",
        "¡MAZA PESADA, TÚ FRÁGIL!",
        "¡GRRAAAAAHHH!",
        "¡OGRO NO CONOCE MIEDO!",
        "¡MONTAÑAS TEMBLAR CUANDO OGRO ENOJA!",
        "¡TÚ NO PODER CON FUERZA DE OGRO!",
        "¡OGRO DESTRUIR TODO!"
    ],
    "dragon": [  # YA ERA "dragon" - NO CAMBIAR
        "¡Mortal insolente! ¡Conoce el poder ancestral!",
        "¡Mis llamas han consumido mil ejércitos!",
        "¡Tu valor es admirable... pero inútil!",
        "¡El fuego eterno será tu tumba!",
        "¡Imposible... un simple mortal no puede...!",
        "¡He dormido durante milenios esperando este momento!",
        "¡Las llamas del inframundo arden en mi interior!"
    ]
}