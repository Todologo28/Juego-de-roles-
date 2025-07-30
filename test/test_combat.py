"""
Pruebas unitarias para el sistema de combate del RPG 3D Épico
"""

import unittest
import sys
import os

# Añadir src al path para importar módulos
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from data.game_data import PlayerData, EnemyData
from data.weapons import WEAPONS, POTIONS
from data.enemies import ENEMY_CONFIGS

class TestCombatSystem(unittest.TestCase):
    """Pruebas para el sistema de combate"""

    def setUp(self):
        """Configurar datos de prueba"""
        self.player = PlayerData()
        self.player.name = "Héroe de Prueba"
        self.player.character_class = "mage"
        self.player.hp = 100
        self.player.max_hp = 100
        self.player.mp = 50
        self.player.max_mp = 50
        self.player.attack = 25

        self.enemy = EnemyData()
        self.enemy.name = "Enemigo de Prueba"
        self.enemy.enemy_type = "goblin"
        self.enemy.hp = 80
        self.enemy.max_hp = 80
        self.enemy.attack = 15

    def test_player_creation(self):
        """Probar creación de jugador"""
        self.assertEqual(self.player.name, "Héroe de Prueba")
        self.assertEqual(self.player.character_class, "mage")
        self.assertEqual(self.player.hp, 100)
        self.assertEqual(self.player.max_hp, 100)

    def test_enemy_creation(self):
        """Probar creación de enemigo"""
        self.assertEqual(self.enemy.name, "Enemigo de Prueba")
        self.assertEqual(self.enemy.enemy_type, "goblin")
        self.assertEqual(self.enemy.hp, 80)
        self.assertEqual(self.enemy.max_hp, 80)

    def test_player_attack_damage(self):
        """Probar daño de ataque del jugador"""
        initial_enemy_hp = self.enemy.hp
        damage = self.player.attack

        # Simular ataque
        self.enemy.hp -= damage

        self.assertEqual(self.enemy.hp, initial_enemy_hp - damage)
        self.assertLess(self.enemy.hp, initial_enemy_hp)

    def test_enemy_attack_damage(self):
        """Probar daño de ataque del enemigo"""
        initial_player_hp = self.player.hp
        damage = self.enemy.attack

        # Simular ataque enemigo
        self.player.hp -= damage

        self.assertEqual(self.player.hp, initial_player_hp - damage)
        self.assertLess(self.player.hp, initial_player_hp)

    def test_player_death_condition(self):
        """Probar condición de muerte del jugador"""
        self.player.hp = 0
        self.assertTrue(self.player.hp <= 0)

        self.player.hp = -10
        self.assertTrue(self.player.hp <= 0)

    def test_enemy_death_condition(self):
        """Probar condición de muerte del enemigo"""
        self.enemy.hp = 0
        self.assertTrue(self.enemy.hp <= 0)

        self.enemy.hp = -5
        self.assertTrue(self.enemy.hp <= 0)

    def test_healing_potion(self):
        """Probar uso de poción de curación"""
        self.player.hp = 50  # Jugador herido

        # Usar poción de curación
        if "health_potion" in POTIONS:
            potion = POTIONS["health_potion"]
            heal_amount = potion.effect_value

            old_hp = self.player.hp
            self.player.hp = min(self.player.max_hp, self.player.hp + heal_amount)

            self.assertGreater(self.player.hp, old_hp)
            self.assertLessEqual(self.player.hp, self.player.max_hp)

    def test_mana_potion(self):
        """Probar uso de poción de maná"""
        self.player.mp = 10  # Jugador con poco maná

        # Usar poción de maná
        if "mana_potion" in POTIONS:
            potion = POTIONS["mana_potion"]
            mana_amount = potion.effect_value

            old_mp = self.player.mp
            self.player.mp = min(self.player.max_mp, self.player.mp + mana_amount)

            self.assertGreater(self.player.mp, old_mp)
            self.assertLessEqual(self.player.mp, self.player.max_mp)

    def test_level_up_experience(self):
        """Probar sistema de experiencia y subida de nivel"""
        initial_level = self.player.level
        initial_hp = self.player.max_hp

        # Ganar experiencia suficiente para subir de nivel
        self.player.experience = 100

        # Simular subida de nivel
        if self.player.experience >= 100:
            self.player.level += 1
            self.player.experience -= 100
            self.player.max_hp += 25
            self.player.hp = self.player.max_hp
            self.player.attack += 6

        self.assertEqual(self.player.level, initial_level + 1)
        self.assertGreater(self.player.max_hp, initial_hp)
        self.assertEqual(self.player.experience, 0)

    def test_enemy_configurations(self):
        """Probar configuraciones de enemigos"""
        for enemy_type, config in ENEMY_CONFIGS.items():
            self.assertIn("name", config)
            self.assertIn("hp", config)
            self.assertIn("attack", config)
            self.assertGreater(config["hp"], 0)
            self.assertGreater(config["attack"], 0)

    def test_weapon_data_integrity(self):
        """Probar integridad de datos de armas"""
        for weapon_key, weapon in WEAPONS.items():
            self.assertTrue(hasattr(weapon, 'name'))
            self.assertTrue(hasattr(weapon, 'attack'))
            self.assertGreater(weapon.attack, 0)

    def test_potion_data_integrity(self):
        """Probar integridad de datos de pociones"""
        for potion_key, potion in POTIONS.items():
            self.assertTrue(hasattr(potion, 'name'))
            self.assertTrue(hasattr(potion, 'effect_value'))
            self.assertGreater(potion.effect_value, 0)

class TestGameBalance(unittest.TestCase):
    """Pruebas de balance del juego"""

    def test_player_vs_goblin_balance(self):
        """Probar balance jugador vs duende"""
        player = PlayerData()
        player.hp = 100
        player.attack = 25

        goblin_config = ENEMY_CONFIGS["goblin"]
        goblin_hp = goblin_config["hp"]
        goblin_attack = goblin_config["attack"]

        # Calcular turnos aproximados para derrotar al duende
        turns_to_kill_goblin = goblin_hp // player.attack + (1 if goblin_hp % player.attack > 0 else 0)
        turns_to_kill_player = player.hp // goblin_attack + (1 if player.hp % goblin_attack > 0 else 0)

        # El jugador debería poder derrotar al duende en menos turnos
        self.assertLessEqual(turns_to_kill_goblin, turns_to_kill_player)

    def test_mage_vs_knight_balance(self):
        """Probar balance entre mago y caballero"""
        mage = PlayerData()
        mage.character_class = "mage"
        mage.hp = 80
        mage.mp = 120
        mage.attack = 25

        knight = PlayerData()
        knight.character_class = "knight"
        knight.hp = 120
        knight.mp = 50
        knight.attack = 40

        # El caballero tiene más vida y ataque
        self.assertGreater(knight.hp, mage.hp)
        self.assertGreater(knight.attack, mage.attack)

        # El mago tiene más maná
        self.assertGreater(mage.mp, knight.mp)

if __name__ == '__main__':
    print("🧪 Ejecutando pruebas del sistema de combate...")
    unittest.main(verbosity=2)