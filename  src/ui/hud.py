"""
Sistema de HUD (Heads-Up Display) para RPG 3D Épico
"""

import pygame
from OpenGL.GL import *
from data.game_data import Colors

class HUD:
    """Sistema de interfaz de usuario"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

        # Inicializar pygame para texto
        pygame.font.init()
        self.font_large = pygame.font.Font(None, 48)
        self.font_medium = pygame.font.Font(None, 32)
        self.font_small = pygame.font.Font(None, 24)

        # Estados
        self.messages = []
        self.fade_time = 0

    def update(self, dt, player_data, enemy_data=None):
        """Actualizar HUD"""
        self.fade_time += dt

    def render_character_select(self):
        """Renderizar pantalla de selección de personaje"""
        self.setup_2d()

        # Título
        self.draw_text("🗡️ ELIGE TU DESTINO ⚔️",
                       self.width // 2, 150,
                       self.font_large, Colors.GOLD, center=True)

        self.draw_text("Selecciona tu clase de aventurero:",
                       self.width // 2, 220,
                       self.font_medium, Colors.WHITE, center=True)

        # Opciones
        self.draw_text("1 - 🧙‍♂️ ARCHIMAGO SUPREMO",
                       self.width // 2, 320,
                       self.font_medium, Colors.PURPLE, center=True)

        self.draw_text("Maestro de las artes arcanas elementales",
                       self.width // 2, 350,
                       self.font_small, Colors.CYAN, center=True)

        self.draw_text("2 - ⚔️ PALADÍN INVENCIBLE",
                       self.width // 2, 420,
                       self.font_medium, Colors.BLUE, center=True)

        self.draw_text("Guerrero sagrado de honor inquebrantable",
                       self.width // 2, 450,
                       self.font_small, Colors.SILVER, center=True)

        # Controles
        self.draw_text("Presiona 1 o 2 para seleccionar",
                       self.width // 2, self.height - 50,
                       self.font_small, Colors.GOLD, center=True)

        self.restore_3d()

    def render_enemy_select(self, defeated_enemies):
        """Renderizar pantalla de selección de enemigo"""
        self.setup_2d()

        # Título
        self.draw_text("⚔️ ELIGE TU DESAFÍO ⚔️",
                       self.width // 2, 150,
                       self.font_large, Colors.GOLD, center=True)

        # Enemigos disponibles
        y_offset = 280

        self.draw_text("1 - 🧌 DUENDE SINIESTRO",
                       self.width // 2, y_offset,
                       self.font_medium, Colors.GREEN, center=True)
        self.draw_text("Ágil asesino de las sombras",
                       self.width // 2, y_offset + 25,
                       self.font_small, Colors.LIME, center=True)

        y_offset += 80
        self.draw_text("2 - 👹 OGRO DEVASTADOR",
                       self.width // 2, y_offset,
                       self.font_medium, Colors.ORANGE, center=True)
        self.draw_text("Coloso destructivo de montaña",
                       self.width // 2, y_offset + 25,
                       self.font_small, Colors.RED, center=True)

        # Dragón (si está disponible)
        if len(defeated_enemies) >= 2:
            y_offset += 80
            self.draw_text("3 - 🐉 DRAGÓN SOMBRÍO",
                           self.width // 2, y_offset,
                           self.font_medium, Colors.PURPLE, center=True)
            self.draw_text("Señor ancestral del fuego eterno",
                           self.width // 2, y_offset + 25,
                           self.font_small, Colors.MAGENTA, center=True)

        self.restore_3d()

    def render_combat(self, player_data, enemy_data, is_player_turn,
                      animation_in_progress, combat_log, show_inventory, show_controls):
        """Renderizar UI de combate"""
        self.setup_2d()

        # Panel del jugador (izquierda)
        self.draw_player_panel(player_data)

        # Panel del enemigo (derecha)
        self.draw_enemy_panel(enemy_data)

        # Acciones (centro abajo)
        if is_player_turn and not animation_in_progress:
            self.draw_action_buttons(player_data)

        # Log de combate
        self.draw_combat_log(combat_log)

        # Controles (si está habilitado)
        if show_controls:
            self.draw_controls()

        # Inventario (si está habilitado)
        if show_inventory:
            self.draw_inventory(player_data)

        self.restore_3d()

    def draw_player_panel(self, player_data):
        """Dibujar panel del jugador"""
        x, y = 20, 20
        panel_width = 300

        # Fondo del panel
        self.draw_rect(x, y, panel_width, 200, (0, 0, 0, 180))

        # Nombre y nivel
        self.draw_text(f"{player_data.name}", x + 10, y + 10,
                       self.font_medium, Colors.GOLD)
        self.draw_text(f"Nivel {player_data.level}", x + 10, y + 40,
                       self.font_small, Colors.WHITE)

        # Vida
        self.draw_text(f"❤️ Vida: {player_data.hp}/{player_data.max_hp}",
                       x + 10, y + 70, self.font_small, Colors.RED)
        self.draw_health_bar(x + 10, y + 90, 280, 20,
                             player_data.hp, player_data.max_hp, Colors.RED)

        # Maná
        self.draw_text(f"🔮 Maná: {player_data.mp}/{player_data.max_mp}",
                       x + 10, y + 120, self.font_small, Colors.BLUE)
        self.draw_health_bar(x + 10, y + 140, 280, 15,
                             player_data.mp, player_data.max_mp, Colors.BLUE)

        # XP
        self.draw_text(f"⭐ XP: {player_data.xp}/100",
                       x + 10, y + 170, self.font_small, Colors.GOLD)

    def draw_enemy_panel(self, enemy_data):
        """Dibujar panel del enemigo"""
        x = self.width - 320
        y = 20
        panel_width = 300

        # Fondo del panel
        self.draw_rect(x, y, panel_width, 150, (0, 0, 0, 180))

        # Nombre
        self.draw_text(f"{enemy_data.name}", x + 10, y + 10,
                       self.font_medium, Colors.RED)
        self.draw_text(f"Nivel {enemy_data.level}", x + 10, y + 40,
                       self.font_small, Colors.WHITE)

        # Vida
        self.draw_text(f"❤️ Vida: {enemy_data.hp}/{enemy_data.max_hp}",
                       x + 10, y + 70, self.font_small, Colors.RED)
        self.draw_health_bar(x + 10, y + 90, 280, 25,
                             enemy_data.hp, enemy_data.max_hp, Colors.RED)

    def draw_action_buttons(self, player_data):
        """Dibujar botones de acción"""
        center_x = self.width // 2
        y = self.height - 150

        self.draw_text("🎮 ACCIONES DE COMBATE", center_x, y - 30,
                       self.font_medium, Colors.GOLD, center=True)

        # Botones
        actions = [
            ("1 - ⚔️ Atacar", Colors.RED),
            ("3 - 🛡️ Defender", Colors.BLUE),
            ("4 - ❤️ Curar", Colors.GREEN),
            ("5 - 🧪 Poción", Colors.PURPLE)
        ]

        if player_data.class_type == "mago":
            actions.insert(1, ("2 - 🔮 Hechizo", Colors.CYAN))

        button_width = 180
        total_width = len(actions) * button_width
        start_x = center_x - total_width // 2

        for i, (text, color) in enumerate(actions):
            x = start_x + i * button_width
            self.draw_text(text, x, y, self.font_small, color, center=True)

    def draw_combat_log(self, combat_log):
        """Dibujar log de combate"""
        x = 20
        y = self.height - 200
        width = self.width - 40
        height = 150

        # Fondo
        self.draw_rect(x, y, width, height, (0, 0, 0, 200))

        # Título
        self.draw_text("📜 LOG DE COMBATE", x + 10, y + 5,
                       self.font_small, Colors.GOLD)

        # Mensajes (últimos 6)
        recent_log = combat_log[-6:] if len(combat_log) > 6 else combat_log
        for i, message in enumerate(recent_log):
            self.draw_text(message, x + 10, y + 30 + i * 20,
                           self.font_small, Colors.WHITE)

    def draw_controls(self):
        """Dibujar controles"""
        x, y = 20, self.height // 2

        self.draw_rect(x, y, 250, 120, (0, 0, 0, 180))
        self.draw_text("🎮 CONTROLES", x + 10, y + 10,
                       self.font_small, Colors.GOLD)
        self.draw_text("1-4: Acciones", x + 10, y + 35,
                       self.font_small, Colors.WHITE)
        self.draw_text("ESC: Pausar", x + 10, y + 55,
                       self.font_small, Colors.WHITE)
        self.draw_text("I: Inventario", x + 10, y + 75,
                       self.font_small, Colors.WHITE)
        self.draw_text("H: Ocultar/Mostrar", x + 10, y + 95,
                       self.font_small, Colors.WHITE)

    def draw_inventory(self, player_data):
        """Dibujar inventario"""
        x = self.width - 320
        y = 200

        self.draw_rect(x, y, 300, 250, (0, 0, 0, 180))
        self.draw_text("🎒 INVENTARIO", x + 10, y + 10,
                       self.font_small, Colors.GOLD)
        self.draw_text(f"💰 Oro: {player_data.gold}", x + 10, y + 35,
                       self.font_small, Colors.GOLD)

        # Arma equipada
        if player_data.equipped_weapon:
            self.draw_text(f"⚔️ {player_data.equipped_weapon['name']}",
                           x + 10, y + 60, self.font_small, Colors.GREEN)

        # Objetos (primeros 8)
        items_shown = player_data.inventory[:8]
        for i, item in enumerate(items_shown):
            item_y = y + 85 + i * 20
            self.draw_text(f"• {item.get('name', 'Objeto')}",
                           x + 10, item_y, self.font_small, Colors.WHITE)

    def render_victory(self):
        """Renderizar pantalla de victoria"""
        self.setup_2d()

        # Fondo semi-transparente
        self.draw_rect(0, 0, self.width, self.height, (0, 0, 0, 150))

        # Mensaje principal
        self.draw_text("🏆 ¡VICTORIA ÉPICA! 🏆",
                       self.width // 2, self.height // 2 - 50,
                       self.font_large, Colors.GOLD, center=True)

        self.draw_text("¡Has derrotado a tu enemigo!",
                       self.width // 2, self.height // 2,
                       self.font_medium, Colors.WHITE, center=True)

        self.draw_text("ENTER - Continuar aventura",
                       self.width // 2, self.height // 2 + 100,
                       self.font_medium, Colors.GREEN, center=True)

        self.restore_3d()

    def render_defeat(self):
        """Renderizar pantalla de derrota"""
        self.setup_2d()

        # Fondo rojo semi-transparente
        self.draw_rect(0, 0, self.width, self.height, (100, 0, 0, 150))

        # Mensaje principal
        self.draw_text("💀 DERROTA HEROICA 💀",
                       self.width // 2, self.height // 2 - 50,
                       self.font_large, Colors.RED, center=True)

        self.draw_text("Has caído en batalla...",
                       self.width // 2, self.height // 2,
                       self.font_medium, Colors.WHITE, center=True)

        self.draw_text("¡Pero un héroe siempre renace más fuerte!",
                       self.width // 2, self.height // 2 + 30,
                       self.font_small, Colors.GOLD, center=True)

        self.draw_text("ENTER - Renacer como héroe",
                       self.width // 2, self.height // 2 + 100,
                       self.font_medium, Colors.BLUE, center=True)

        self.restore_3d()

    def render_final_screen(self, player_data):
        """Renderizar pantalla final"""
        self.setup_2d()

        # Fondo dorado
        self.draw_rect(0, 0, self.width, self.height, (50, 50, 0, 200))

        # Mensaje principal
        self.draw_text("👑 ¡LEYENDA COMPLETADA! 👑",
                       self.width // 2, 150,
                       self.font_large, Colors.GOLD, center=True)

        self.draw_text("¡Te has convertido en una verdadera leyenda!",
                       self.width // 2, 220,
                       self.font_medium, Colors.WHITE, center=True)

        # Estadísticas finales
        stats_y = 300
        stats = [
            f"🏆 Victorias: {player_data.total_victories}",
            f"⭐ Nivel final: {player_data.level}",
            f"💰 Oro acumulado: {player_data.gold}",
            f"🔥 Mejor racha: {player_data.win_streak}"
        ]

        for i, stat in enumerate(stats):
            self.draw_text(stat, self.width // 2, stats_y + i * 40,
                           self.font_medium, Colors.GOLD, center=True)

        self.draw_text("ENTER - Nueva leyenda",
                       self.width // 2, self.height - 100,
                       self.font_medium, Colors.GREEN, center=True)

        self.restore_3d()

    # ============================================================================
    # UTILIDADES DE DIBUJO
    # ============================================================================

    def setup_2d(self):
        """Configurar modo 2D para UI"""
        glMatrixMode(GL_PROJECTION)
        glPushMatrix()
        glLoadIdentity()
        glOrtho(0, self.width, self.height, 0, -1, 1)

        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glLoadIdentity()

        glDisable(GL_DEPTH_TEST)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    def restore_3d(self):
        """Restaurar modo 3D"""
        glDisable(GL_BLEND)
        glEnable(GL_DEPTH_TEST)

        glMatrixMode(GL_PROJECTION)
        glPopMatrix()
        glMatrixMode(GL_MODELVIEW)
        glPopMatrix()

    def draw_text(self, text, x, y, font, color, center=False):
        """Dibujar texto en pantalla"""
        # Por simplicidad, usar print por ahora
        # En una implementación completa usarías texturas de texto
        pass

    def draw_rect(self, x, y, width, height, color):
        """Dibujar rectángulo"""
        glColor4f(color[0]/255.0, color[1]/255.0, color[2]/255.0,
                  color[3]/255.0 if len(color) > 3 else 1.0)

        glBegin(GL_QUADS)
        glVertex2f(x, y)
        glVertex2f(x + width, y)
        glVertex2f(x + width, y + height)
        glVertex2f(x, y + height)
        glEnd()

    def draw_health_bar(self, x, y, width, height, current, max_val, color):
        """Dibujar barra de vida/maná"""
        # Fondo
        self.draw_rect(x, y, width, height, (50, 50, 50, 255))

        # Barra
        if max_val > 0:
            fill_width = (current / max_val) * width
            self.draw_rect(x, y, fill_width, height, color)