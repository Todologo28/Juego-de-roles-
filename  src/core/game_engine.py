"""
Motor principal del juego RPG 3D Épico - Versión gráfica completa
"""

import pygame
import sys
import math
import random
import time
from OpenGL.GL import *
from OpenGL.GLU import *

# Imports locales
from data.game_data import GameState, PlayerData, EnemyData, GameConfig
from data.weapons import WEAPONS, POTIONS
from data.enemies import ENEMY_CONFIGS
from models.player_models import MageModel, KnightModel
from models.enemy_models import EnemyModel
from core.renderer_3d import Renderer3D
from core.particle_system import ParticleSystem
from core.audio_manager import AudioManager
from ui.hud import HUD

class GameEngine:
    """Motor principal del juego con renderizado 3D épico"""

    def __init__(self):
        # Configuración de pantalla
        self.screen_width = 1200
        self.screen_height = 800
        self.fps = 60

        # Inicializar pygame y OpenGL
        pygame.init()
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height),
            pygame.DOUBLEBUF | pygame.OPENGL | pygame.RESIZABLE
        )
        pygame.display.set_caption("🎮 RPG 3D Épico - Batalla Definitiva")

        self.clock = pygame.time.Clock()
        self.running = True

        # Estados del juego
        self.game_state = GameState.CHARACTER_SELECT
        self.selected_character = None
        self.selected_enemy = None

        # Datos del juego
        self.player_data = PlayerData()
        self.enemy_data = EnemyData()
        self.game_config = GameConfig()

        # Sistemas del motor
        self.setup_opengl()
        self.renderer = Renderer3D()
        self.particle_system = ParticleSystem(self.renderer)
        self.audio_manager = AudioManager()
        self.hud = HUD(self.screen_width, self.screen_height)

        # Modelos 3D
        self.player_model = None
        self.enemy_model = None

        # Variables de combate
        self.is_player_turn = True
        self.animation_in_progress = False
        self.animation_timer = 0
        self.current_animation = None
        self.combat_log = []
        self.show_inventory = False
        self.show_controls = False

        # Variables de tiempo
        self.game_time = 0
        self.last_particle_time = 0

        # Cargar recursos
        self.audio_manager.load_default_sounds()

        print("🎮 Motor gráfico RPG 3D inicializado correctamente")
        print("🔥 ¡Prepárate para la batalla épica!")

    def setup_opengl(self):
        """Configurar OpenGL para renderizado 3D épico"""
        # Configuraciones básicas
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_CULL_FACE)
        glCullFace(GL_BACK)

        # Configurar perspectiva
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, self.screen_width/self.screen_height, 0.1, 100.0)

        # Configurar viewport
        glViewport(0, 0, self.screen_width, self.screen_height)

        print("✅ OpenGL configurado correctamente")

    def handle_events(self):
        """Manejar eventos del juego"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.VIDEORESIZE:
                self.screen_width, self.screen_height = event.size
                glViewport(0, 0, self.screen_width, self.screen_height)
                glMatrixMode(GL_PROJECTION)
                glLoadIdentity()
                gluPerspective(45, self.screen_width/self.screen_height, 0.1, 100.0)

            elif event.type == pygame.KEYDOWN:
                self.handle_keypress(event.key)

    def handle_keypress(self, key):
        """Manejar teclas presionadas"""
        if key == pygame.K_ESCAPE:
            if self.game_state == GameState.COMBAT:
                self.show_controls = not self.show_controls
            else:
                self.running = False

        elif key == pygame.K_q:
            self.running = False

        elif self.game_state == GameState.CHARACTER_SELECT:
            if key == pygame.K_1:
                self.select_character("mage")
            elif key == pygame.K_2:
                self.select_character("knight")

        elif self.game_state == GameState.ENEMY_SELECT:
            if key == pygame.K_1 and 'goblin' not in self.player_data.defeated_enemies:
                self.select_enemy("goblin")
            elif key == pygame.K_2 and 'ogre' not in self.player_data.defeated_enemies:
                self.select_enemy("ogre")
            elif key == pygame.K_3 and 'dragon' not in self.player_data.defeated_enemies:
                self.select_enemy("dragon")

        elif self.game_state == GameState.COMBAT and not self.animation_in_progress:
            if self.is_player_turn:
                if key == pygame.K_1:
                    self.player_attack()
                elif key == pygame.K_2:
                    self.show_spell_menu()
                elif key == pygame.K_3:
                    self.show_inventory = not self.show_inventory
                elif key == pygame.K_h and self.show_inventory:
                    self.use_healing_potion()

        elif self.game_state in [GameState.VICTORY, GameState.DEFEAT, GameState.FINAL_VICTORY]:
            if key == pygame.K_SPACE:
                if self.game_state == GameState.VICTORY:
                    self.continue_adventure()
                else:
                    self.restart_game()

    def select_character(self, character_type):
        """Seleccionar personaje jugador"""
        self.selected_character = character_type

        if character_type == "mage":
            self.player_data.name = "Mago Épico"
            self.player_data.character_class = "mage"
            self.player_data.hp = 80
            self.player_data.max_hp = 80
            self.player_data.mp = 120
            self.player_data.max_mp = 120
            self.player_data.attack = 25
            self.player_data.inventory = [POTIONS["health_potion"], POTIONS["mana_potion"]]
            self.player_model = MageModel(self.renderer)

        elif character_type == "knight":
            self.player_data.name = "Caballero Valiente"
            self.player_data.character_class = "knight"
            self.player_data.hp = 120
            self.player_data.max_hp = 120
            self.player_data.mp = 50
            self.player_data.max_mp = 50
            self.player_data.attack = 40
            self.player_data.inventory = [POTIONS["health_potion"], POTIONS["strength_potion"]]
            self.player_model = KnightModel(self.renderer)

        self.game_state = GameState.ENEMY_SELECT
        self.add_to_combat_log(f"🎭 Has elegido: {self.player_data.name}")
        self.audio_manager.play_sound("heal", 0.5)  # Sonido de selección

        print(f"👤 Personaje seleccionado: {self.player_data.name}")

    def select_enemy(self, enemy_type):
        """Seleccionar enemigo"""
        self.selected_enemy = enemy_type
        enemy_config = ENEMY_CONFIGS[enemy_type]

        self.enemy_data.name = enemy_config["name"]
        self.enemy_data.hp = enemy_config["hp"]
        self.enemy_data.max_hp = enemy_config["hp"]
        self.enemy_data.attack = enemy_config["attack"]
        self.enemy_data.enemy_type = enemy_type

        self.enemy_model = EnemyModel(self.renderer, enemy_type)

        self.game_state = GameState.COMBAT
        self.is_player_turn = True
        self.add_to_combat_log(f"⚔️ ¡Enfrentas a {self.enemy_data.name}!")
        self.audio_manager.play_sound("monster_roar", 0.6)

        # Generar partículas de inicio de combate
        self.particle_system.emit_explosion([0, 0, 0], (1, 0.5, 0), 30)

        print(f"👹 Enemigo seleccionado: {self.enemy_data.name}")

    def player_attack(self):
        """Ataque del jugador"""
        if self.animation_in_progress:
            return

        # Calcular daño
        base_damage = self.player_data.attack
        damage = random.randint(int(base_damage * 0.8), int(base_damage * 1.2))

        # Aplicar daño
        self.enemy_data.hp = max(0, self.enemy_data.hp - damage)

        # Efectos visuales y sonoros
        self.start_attack_animation()
        self.audio_manager.play_combat_sound("attack", self.player_data.character_class)

        # Partículas de impacto
        self.particle_system.emit_explosion([4, 0, 0], (1, 0, 0), 20)

        self.add_to_combat_log(f"⚔️ {self.player_data.name} ataca por {damage} de daño!")

        # Verificar si el enemigo murió
        if self.enemy_data.hp <= 0:
            self.enemy_defeated()
        else:
            self.is_player_turn = False
            self.schedule_enemy_turn()

    def show_spell_menu(self):
        """Mostrar menú de hechizos y lanzar hechizo aleatorio"""
        if self.player_data.mp < 20:
            self.add_to_combat_log("❌ No tienes suficiente MP para lanzar hechizos")
            return

        # Hechizos disponibles según la clase
        if self.player_data.character_class == "mage":
            spells = ["fireball", "ice_shard", "lightning"]
            spell = random.choice(spells)
            mp_cost = 25
            damage = random.randint(35, 50)
        else:  # knight
            spells = ["heal", "shield_bash"]
            spell = random.choice(spells)
            mp_cost = 20
            damage = random.randint(20, 35)

        # Consumir MP
        self.player_data.mp = max(0, self.player_data.mp - mp_cost)

        if spell == "heal":
            # Curación
            heal_amount = random.randint(30, 50)
            self.player_data.hp = min(self.player_data.max_hp, self.player_data.hp + heal_amount)
            self.add_to_combat_log(f"✨ {self.player_data.name} se cura {heal_amount} HP!")
            self.particle_system.emit_healing([-4, 1, 0], 1.0)
            self.audio_manager.play_sound("heal", 0.7)
        else:
            # Hechizo de daño
            self.enemy_data.hp = max(0, self.enemy_data.hp - damage)
            self.add_to_combat_log(f"🔥 {self.player_data.name} lanza {spell} por {damage} de daño!")

            # Efectos específicos por hechizo
            if spell == "fireball":
                self.particle_system.emit_fire([4, 1, 0], 1.0)
                self.audio_manager.play_sound("fireball", 0.8)
            elif spell == "ice_shard":
                self.particle_system.emit_ice([4, 1, 0], 1.0)
                self.audio_manager.play_sound("ice_spell", 0.8)
            elif spell == "lightning":
                self.particle_system.emit_lightning([-4, 2, 0], [4, 1, 0])
                self.audio_manager.play_sound("lightning", 0.8)

        self.start_spell_animation(spell)

        # Verificar si el enemigo murió
        if self.enemy_data.hp <= 0:
            self.enemy_defeated()
        else:
            self.is_player_turn = False
            self.schedule_enemy_turn()

    def use_healing_potion(self):
        """Usar poción de curación"""
        health_potions = [item for item in self.player_data.inventory if item.name == "Poción de Curación"]

        if not health_potions:
            self.add_to_combat_log("❌ No tienes pociones de curación")
            return

        # Usar poción
        potion = health_potions[0]
        self.player_data.inventory.remove(potion)

        heal_amount = potion.effect_value
        old_hp = self.player_data.hp
        self.player_data.hp = min(self.player_data.max_hp, self.player_data.hp + heal_amount)
        actual_heal = self.player_data.hp - old_hp

        self.add_to_combat_log(f"🧪 Usas {potion.name} y recuperas {actual_heal} HP!")

        # Efectos
        self.particle_system.emit_healing([-4, 1, 0], 0.8)
        self.audio_manager.play_sound("heal", 0.6)

        self.is_player_turn = False
        self.schedule_enemy_turn()

    def schedule_enemy_turn(self):
        """Programar turno del enemigo"""
        self.animation_in_progress = True
        self.animation_timer = 1.0  # 1 segundo de espera
        self.current_animation = "enemy_turn"

    def enemy_turn(self):
        """Turno del enemigo"""
        if self.enemy_data.hp <= 0:
            return

        # IA simple del enemigo
        action = random.choice(["attack", "special"])

        if action == "attack":
            damage = random.randint(int(self.enemy_data.attack * 0.8), int(self.enemy_data.attack * 1.2))
            self.player_data.hp = max(0, self.player_data.hp - damage)

            self.add_to_combat_log(f"👹 {self.enemy_data.name} te ataca por {damage} de daño!")

            # Efectos
            self.particle_system.emit_explosion([-4, 0, 0], (0.8, 0.2, 0.2), 15)
            self.audio_manager.play_sound("monster_roar", 0.5)

        else:  # special attack
            damage = int(self.enemy_data.attack * 1.5)
            self.player_data.hp = max(0, self.player_data.hp - damage)

            self.add_to_combat_log(f"🔥 {self.enemy_data.name} usa ataque especial por {damage} de daño!")

            # Efectos especiales según enemigo
            if self.enemy_data.enemy_type == "dragon":
                self.particle_system.emit_fire([-4, 1, 0], 1.2)
                self.audio_manager.play_sound("fireball", 0.9)
            elif self.enemy_data.enemy_type == "ogre":
                self.particle_system.emit_explosion([-4, 0, 0], (0.6, 0.4, 0.2), 25)
            else:  # goblin
                self.particle_system.emit_explosion([-4, 0, 0], (0.2, 0.7, 0.2), 20)

        # Verificar si el jugador murió
        if self.player_data.hp <= 0:
            self.game_state = GameState.DEFEAT
            self.add_to_combat_log("💀 Has sido derrotado...")
            self.audio_manager.play_sound("monster_roar", 1.0)
        else:
            self.is_player_turn = True

    def enemy_defeated(self):
        """Enemigo derrotado"""
        self.add_to_combat_log(f"🎉 ¡Has derrotado a {self.enemy_data.name}!")

        # Añadir a lista de derrotados
        self.player_data.defeated_enemies.append(self.enemy_data.enemy_type)

        # Subir de nivel
        self.player_data.level += 1
        self.player_data.experience += 100

        # Efectos de victoria
        self.particle_system.emit_explosion([4, 2, 0], (1, 1, 0), 50)
        self.audio_manager.play_sound("victory", 0.8)

        # Verificar si completó el juego
        if len(self.player_data.defeated_enemies) >= 3:
            self.game_state = GameState.FINAL_VICTORY
        else:
            self.game_state = GameState.VICTORY

    def continue_adventure(self):
        """Continuar aventura"""
        self.game_state = GameState.ENEMY_SELECT

        # Restaurar algo de HP y MP
        self.player_data.hp = min(self.player_data.max_hp, self.player_data.hp + 20)
        self.player_data.mp = min(self.player_data.max_mp, self.player_data.mp + 30)

        self.add_to_combat_log("🌟 ¡Continúas tu aventura!")

    def restart_game(self):
        """Reiniciar juego"""
        self.game_state = GameState.CHARACTER_SELECT
        self.player_data = PlayerData()
        self.enemy_data = EnemyData()
        self.combat_log.clear()
        self.particle_system.clear()

        print("🔄 Juego reiniciado")

    def start_attack_animation(self):
        """Iniciar animación de ataque"""
        self.animation_in_progress = True
        self.animation_timer = 0.5
        self.current_animation = "attack"

    def start_spell_animation(self, spell_type):
        """Iniciar animación de hechizo"""
        self.animation_in_progress = True
        self.animation_timer = 1.0
        self.current_animation = f"spell_{spell_type}"

    def update_animations(self, dt):
        """Actualizar animaciones"""
        if self.animation_in_progress:
            self.animation_timer -= dt

            if self.animation_timer <= 0:
                self.animation_in_progress = False

                if self.current_animation == "enemy_turn":
                    self.enemy_turn()

                self.current_animation = None

    def add_to_combat_log(self, message):
        """Añadir mensaje al log de combate"""
        self.combat_log.append(message)

        # Limitar el log a 50 mensajes
        if len(self.combat_log) > 50:
            self.combat_log = self.combat_log[-50:]

        print(f"📜 {message}")

    def update(self, dt):
        """Actualizar lógica del juego"""
        self.game_time += dt

        # Actualizar sistemas
        self.update_animations(dt)
        self.particle_system.update(dt)

        # Actualizar modelos
        if self.player_model:
            self.player_model.update(dt)
        if self.enemy_model:
            self.enemy_model.update(dt)

            # Actualizar salud del enemigo para efectos visuales
            if self.enemy_data.max_hp > 0:
                health_percent = self.enemy_data.hp / self.enemy_data.max_hp
                self.enemy_model.set_health_percent(health_percent)

        # Generar partículas ambientales ocasionalmente
        if self.game_time - self.last_particle_time > 2.0:
            if self.game_state == GameState.COMBAT:
                self.particle_system.emit_magic_aura([0, -1, 0], (0.3, 0.3, 0.8))
            self.last_particle_time = self.game_time

    def render(self):
        """Renderizar frame del juego"""
        # Limpiar pantalla
        self.renderer.clear_screen(0.05, 0.05, 0.15)

        # Configurar cámara según estado del juego
        if self.game_state == GameState.COMBAT:
            self.renderer.setup_camera(25, 45, 18)
        else:
            angle_y = 45 + 10 * math.sin(self.game_time * 0.5)
            self.renderer.setup_camera(20, angle_y, 20)

        # Renderizar elementos 3D
        if self.game_state in [GameState.COMBAT, GameState.VICTORY, GameState.DEFEAT]:
            # Suelo épico
            self.renderer.draw_floor(15)

            # Círculo mágico
            self.renderer.draw_magic_circle(8, self.game_time)

            # Elementos de fondo
            self.renderer.draw_background_elements(self.game_time)

            # Modelos de personajes
            if self.player_model:
                self.player_model.draw(self.game_time)

            if self.enemy_model and self.enemy_data.hp > 0:
                self.enemy_model.draw(self.game_time)

            # Sistema de partículas
            self.particle_system.render()

        # Renderizar UI según estado
        if self.game_state == GameState.CHARACTER_SELECT:
            self.render_character_select_ui()
        elif self.game_state == GameState.ENEMY_SELECT:
            self.render_enemy_select_ui()
        elif self.game_state == GameState.COMBAT:
            self.render_combat_ui()
        elif self.game_state == GameState.VICTORY:
            self.render_victory_ui()
        elif self.game_state == GameState.DEFEAT:
            self.render_defeat_ui()
        elif self.game_state == GameState.FINAL_VICTORY:
            self.render_final_victory_ui()

        # Intercambiar buffers
        pygame.display.flip()

    def render_character_select_ui(self):
        """Renderizar UI de selección de personaje"""
        # Por ahora, usamos la consola como UI
        if not hasattr(self, '_character_select_shown'):
            self.hud.render_character_select()
            self._character_select_shown = True

    def render_enemy_select_ui(self):
        """Renderizar UI de selección de enemigo"""
        if not hasattr(self, '_enemy_select_shown'):
            self.hud.render_enemy_select(self.player_data.defeated_enemies)
            self._enemy_select_shown = True
            del self._character_select_shown  # Reset para próxima vez

    def render_combat_ui(self):
        """Renderizar UI de combate"""
        # La UI se muestra en consola por ahora
        pass

    def render_victory_ui(self):
        """Renderizar UI de victoria"""
        if not hasattr(self, '_victory_shown'):
            self.hud.render_victory()
            print("Presiona ESPACIO para continuar")
            self._victory_shown = True

    def render_defeat_ui(self):
        """Renderizar UI de derrota"""
        if not hasattr(self, '_defeat_shown'):
            self.hud.render_defeat()
            print("Presiona ESPACIO para reiniciar")
            self._defeat_shown = True

    def render_final_victory_ui(self):
        """Renderizar UI de victoria final"""
        if not hasattr(self, '_final_victory_shown'):
            self.hud.render_final_screen(self.player_data)
            print("Presiona ESPACIO para reiniciar")
            self._final_victory_shown = True

    def run(self):
        """Bucle principal del juego"""
        print("🎮 Iniciando bucle principal...")
        print("🎯 Controles: 1-3 para acciones, ESC para salir")

        while self.running:
            dt = self.clock.tick(self.fps) / 1000.0

            self.handle_events()
            self.update(dt)
            self.render()

        # Limpiar al salir
        self.cleanup()

    def cleanup(self):
        """Limpiar recursos al salir"""
        print("🧹 Limpiando recursos...")
        if hasattr(self, 'audio_manager'):
            self.audio_manager.cleanup()
        pygame.quit()
        print("👋 ¡Gracias por jugar RPG 3D Épico!")