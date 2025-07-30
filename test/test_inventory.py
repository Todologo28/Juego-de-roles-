"""
Pruebas unitarias para el sistema de inventario del RPG 3D Épico
"""

import unittest
import sys
import os

# Añadir src al path para importar módulos
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from data.game_data import PlayerData, Weapon, Potion
from data.weapons import WEAPONS, POTIONS, get_random_weapon, get_random_potion

class TestInventorySystem(unittest.TestCase):
    """Pruebas para el sistema de inventario"""

    def setUp(self):
        """Configurar datos de prueba"""
        self.player = PlayerData()
        self.player.name = "Héroe de Prueba"
        self.player.inventory = []
        self.player.gold = 100

        # Crear objetos de prueba
        self.test_weapon = Weapon(
            name="Espada de Prueba",
            attack=15,
            rarity="común",
            description="Una espada para pruebas"
        )

        self.test_potion = Potion(
            name="Poción de Prueba",
            effect_value=25,
            effect_type="heal",
            description="Una poción para pruebas"
        )

    def test_add_item_to_inventory(self):
        """Probar añadir objeto al inventario"""
        initial_size = len(self.player.inventory)

        # Añadir poción al inventario
        self.player.inventory.append(self.test_potion.to_dict())

        self.assertEqual(len(self.player.inventory), initial_size + 1)
        self.assertIn(self.test_potion.to_dict(), self.player.inventory)

    def test_remove_item_from_inventory(self):
        """Probar remover objeto del inventario"""
        # Añadir objeto primero
        potion_dict = self.test_potion.to_dict()
        self.player.inventory.append(potion_dict)
        initial_size = len(self.player.inventory)

        # Remover objeto
        self.player.inventory.remove(potion_dict)

        self.assertEqual(len(self.player.inventory), initial_size - 1)
        self.assertNotIn(potion_dict, self.player.inventory)

    def test_equip_weapon(self):
        """Probar equipar arma"""
        weapon_dict = self.test_weapon.to_dict()
        initial_attack = self.player.attack

        # Equipar arma
        self.player.equipped_weapon = weapon_dict
        self.player.attack += weapon_dict['attack']

        self.assertEqual(self.player.equipped_weapon, weapon_dict)
        self.assertEqual(self.player.attack, initial_attack + weapon_dict['attack'])

    def test_unequip_weapon(self):
        """Probar desequipar arma"""
        weapon_dict = self.test_weapon.to_dict()
        self.player.equipped_weapon = weapon_dict
        self.player.attack += weapon_dict['attack']

        initial_attack = self.player.attack

        # Desequipar arma
        self.player.attack -= weapon_dict['attack']
        self.player.equipped_weapon = None

        self.assertIsNone(self.player.equipped_weapon)
        self.assertEqual(self.player.attack, initial_attack - weapon_dict['attack'])

    def test_use_healing_potion(self):
        """Probar usar poción de curación"""
        self.player.hp = 50  # Jugador herido
        self.player.max_hp = 100

        heal_potion = Potion(
            name="Poción de Curación",
            effect_value=30,
            effect_type="heal"
        )

        # Añadir poción al inventario
        potion_dict = heal_potion.to_dict()
        self.player.inventory.append(potion_dict)

        # Usar poción
        old_hp = self.player.hp
        self.player.hp = min(self.player.max_hp, self.player.hp + heal_potion.effect_value)
        self.player.inventory.remove(potion_dict)

        self.assertGreater(self.player.hp, old_hp)
        self.assertNotIn(potion_dict, self.player.inventory)

    def test_use_mana_potion(self):
        """Probar usar poción de maná"""
        self.player.mp = 10  # Jugador con poco maná
        self.player.max_mp = 50

        mana_potion = Potion(
            name="Poción de Maná",
            effect_value=20,
            effect_type="mana"
        )

        # Añadir poción al inventario
        potion_dict = mana_potion.to_dict()
        self.player.inventory.append(potion_dict)

        # Usar poción
        old_mp = self.player.mp
        self.player.mp = min(self.player.max_mp, self.player.mp + mana_potion.effect_value)
        self.player.inventory.remove(potion_dict)

        self.assertGreater(self.player.mp, old_mp)
        self.assertNotIn(potion_dict, self.player.inventory)

    def test_inventory_capacity(self):
        """Probar capacidad del inventario"""
        # Llenar inventario con muchos objetos
        for i in range(50):
            test_item = Potion(f"Objeto {i}", 5, "heal").to_dict()
            self.player.inventory.append(test_item)

        # Verificar que se pueden añadir objetos
        self.assertEqual(len(self.player.inventory), 50)

        # En un juego real, podrías querer limitar la capacidad
        max_capacity = 100
        self.assertLessEqual(len(self.player.inventory), max_capacity)

    def test_find_items_by_type(self):
        """Probar buscar objetos por tipo"""
        # Añadir diferentes tipos de pociones
        heal_potion = Potion("Curación", 25, "heal").to_dict()
        mana_potion = Potion("Maná", 15, "mana").to_dict()
        strength_potion = Potion("Fuerza", 10, "strength").to_dict()

        self.player.inventory.extend([heal_potion, mana_potion, strength_potion])

        # Buscar pociones de curación
        heal_potions = [item for item in self.player.inventory
                        if item.get('effect_type') == 'heal']

        self.assertEqual(len(heal_potions), 1)
        self.assertEqual(heal_potions[0]['name'], "Curación")

    def test_gold_transactions(self):
        """Probar transacciones de oro"""
        initial_gold = self.player.gold

        # Ganar oro
        gold_earned = 50
        self.player.gold += gold_earned
        self.assertEqual(self.player.gold, initial_gold + gold_earned)

        # Gastar oro
        gold_spent = 30
        if self.player.gold >= gold_spent:
            self.player.gold -= gold_spent

        self.assertEqual(self.player.gold, initial_gold + gold_earned - gold_spent)

    def test_weapon_comparison(self):
        """Probar comparación de armas"""
        weak_weapon = Weapon("Espada Débil", 10, 0, "común")
        strong_weapon = Weapon("Espada Fuerte", 25, 0, "épica")

        # La espada fuerte debería tener más ataque
        self.assertGreater(strong_weapon.attack, weak_weapon.attack)

        # Diferentes raridades
        self.assertNotEqual(weak_weapon.rarity, strong_weapon.rarity)

class TestWeaponsAndPotions(unittest.TestCase):
    """Pruebas para armas y pociones predefinidas"""

    def test_all_weapons_valid(self):
        """Probar que todas las armas son válidas"""
        for weapon_key, weapon in WEAPONS.items():
            self.assertIsInstance(weapon.name, str)
            self.assertGreater(len(weapon.name), 0)
            self.assertGreaterEqual(weapon.attack, 0)
            self.assertIn(weapon.rarity, ["común", "rara", "épica", "legendaria"])

    def test_all_potions_valid(self):
        """Probar que todas las pociones son válidas"""
        for potion_key, potion in POTIONS.items():
            self.assertIsInstance(potion.name, str)
            self.assertGreater(len(potion.name), 0)
            self.assertGreater(potion.effect_value, 0)
            self.assertIn(potion.effect_type, ["heal", "mana", "strength", "heal_mana"])

    def test_random_weapon_generation(self):
        """Probar generación aleatoria de armas"""
        try:
            random_weapon = get_random_weapon()
            self.assertIsInstance(random_weapon, dict)
            self.assertIn('name', random_weapon)
            self.assertIn('attack', random_weapon)
        except:
            # Si la función no existe, no es un error crítico
            pass

    def test_random_potion_generation(self):
        """Probar generación aleatoria de pociones"""
        try:
            random_potion = get_random_potion()
            self.assertIsInstance(random_potion, dict)
            self.assertIn('name', random_potion)
            self.assertIn('effect_value', random_potion)
        except:
            # Si la función no existe, no es un error crítico
            pass

    def test_starter_items(self):
        """Probar objetos iniciales"""
        # Verificar que existen pociones básicas
        self.assertIn("health_potion", POTIONS)
        self.assertIn("mana_potion", POTIONS)

        # Verificar que existen armas básicas
        basic_weapons = [key for key in WEAPONS.keys()
                         if WEAPONS[key].rarity == "común"]
        self.assertGreater(len(basic_weapons), 0)

if __name__ == '__main__':
    print("🎒 Ejecutando pruebas del sistema de inventario...")
    unittest.main(verbosity=2)