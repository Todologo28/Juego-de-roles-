"""
Modelos 3D épicos de los enemigos - Versión Completa
"""

import math
import random
from OpenGL.GL import *
from OpenGL.GLU import *
from models.player_models import Character3D

class EnemyModel(Character3D):
    """Modelo base para enemigos"""

    def __init__(self, renderer, enemy_type):
        super().__init__(renderer)
        self.position = [4, 0, 0]
        self.enemy_type = enemy_type
        self.menace_factor = 0
        self.threat_aura = 0

    def draw(self, time):
        """Dibujar enemigo según su tipo"""
        glPushMatrix()

        # Aplicar transformaciones
        glTranslatef(*self.position)
        glRotatef(self.rotation[1], 0, 1, 0)
        glScalef(*self.scale)

        # Actualizar animaciones
        self.menace_factor += 0.03
        self.threat_aura += 1.2

        # Dibujar según tipo
        if self.enemy_type == "duende":
            self.draw_goblin(time)
        elif self.enemy_type == "ogro":
            self.draw_ogre(time)
        elif self.enemy_type == "dragon":
            self.draw_dragon(time)

        # Aura amenazante
        self.draw_enemy_aura(time)

        glPopMatrix()

    def draw_goblin(self, time):
        """Dibujar Duende Siniestro"""
        # Cuerpo ágil del duende
        glPushMatrix()
        glTranslatef(0, 1.4, 0)

        # Material del duende
        self.renderer.set_material(
            [0.05, 0.2, 0.05, 1.0],  # Verde oscuro
            [0.13, 0.55, 0.13, 1.0], # Verde
            [0.3, 0.8, 0.3, 1.0],    # Verde brillante
            [40.0]
        )

        glColor3f(0.13, 0.55, 0.13)
        self.renderer.draw_cylinder(0.7, 2.4, 12)

        # Armadura improvisada
        glColor3f(0.4, 0.26, 0.13)
        self.renderer.draw_cylinder(0.75, 1.8, 12)

        glPopMatrix()

        # Cabeza siniestra
        glPushMatrix()
        glTranslatef(0, 3.2, 0)

        # Cabeza principal
        glColor3f(0.2, 0.8, 0.2)
        self.renderer.draw_sphere(0.6, (0.2, 0.8, 0.2), 16, 12)

        # Ojos rojos malvados
        eye_glow = 0.8 + math.sin(time * 5) * 0.2

        glPushMatrix()
        glTranslatef(-0.18, 0.1, 0.5)
        glColor3f(1.0 * eye_glow, 0, 0)
        self.renderer.draw_sphere(0.1, (1.0, 0, 0), 8, 6)
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0.18, 0.1, 0.5)
        glColor3f(1.0 * eye_glow, 0, 0)
        self.renderer.draw_sphere(0.1, (1.0, 0, 0), 8, 6)
        glPopMatrix()

        # Nariz ganchuda
        glPushMatrix()
        glTranslatef(0, 0, 0.55)
        glRotatef(90, 1, 0, 0)
        glColor3f(0.13, 0.55, 0.13)
        self.renderer.draw_cone(0.08, 0.3, 8)
        glPopMatrix()

        # Dientes afilados
        glColor3f(1.0, 1.0, 0.9)
        for i in range(6):
            glPushMatrix()
            glTranslatef(-0.2 + i * 0.08, -0.2, 0.5)
            glRotatef(180, 1, 0, 0)
            self.renderer.draw_cone(0.02, 0.15, 6)
            glPopMatrix()

        glPopMatrix()

        # Orejas puntiagudas grandes
        ear_sway = math.sin(self.menace_factor * 2) * 5

        glPushMatrix()
        glTranslatef(-0.6, 3.5, 0)
        glRotatef(-60 + ear_sway, 0, 0, 1)
        glColor3f(0.2, 0.8, 0.2)
        self.renderer.draw_cone(0.2, 0.8, 8)
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0.6, 3.5, 0)
        glRotatef(60 - ear_sway, 0, 0, 1)
        glColor3f(0.2, 0.8, 0.2)
        self.renderer.draw_cone(0.2, 0.8, 8)
        glPopMatrix()

        # Brazos ágiles
        self.draw_goblin_arms(time)

        # Dagas gemelas
        self.draw_goblin_weapons(time)

        # Piernas arqueadas
        self.draw_goblin_legs()

    def draw_goblin_arms(self, time):
        """Dibujar brazos del duende"""
        arm_swing = math.sin(time * 3) * 10

        # Brazo izquierdo
        glPushMatrix()
        glTranslatef(-1, 2.2, 0)
        glRotatef(30 + arm_swing, 0, 0, 1)

        glColor3f(0.2, 0.8, 0.2)
        self.renderer.draw_cylinder(0.15, 1.4, 8)

        # Antebrazo
        glTranslatef(0, -1.0, 0)
        glRotatef(20, 0, 0, 1)
        self.renderer.draw_cylinder(0.12, 1.2, 8)

        # Mano garra
        glTranslatef(0, -0.8, 0)
        self.renderer.draw_sphere(0.18, (0.15, 0.6, 0.15), 8, 6)

        # Garras
        glColor3f(0.8, 0.8, 0.8)
        for i in range(4):
            glPushMatrix()
            glRotatef(i * 20 - 30, 0, 1, 0)
            glTranslatef(0, 0, 0.15)
            self.renderer.draw_cone(0.02, 0.2, 6)
            glPopMatrix()

        glPopMatrix()

        # Brazo derecho (similar)
        glPushMatrix()
        glTranslatef(1, 2.2, 0)
        glRotatef(-30 - arm_swing, 0, 0, 1)

        glColor3f(0.2, 0.8, 0.2)
        self.renderer.draw_cylinder(0.15, 1.4, 8)

        glTranslatef(0, -1.0, 0)
        glRotatef(-20, 0, 0, 1)
        self.renderer.draw_cylinder(0.12, 1.2, 8)

        glTranslatef(0, -0.8, 0)
        self.renderer.draw_sphere(0.18, (0.15, 0.6, 0.15), 8, 6)

        glColor3f(0.8, 0.8, 0.8)
        for i in range(4):
            glPushMatrix()
            glRotatef(i * 20 - 30, 0, 1, 0)
            glTranslatef(0, 0, 0.15)
            self.renderer.draw_cone(0.02, 0.2, 6)
            glPopMatrix()

        glPopMatrix()

    def draw_goblin_weapons(self, time):
        """Dibujar dagas del duende"""
        weapon_gleam = 0.8 + math.sin(time * 4) * 0.2

        # Daga izquierda
        glPushMatrix()
        glTranslatef(1.4, 1.8, 0)
        glRotatef(-30, 0, 0, 1)

        # Mango
        glColor3f(0.4, 0.26, 0.13)
        self.renderer.draw_cylinder(0.05, 0.4, 8)

        # Hoja
        glTranslatef(0, 0.5, 0)
        glColor3f(0.7 * weapon_gleam, 0.7 * weapon_gleam, 0.8 * weapon_gleam)
        self.renderer.draw_cone(0.08, 0.8, 6)

        glPopMatrix()

        # Daga derecha
        glPushMatrix()
        glTranslatef(-1.4, 1.8, 0)
        glRotatef(30, 0, 0, 1)

        glColor3f(0.4, 0.26, 0.13)
        self.renderer.draw_cylinder(0.05, 0.4, 8)

        glTranslatef(0, 0.5, 0)
        glColor3f(0.7 * weapon_gleam, 0.7 * weapon_gleam, 0.8 * weapon_gleam)
        self.renderer.draw_cone(0.08, 0.8, 6)

        glPopMatrix()

    def draw_goblin_legs(self):
        """Dibujar piernas arqueadas del duende"""
        # Pierna izquierda
        glPushMatrix()
        glTranslatef(-0.4, 0.2, 0)
        glRotatef(10, 0, 0, 1)  # Ligeramente arqueada

        # Muslo
        glColor3f(0.2, 0.8, 0.2)
        self.renderer.draw_cylinder(0.2, 1.2, 8)

        # Rodilla
        glTranslatef(0, -1.0, 0)
        glRotatef(-20, 1, 0, 0)  # Curvatura hacia atrás

        # Pantorrilla
        self.renderer.draw_cylinder(0.18, 1.0, 8)

        # Pie grande
        glTranslatef(0, -0.8, 0.3)
        glColor3f(0.15, 0.6, 0.15)
        self.renderer.draw_sphere(0.25, (0.15, 0.6, 0.15), 8, 6)

        # Dedos del pie
        glColor3f(0.8, 0.8, 0.8)
        for i in range(3):
            glPushMatrix()
            glTranslatef(-0.1 + i * 0.1, 0, 0.2)
            self.renderer.draw_cone(0.03, 0.15, 6)
            glPopMatrix()

        glPopMatrix()

        # Pierna derecha
        glPushMatrix()
        glTranslatef(0.4, 0.2, 0)
        glRotatef(-10, 0, 0, 1)  # Arqueada al otro lado

        glColor3f(0.2, 0.8, 0.2)
        self.renderer.draw_cylinder(0.2, 1.2, 8)

        glTranslatef(0, -1.0, 0)
        glRotatef(-20, 1, 0, 0)

        self.renderer.draw_cylinder(0.18, 1.0, 8)

        glTranslatef(0, -0.8, 0.3)
        glColor3f(0.15, 0.6, 0.15)
        self.renderer.draw_sphere(0.25, (0.15, 0.6, 0.15), 8, 6)

        glColor3f(0.8, 0.8, 0.8)
        for i in range(3):
            glPushMatrix()
            glTranslatef(-0.1 + i * 0.1, 0, 0.2)
            self.renderer.draw_cone(0.03, 0.15, 6)
            glPopMatrix()

        glPopMatrix()

    def draw_ogre(self, time):
        """Dibujar Ogro Brutal"""
        # Cuerpo masivo
        glPushMatrix()
        glTranslatef(0, 2.5, 0)

        # Material del ogro
        self.renderer.set_material(
            [0.3, 0.15, 0.05, 1.0],  # Marrón oscuro
            [0.6, 0.3, 0.1, 1.0],    # Marrón
            [0.8, 0.4, 0.2, 1.0],    # Marrón brillante
            [20.0]
        )

        # Torso enorme
        glColor3f(0.6, 0.3, 0.1)
        self.renderer.draw_cylinder(1.5, 4.0, 16)

        # Vientre prominente
        glPushMatrix()
        glTranslatef(0, -1, 0.8)
        glScalef(1.2, 0.8, 1.0)
        self.renderer.draw_sphere(1.0, (0.5, 0.25, 0.08), 12, 8)
        glPopMatrix()

        glPopMatrix()

        # Cabeza brutal
        glPushMatrix()
        glTranslatef(0, 5.8, 0)

        # Cabeza principal
        glColor3f(0.5, 0.25, 0.08)
        self.renderer.draw_sphere(1.0, (0.5, 0.25, 0.08), 16, 12)

        # Ojos pequeños y crueles
        eye_flicker = 0.6 + math.sin(time * 2) * 0.1

        glPushMatrix()
        glTranslatef(-0.3, 0.2, 0.8)
        glColor3f(1.0 * eye_flicker, 0.2, 0)
        self.renderer.draw_sphere(0.12, (1.0, 0.2, 0), 8, 6)
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0.3, 0.2, 0.8)
        glColor3f(1.0 * eye_flicker, 0.2, 0)
        self.renderer.draw_sphere(0.12, (1.0, 0.2, 0), 8, 6)
        glPopMatrix()

        # Boca enorme con colmillos
        glPushMatrix()
        glTranslatef(0, -0.3, 0.7)
        glColor3f(0.2, 0.1, 0.05)
        self.renderer.draw_sphere(0.4, (0.2, 0.1, 0.05), 12, 8)

        # Colmillos gigantes
        glColor3f(1.0, 1.0, 0.8)
        glPushMatrix()
        glTranslatef(-0.2, 0.1, 0.3)
        glRotatef(180, 1, 0, 0)
        self.renderer.draw_cone(0.08, 0.6, 8)
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0.2, 0.1, 0.3)
        glRotatef(180, 1, 0, 0)
        self.renderer.draw_cone(0.08, 0.6, 8)
        glPopMatrix()

        glPopMatrix()

        glPopMatrix()

        # Brazos musculosos
        self.draw_ogre_arms(time)

        # Garrote devastador
        self.draw_ogre_weapon(time)

        # Piernas como troncos
        self.draw_ogre_legs()

    def draw_ogre_arms(self, time):
        """Dibujar brazos musculosos del ogro"""
        muscle_flex = math.sin(time * 1.5) * 0.1 + 1.0

        # Brazo izquierdo
        glPushMatrix()
        glTranslatef(-2.0, 4.0, 0)
        glRotatef(20, 0, 0, 1)

        # Hombro
        glColor3f(0.6, 0.3, 0.1)
        self.renderer.draw_sphere(0.6, (0.6, 0.3, 0.1), 12, 8)

        # Brazo superior
        glTranslatef(0, -1.2, 0)
        glScalef(muscle_flex, 1.0, muscle_flex)
        self.renderer.draw_cylinder(0.4, 2.0, 12)

        # Antebrazo
        glTranslatef(0, -1.8, 0)
        glRotatef(15, 1, 0, 0)
        glScalef(1.0/muscle_flex, 1.0, 1.0/muscle_flex)
        self.renderer.draw_cylinder(0.35, 1.8, 12)

        # Puño enorme
        glTranslatef(0, -1.5, 0)
        glColor3f(0.5, 0.25, 0.08)
        self.renderer.draw_sphere(0.5, (0.5, 0.25, 0.08), 10, 8)

        # Nudillos
        glColor3f(0.4, 0.2, 0.06)
        for i in range(4):
            glPushMatrix()
            glRotatef(i * 20 - 30, 0, 1, 0)
            glTranslatef(0, 0, 0.4)
            self.renderer.draw_sphere(0.1, (0.4, 0.2, 0.06), 6, 4)
            glPopMatrix()

        glPopMatrix()

        # Brazo derecho (sostiene el garrote)
        glPushMatrix()
        glTranslatef(2.0, 4.0, 0)
        glRotatef(-20, 0, 0, 1)
        glRotatef(45, 1, 0, 0)  # Levantado para el garrote

        glColor3f(0.6, 0.3, 0.1)
        self.renderer.draw_sphere(0.6, (0.6, 0.3, 0.1), 12, 8)

        glTranslatef(0, -1.2, 0)
        glScalef(muscle_flex, 1.0, muscle_flex)
        self.renderer.draw_cylinder(0.4, 2.0, 12)

        glTranslatef(0, -1.8, 0)
        glRotatef(-15, 1, 0, 0)
        glScalef(1.0/muscle_flex, 1.0, 1.0/muscle_flex)
        self.renderer.draw_cylinder(0.35, 1.8, 12)

        glTranslatef(0, -1.5, 0)
        glColor3f(0.5, 0.25, 0.08)
        self.renderer.draw_sphere(0.5, (0.5, 0.25, 0.08), 10, 8)

        glPopMatrix()

    def draw_ogre_weapon(self, time):
        """Dibujar garrote del ogro"""
        weapon_sway = math.sin(time * 0.8) * 15

        glPushMatrix()
        glTranslatef(2.5, 2.5, 0)
        glRotatef(45 + weapon_sway, 1, 0, 0)
        glRotatef(-30, 0, 0, 1)

        # Mango del garrote
        glColor3f(0.4, 0.26, 0.13)
        self.renderer.draw_cylinder(0.15, 3.0, 12)

        # Cabeza del garrote
        glTranslatef(0, 3.2, 0)
        glColor3f(0.3, 0.15, 0.08)
        self.renderer.draw_sphere(0.8, (0.3, 0.15, 0.08), 12, 8)

        # Clavos amenazantes
        glColor3f(0.6, 0.6, 0.6)
        for i in range(8):
            glPushMatrix()
            glRotatef(i * 45, 0, 1, 0)
            glTranslatef(0, 0, 0.7)
            self.renderer.draw_cone(0.05, 0.3, 6)
            glPopMatrix()

        glPopMatrix()

    def draw_ogre_legs(self):
        """Dibujar piernas como troncos del ogro"""
        # Pierna izquierda
        glPushMatrix()
        glTranslatef(-0.8, 0.5, 0)

        # Muslo
        glColor3f(0.6, 0.3, 0.1)
        self.renderer.draw_cylinder(0.6, 2.5, 12)

        # Rodilla
        glTranslatef(0, -2.2, 0)
        self.renderer.draw_sphere(0.7, (0.5, 0.25, 0.08), 10, 8)

        # Pantorrilla
        glTranslatef(0, -0.8, 0)
        self.renderer.draw_cylinder(0.5, 2.0, 12)

        # Pie enorme
        glTranslatef(0, -1.8, 0.5)
        glColor3f(0.5, 0.25, 0.08)
        glScalef(1.5, 0.6, 2.0)
        self.renderer.draw_sphere(0.4, (0.5, 0.25, 0.08), 8, 6)

        glPopMatrix()

        # Pierna derecha
        glPushMatrix()
        glTranslatef(0.8, 0.5, 0)

        glColor3f(0.6, 0.3, 0.1)
        self.renderer.draw_cylinder(0.6, 2.5, 12)

        glTranslatef(0, -2.2, 0)
        self.renderer.draw_sphere(0.7, (0.5, 0.25, 0.08), 10, 8)

        glTranslatef(0, -0.8, 0)
        self.renderer.draw_cylinder(0.5, 2.0, 12)

        glTranslatef(0, -1.8, 0.5)
        glColor3f(0.5, 0.25, 0.08)
        glScalef(1.5, 0.6, 2.0)
        self.renderer.draw_sphere(0.4, (0.5, 0.25, 0.08), 8, 6)

        glPopMatrix()

    def draw_dragon(self, time):
        """Dibujar Dragón Ancestral"""
        # Cuerpo serpentino
        glPushMatrix()
        glTranslatef(0, 3.0, 0)

        # Material del dragón
        self.renderer.set_material(
            [0.1, 0.0, 0.1, 1.0],    # Púrpura oscuro
            [0.4, 0.1, 0.2, 1.0],    # Rojo oscuro
            [0.8, 0.2, 0.4, 1.0],    # Rojo brillante
            [80.0]
        )

        # Cuerpo principal
        body_undulation = math.sin(time * 2) * 0.3
        glRotatef(body_undulation * 10, 0, 0, 1)

        glColor3f(0.4, 0.1, 0.2)
        self.renderer.draw_cylinder(1.2, 5.0, 16)

        # Escamas brillantes
        glColor3f(0.6, 0.15, 0.3)
        for i in range(20):
            glPushMatrix()
            glRotatef(i * 18, 0, 1, 0)
            glTranslatef(0, -2 + (i % 4) * 1, 1.1)
            glScalef(0.3, 0.1, 0.2)
            self.renderer.draw_sphere(0.2, (0.6, 0.15, 0.3), 6, 4)
            glPopMatrix()

        glPopMatrix()

        # Cabeza de dragón
        glPushMatrix()
        glTranslatef(0, 6.5, 0)

        # Cabeza principal
        glColor3f(0.5, 0.12, 0.25)
        glScalef(1.0, 1.5, 2.0)
        self.renderer.draw_sphere(0.8, (0.5, 0.12, 0.25), 16, 12)
        glScalef(1.0, 1.0/1.5, 1.0/2.0)

        # Ojos de fuego
        fire_intensity = 0.8 + math.sin(time * 6) * 0.2

        glPushMatrix()
        glTranslatef(-0.25, 0.2, 1.3)
        glColor3f(1.0 * fire_intensity, 0.5 * fire_intensity, 0)
        self.renderer.draw_sphere(0.15, (1.0, 0.5, 0), 8, 6)
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0.25, 0.2, 1.3)
        glColor3f(1.0 * fire_intensity, 0.5 * fire_intensity, 0)
        self.renderer.draw_sphere(0.15, (1.0, 0.5, 0), 8, 6)
        glPopMatrix()

        # Hocico
        glPushMatrix()
        glTranslatef(0, -0.3, 1.4)
        glColor3f(0.4, 0.08, 0.2)
        glScalef(0.6, 0.4, 1.2)
        self.renderer.draw_sphere(0.5, (0.4, 0.08, 0.2), 12, 8)
        glPopMatrix()

        # Cuernos majestuosos
        horn_curve = math.sin(time * 1.5) * 2

        glPushMatrix()
        glTranslatef(-0.4, 0.8, 0.5)
        glRotatef(-30 + horn_curve, 0, 0, 1)
        glColor3f(0.8, 0.8, 0.7)
        self.renderer.draw_cone(0.12, 1.5, 8)
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0.4, 0.8, 0.5)
        glRotatef(30 - horn_curve, 0, 0, 1)
        glColor3f(0.8, 0.8, 0.7)
        self.renderer.draw_cone(0.12, 1.5, 8)
        glPopMatrix()

        # Dientes afilados
        glColor3f(1.0, 1.0, 0.9)
        for i in range(8):
            glPushMatrix()
            glTranslatef(-0.3 + i * 0.1, -0.6, 1.8)
            glRotatef(180, 1, 0, 0)
            self.renderer.draw_cone(0.03, 0.25, 6)
            glPopMatrix()

        glPopMatrix()

        # Alas poderosas
        self.draw_dragon_wings(time)

        # Cola serpentina
        self.draw_dragon_tail(time)

        # Piernas de dragón
        self.draw_dragon_legs()

    def draw_dragon_wings(self, time):
        """Dibujar alas del dragón"""
        wing_flap = math.sin(time * 3) * 15
        wing_spread = 20 + math.cos(time * 2) * 5

        # Ala izquierda
        glPushMatrix()
        glTranslatef(-1.5, 4.5, -0.5)
        glRotatef(-wing_spread - wing_flap, 0, 0, 1)

        # Hueso del ala
        glColor3f(0.3, 0.2, 0.15)
        self.renderer.draw_cylinder(0.08, 2.5, 8)

        # Membrana del ala
        glColor3f(0.2, 0.05, 0.1)
        for i in range(3):
            glPushMatrix()
            glRotatef(i * 25 - 25, 0, 1, 0)
            glTranslatef(0, -1.2, 0)
            glScalef(0.1, 2.0, 1.5)
            self.renderer.draw_sphere(1.0, (0.2, 0.05, 0.1), 8, 6)
            glPopMatrix()

        glPopMatrix()

        # Ala derecha
        glPushMatrix()
        glTranslatef(1.5, 4.5, -0.5)
        glRotatef(wing_spread + wing_flap, 0, 0, 1)

        glColor3f(0.3, 0.2, 0.15)
        self.renderer.draw_cylinder(0.08, 2.5, 8)

        glColor3f(0.2, 0.05, 0.1)
        for i in range(3):
            glPushMatrix()
            glRotatef(i * 25 - 25, 0, 1, 0)
            glTranslatef(0, -1.2, 0)
            glScalef(0.1, 2.0, 1.5)
            self.renderer.draw_sphere(1.0, (0.2, 0.05, 0.1), 8, 6)
            glPopMatrix()

        glPopMatrix()

    def draw_dragon_tail(self, time):
        """Dibujar cola serpentina del dragón"""
        # Segmentos de la cola
        tail_segments = 8
        for i in range(tail_segments):
            glPushMatrix()

            # Posición y curvatura de cada segmento
            segment_pos = i * 0.8
            tail_sway = math.sin(time * 2 + i * 0.5) * (0.3 + i * 0.1)

            glTranslatef(tail_sway, 0.5 - segment_pos, -1.5 - i * 0.3)
            glRotatef(tail_sway * 20, 0, 1, 0)

            # Tamaño decreciente
            scale = 1.0 - (i * 0.1)
            glScalef(scale, scale, scale)

            glColor3f(0.4 - i * 0.02, 0.1, 0.2 - i * 0.01)
            self.renderer.draw_cylinder(0.3, 0.8, 8)

            # Espinas en la cola
            if i < 5:
                glColor3f(0.6, 0.5, 0.4)
                glPushMatrix()
                glTranslatef(0, 0.4, 0)
                self.renderer.draw_cone(0.05, 0.3, 6)
                glPopMatrix()

            glPopMatrix()

        # Punta afilada de la cola
        glPushMatrix()
        glTranslatef(0, -5.5, -4.0)
        glColor3f(0.8, 0.8, 0.7)
        self.renderer.draw_cone(0.15, 0.8, 8)
        glPopMatrix()

    def draw_dragon_legs(self):
        """Dibujar piernas poderosas del dragón"""
        # Pierna izquierda
        glPushMatrix()
        glTranslatef(-1.0, 1.0, 0)

        # Muslo
        glColor3f(0.4, 0.1, 0.2)
        self.renderer.draw_cylinder(0.4, 2.0, 10)

        # Rodilla
        glTranslatef(0, -1.8, 0)
        glRotatef(-30, 1, 0, 0)

        # Pantorrilla
        self.renderer.draw_cylinder(0.3, 1.5, 10)

        # Garra de dragón
        glTranslatef(0, -1.2, 0.4)
        glColor3f(0.35, 0.08, 0.18)
        self.renderer.draw_sphere(0.4, (0.35, 0.08, 0.18), 8, 6)

        # Garras letales
        glColor3f(0.9, 0.9, 0.8)
        for i in range(4):
            glPushMatrix()
            glRotatef(i * 30 - 45, 0, 1, 0)
            glTranslatef(0, 0, 0.35)
            self.renderer.draw_cone(0.04, 0.4, 6)
            glPopMatrix()

        glPopMatrix()

        # Pierna derecha
        glPushMatrix()
        glTranslatef(1.0, 1.0, 0)

        glColor3f(0.4, 0.1, 0.2)
        self.renderer.draw_cylinder(0.4, 2.0, 10)

        glTranslatef(0, -1.8, 0)
        glRotatef(-30, 1, 0, 0)

        self.renderer.draw_cylinder(0.3, 1.5, 10)

        glTranslatef(0, -1.2, 0.4)
        glColor3f(0.35, 0.08, 0.18)
        self.renderer.draw_sphere(0.4, (0.35, 0.08, 0.18), 8, 6)

        glColor3f(0.9, 0.9, 0.8)
        for i in range(4):
            glPushMatrix()
            glRotatef(i * 30 - 45, 0, 1, 0)
            glTranslatef(0, 0, 0.35)
            self.renderer.draw_cone(0.04, 0.4, 6)
            glPopMatrix()

        glPopMatrix()

    def draw_enemy_aura(self, time):
        """Dibujar aura amenazante del enemigo"""
        # Habilitar transparencia
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        # Aura pulsante
        aura_pulse = 0.3 + math.sin(time * 4) * 0.2
        aura_size = 1.5 + math.cos(time * 2) * 0.3

        glPushMatrix()
        glTranslatef(0, 2.5, 0)
        glScalef(aura_size, aura_size * 0.5, aura_size)

        # Color del aura según el tipo de enemigo
        if self.enemy_type == "duende":
            glColor4f(0.2, 0.8, 0.2, aura_pulse * 0.3)
        elif self.enemy_type == "ogro":
            glColor4f(0.8, 0.4, 0.2, aura_pulse * 0.4)
        elif self.enemy_type == "dragon":
            glColor4f(0.8, 0.2, 0.4, aura_pulse * 0.5)

        # Dibujar aura como esfera translúcida
        self.renderer.draw_sphere(2.0, None, 16, 12)

        glPopMatrix()

        # Partículas de energía maligna
        self.draw_malevolent_particles(time)

        glDisable(GL_BLEND)

    def draw_malevolent_particles(self, time):
        """Dibujar partículas de energía maligna"""
        glColor4f(1.0, 0.3, 0.1, 0.6)

        for i in range(12):
            # Posición orbital de las partículas
            orbit_angle = (time * 50 + i * 30) % 360
            orbit_radius = 2.0 + math.sin(time * 3 + i) * 0.5
            particle_height = 1.0 + math.sin(time * 2 + i * 0.5) * 2.0

            x = math.cos(math.radians(orbit_angle)) * orbit_radius
            z = math.sin(math.radians(orbit_angle)) * orbit_radius
            y = particle_height

            glPushMatrix()
            glTranslatef(x, y, z)

            # Partículas pulsantes
            particle_size = 0.05 + math.sin(time * 6 + i) * 0.02
            self.renderer.draw_sphere(particle_size, None, 6, 4)

            glPopMatrix()

    def update_ai_behavior(self, player_pos, time):
        """Actualizar comportamiento de IA del enemigo"""
        # Calcular distancia al jugador
        dx = player_pos[0] - self.position[0]
        dz = player_pos[2] - self.position[2]
        distance = math.sqrt(dx*dx + dz*dz)

        # Comportamiento según tipo de enemigo
        if self.enemy_type == "duende":
            self.update_goblin_ai(dx, dz, distance, time)
        elif self.enemy_type == "ogro":
            self.update_ogre_ai(dx, dz, distance, time)
        elif self.enemy_type == "dragon":
            self.update_dragon_ai(dx, dz, distance, time)

    def update_goblin_ai(self, dx, dz, distance, time):
        """IA del duende: ágil y esquivo"""
        if distance < 8.0:  # Rango de detección
            if distance > 2.0:  # Acercarse sigilosamente
                move_speed = 0.02
                self.position[0] += (dx / distance) * move_speed
                self.position[2] += (dz / distance) * move_speed
            else:  # Esquivar y atacar
                dodge_angle = time * 3
                self.position[0] += math.cos(dodge_angle) * 0.03
                self.position[2] += math.sin(dodge_angle) * 0.03

            # Rotar hacia el jugador
            self.rotation[1] = math.degrees(math.atan2(dx, dz))

    def update_ogre_ai(self, dx, dz, distance, time):
        """IA del ogro: lento pero implacable"""
        if distance < 12.0:  # Mayor rango por su tamaño
            if distance > 3.0:  # Avanzar pesadamente
                move_speed = 0.015
                self.position[0] += (dx / distance) * move_speed
                self.position[2] += (dz / distance) * move_speed

            # Rotar lentamente hacia el jugador
            target_rotation = math.degrees(math.atan2(dx, dz))
            rotation_diff = target_rotation - self.rotation[1]
            self.rotation[1] += rotation_diff * 0.02

    def update_dragon_ai(self, dx, dz, distance, time):
        """IA del dragón: vuelo y ataques devastadores"""
        if distance < 15.0:  # Rango extenso
            # Vuelo circular
            circle_angle = time * 0.5
            circle_radius = 6.0

            target_x = math.cos(circle_angle) * circle_radius
            target_z = math.sin(circle_angle) * circle_radius

            # Movimiento suave hacia la posición objetivo
            self.position[0] += (target_x - self.position[0]) * 0.01
            self.position[2] += (target_z - self.position[2]) * 0.01

            # Altura fluctuante
            self.position[1] = 2.0 + math.sin(time * 2) * 1.0

            # Rotar hacia el jugador
            self.rotation[1] = math.degrees(math.atan2(dx, dz))

    def get_attack_damage(self):
        """Obtener daño de ataque según tipo de enemigo"""
        damage_values = {
            "duende": 15,
            "ogro": 35,
            "dragon": 60
        }
        return damage_values.get(self.enemy_type, 10)

    def get_health(self):
        """Obtener vida según tipo de enemigo"""
        health_values = {
            "duende": 80,
            "ogro": 200,
            "dragon": 400
        }
        return health_values.get(self.enemy_type, 50)

    def get_movement_speed(self):
        """Obtener velocidad de movimiento"""
        speed_values = {
            "duende": 0.8,
            "ogro": 0.3,
            "dragon": 0.6
        }
        return speed_values.get(self.enemy_type, 0.5)

# Clase especializada para crear diferentes tipos de enemigos
class EnemyFactory:
    """Fábrica para crear diferentes tipos de enemigos"""

    @staticmethod
    def create_enemy(renderer, enemy_type, position=None):
        """Crear un enemigo del tipo especificado"""
        enemy = EnemyModel(renderer, enemy_type)

        if position:
            enemy.position = list(position)

        # Configuraciones específicas por tipo
        if enemy_type == "duende":
            enemy.scale = [0.8, 0.8, 0.8]  # Más pequeño
        elif enemy_type == "ogro":
            enemy.scale = [1.2, 1.2, 1.2]  # Más grande
        elif enemy_type == "dragon":
            enemy.scale = [1.5, 1.5, 1.5]  # El más grande
            enemy.position[1] = 3.0  # Altura inicial para vuelo

        return enemy

    @staticmethod
    def create_enemy_squad(renderer, squad_type="mixed", count=5):
        """Crear un escuadrón de enemigos"""
        squad = []

        if squad_type == "goblin_pack":
            # Manada de duendes
            for i in range(count):
                angle = (i / count) * 360
                radius = 8 + random.uniform(-2, 2)
                x = math.cos(math.radians(angle)) * radius
                z = math.sin(math.radians(angle)) * radius

                enemy = EnemyFactory.create_enemy(renderer, "duende", [x, 0, z])
                squad.append(enemy)

        elif squad_type == "ogre_clan":
            # Clan de ogros
            for i in range(min(count, 3)):  # Máximo 3 ogros
                angle = (i / 3) * 120
                radius = 12
                x = math.cos(math.radians(angle)) * radius
                z = math.sin(math.radians(angle)) * radius

                enemy = EnemyFactory.create_enemy(renderer, "ogro", [x, 0, z])
                squad.append(enemy)

        elif squad_type == "dragon_solo":
            # Dragón solitario
            enemy = EnemyFactory.create_enemy(renderer, "dragon", [0, 3, 10])
            squad.append(enemy)

        elif squad_type == "mixed":
            # Escuadrón mixto
            types = ["duende", "duende", "ogro", "duende"]
            for i, enemy_type in enumerate(types[:count]):
                angle = (i / len(types)) * 360
                radius = 6 + (2 if enemy_type == "ogro" else 0)
                x = math.cos(math.radians(angle)) * radius
                z = math.sin(math.radians(angle)) * radius

                enemy = EnemyFactory.create_enemy(renderer, enemy_type, [x, 0, z])
                squad.append(enemy)

        return squad