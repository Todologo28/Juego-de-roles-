"""
Modelos 3D épicos de los personajes jugadores - VERSIÓN GRÁFICA COMPLETA
"""

import math
import random
from OpenGL.GL import *
from OpenGL.GLU import *

class Character3D:
    """Clase base para personajes 3D"""
    def __init__(self, renderer):
        self.renderer = renderer
        self.position = [-4, 0, 0]
        self.rotation = [0, 0, 0]
        self.scale = [1, 1, 1]
        self.animation_time = 0
        self.health_percent = 1.0
        self.is_attacking = False
        self.is_casting = False
        self.bob_offset = 0

    def update(self, dt):
        """Actualizar animación del personaje"""
        self.animation_time += dt
        self.bob_offset = 0.05 * math.sin(self.animation_time * 2)

    def set_attack_animation(self, attacking):
        """Activar/desactivar animación de ataque"""
        self.is_attacking = attacking

    def set_cast_animation(self, casting):
        """Activar/desactivar animación de hechizo"""
        self.is_casting = casting

class MageModel(Character3D):
    """Modelo 3D épico del Mago con efectos gráficos"""

    def __init__(self, renderer):
        super().__init__(renderer)
        self.staff_glow_intensity = 0
        self.orb_pulse = 0
        self.cape_sway = 0

    def draw(self, time):
        """Dibujar el modelo completo del mago"""
        glPushMatrix()

        # Aplicar transformaciones
        glTranslatef(self.position[0], self.position[1] + self.bob_offset, self.position[2])
        glRotatef(self.rotation[1], 0, 1, 0)
        glScalef(*self.scale)

        # Actualizar animaciones
        self.orb_pulse += 0.05
        self.cape_sway += 0.03

        # Dibujar componentes del mago
        self.draw_mage_body()
        self.draw_mage_head()
        self.draw_wizard_hat()
        self.draw_mage_arms()
        self.draw_mage_legs()
        self.draw_magic_staff(time)
        self.draw_mage_cape(time)

        glPopMatrix()

    def draw_mage_body(self):
        """Dibujar cuerpo del mago con túnica épica"""
        # Túnica principal azul
        glColor3f(0.2, 0.3, 0.8)
        glPushMatrix()
        glTranslatef(0, 1.0, 0)
        self.renderer.draw_cylinder(0.8, 2.0, 12)
        glPopMatrix()

        # Detalles dorados
        glColor3f(0.8, 0.6, 0.1)

        # Cinturón mágico
        glPushMatrix()
        glTranslatef(0, 0.5, 0)
        self.renderer.draw_cylinder(0.85, 0.15, 12)
        glPopMatrix()

        # Símbolos mágicos en la túnica
        for i in range(4):
            angle = i * 90
            x = 0.7 * math.cos(math.radians(angle))
            z = 0.7 * math.sin(math.radians(angle))

            glPushMatrix()
            glTranslatef(x, 1.2, z)
            glRotatef(angle, 0, 1, 0)
            self.renderer.draw_sphere(0.06, (0.8, 0.6, 0.1), 8, 6)
            glPopMatrix()

    def draw_mage_head(self):
        """Dibujar cabeza del mago"""
        # Cara
        glPushMatrix()
        glTranslatef(0, 2.2, 0)
        glColor3f(0.9, 0.8, 0.7)
        self.renderer.draw_sphere(0.4, (0.9, 0.8, 0.7), 12, 10)
        glPopMatrix()

        # Ojos brillantes mágicos
        eye_glow = 0.8 + 0.2 * math.sin(self.animation_time * 3)

        glPushMatrix()
        glTranslatef(-0.15, 2.3, 0.35)
        glColor3f(0.3 * eye_glow, 0.6 * eye_glow, 1.0 * eye_glow)
        self.renderer.draw_sphere(0.05, (0.3, 0.6, 1.0), 6, 4)
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0.15, 2.3, 0.35)
        glColor3f(0.3 * eye_glow, 0.6 * eye_glow, 1.0 * eye_glow)
        self.renderer.draw_sphere(0.05, (0.3, 0.6, 1.0), 6, 4)
        glPopMatrix()

        # Barba sabia
        glPushMatrix()
        glTranslatef(0, 1.8, 0.3)
        glColor3f(0.85, 0.85, 0.85)
        self.renderer.draw_sphere(0.3, (0.85, 0.85, 0.85), 8, 6)
        glPopMatrix()

    def draw_wizard_hat(self):
        """Dibujar sombrero de mago épico"""
        glColor3f(0.15, 0.15, 0.7)

        # Base del sombrero
        glPushMatrix()
        glTranslatef(0, 2.8, 0)
        self.renderer.draw_cylinder(0.6, 0.2, 12)
        glPopMatrix()

        # Cono del sombrero usando GLU
        glPushMatrix()
        glTranslatef(0, 3.0, 0)
        quadric = gluNewQuadric()
        gluQuadricNormals(quadric, GLU_SMOOTH)
        gluCylinder(quadric, 0.6, 0.1, 1.5, 12, 1)
        gluDeleteQuadric(quadric)
        glPopMatrix()

        # Estrella mágica en la punta
        glPushMatrix()
        glTranslatef(0, 4.5, 0)
        star_glow = 0.8 + 0.2 * math.sin(self.animation_time * 4)
        glColor3f(1.0 * star_glow, 1.0 * star_glow, 0.2)
        self.draw_star(0.15)
        glPopMatrix()

        # Símbolos místicos giratorios en el sombrero
        glColor3f(0.8, 0.6, 0.1)
        for i in range(6):
            angle = i * 60 + self.animation_time * 30
            height = 3.2 + i * 0.2
            radius = 0.5 - i * 0.05

            x = radius * math.cos(math.radians(angle))
            z = radius * math.sin(math.radians(angle))

            glPushMatrix()
            glTranslatef(x, height, z)
            symbol_pulse = 0.6 + 0.4 * math.sin(self.animation_time * 2 + i)
            self.renderer.draw_sphere(0.04, (0.8 * symbol_pulse, 0.6 * symbol_pulse, 0.1), 6, 4)
            glPopMatrix()

    def draw_star(self, size):
        """Dibujar estrella mágica de 5 puntas"""
        glBegin(GL_TRIANGLES)
        for i in range(5):
            angle1 = i * 2 * math.pi / 5
            angle2 = (i + 1) * 2 * math.pi / 5
            angle_mid = (angle1 + angle2) / 2

            # Punto exterior
            x1 = size * math.cos(angle1)
            z1 = size * math.sin(angle1)

            # Punto interior
            x_mid = size * 0.4 * math.cos(angle_mid)
            z_mid = size * 0.4 * math.sin(angle_mid)

            # Punto exterior siguiente
            x2 = size * math.cos(angle2)
            z2 = size * math.sin(angle2)

            # Triángulos de la estrella
            glVertex3f(0, 0, 0)
            glVertex3f(x1, 0, z1)
            glVertex3f(x_mid, 0, z_mid)

            glVertex3f(0, 0, 0)
            glVertex3f(x_mid, 0, z_mid)
            glVertex3f(x2, 0, z2)
        glEnd()

    def draw_mage_arms(self):
        """Dibujar brazos del mago"""
        arm_sway = math.sin(self.animation_time * 1.5) * 5

        # Brazo izquierdo
        glPushMatrix()
        glTranslatef(-1.0, 2.0, 0)
        glRotatef(20 + arm_sway, 0, 0, 1)

        # Hombro
        glColor3f(0.2, 0.3, 0.8)
        self.renderer.draw_sphere(0.25, (0.2, 0.3, 0.8), 8, 6)

        # Brazo
        glTranslatef(0, -0.6, 0)
        self.renderer.draw_cylinder(0.15, 1.2, 8)

        # Antebrazo
        glTranslatef(0, -0.8, 0)
        glRotatef(10, 0, 0, 1)
        self.renderer.draw_cylinder(0.12, 1.0, 8)

        # Mano
        glTranslatef(0, -0.7, 0)
        glColor3f(0.9, 0.8, 0.7)
        self.renderer.draw_sphere(0.18, (0.9, 0.8, 0.7), 8, 6)

        glPopMatrix()

        # Brazo derecho (similar)
        glPushMatrix()
        glTranslatef(1.0, 2.0, 0)
        glRotatef(-20 - arm_sway, 0, 0, 1)

        glColor3f(0.2, 0.3, 0.8)
        self.renderer.draw_sphere(0.25, (0.2, 0.3, 0.8), 8, 6)

        glTranslatef(0, -0.6, 0)
        self.renderer.draw_cylinder(0.15, 1.2, 8)

        glTranslatef(0, -0.8, 0)
        glRotatef(-10, 0, 0, 1)
        self.renderer.draw_cylinder(0.12, 1.0, 8)

        glTranslatef(0, -0.7, 0)
        glColor3f(0.9, 0.8, 0.7)
        self.renderer.draw_sphere(0.18, (0.9, 0.8, 0.7), 8, 6)

        glPopMatrix()

    def draw_mage_legs(self):
        """Dibujar piernas del mago"""
        # Pierna izquierda
        glPushMatrix()
        glTranslatef(-0.4, -0.2, 0)

        # Muslo
        glColor3f(0.2, 0.3, 0.8)
        self.renderer.draw_cylinder(0.25, 1.2, 8)

        # Pantorrilla
        glTranslatef(0, -1.0, 0)
        self.renderer.draw_cylinder(0.2, 1.0, 8)

        # Bota mágica
        glTranslatef(0, -0.8, 0.15)
        glColor3f(0.4, 0.2, 0.1)
        self.renderer.draw_cube(0.25, (0.4, 0.2, 0.1))

        glPopMatrix()

        # Pierna derecha
        glPushMatrix()
        glTranslatef(0.4, -0.2, 0)

        glColor3f(0.2, 0.3, 0.8)
        self.renderer.draw_cylinder(0.25, 1.2, 8)

        glTranslatef(0, -1.0, 0)
        self.renderer.draw_cylinder(0.2, 1.0, 8)

        glTranslatef(0, -0.8, 0.15)
        glColor3f(0.4, 0.2, 0.1)
        self.renderer.draw_cube(0.25, (0.4, 0.2, 0.1))

        glPopMatrix()

    def draw_magic_staff(self, time):
        """Dibujar bastón mágico supremo"""
        glPushMatrix()

        # Animación del bastón
        staff_sway = 0
        if self.is_casting:
            staff_sway = math.sin(time * 5) * 15
            glRotatef(staff_sway, 1, 0, 0)
        elif self.is_attacking:
            staff_sway = math.sin(time * 8) * 25
            glRotatef(staff_sway, 0, 0, 1)

        glTranslatef(1.2, 1.0, 0)
        glRotatef(15, 0, 0, 1)

        # Mango del bastón (madera noble)
        glColor3f(0.6, 0.4, 0.2)
        self.renderer.draw_cylinder(0.08, 2.8, 12)

        # Anillos decorativos
        glColor3f(0.8, 0.6, 0.1)
        for i in range(3):
            glPushMatrix()
            glTranslatef(0, 0.8 + i * 0.6, 0)
            self.renderer.draw_cylinder(0.12, 0.1, 12)
            glPopMatrix()

        # Orbe mágico supremo en la punta
        glPushMatrix()
        glTranslatef(0, 2.8, 0)

        # Pulso mágico
        orb_scale = 1.0 + 0.2 * math.sin(self.orb_pulse)
        if self.is_casting:
            orb_scale = 1.0 + 0.4 * math.sin(time * 6)

        glScalef(orb_scale, orb_scale, orb_scale)

        # Orbe principal
        orb_intensity = 0.8 + 0.2 * math.sin(time * 4)
        if self.is_casting:
            orb_intensity = 1.0

        glColor3f(0.3 * orb_intensity, 0.8 * orb_intensity, 1.0 * orb_intensity)
        self.renderer.draw_sphere(0.25, (0.3, 0.8, 1.0), 12, 10)

        # Núcleo brillante
        glColor3f(1.0, 1.0, 1.0)
        self.renderer.draw_sphere(0.12, (1.0, 1.0, 1.0), 8, 6)

        glPopMatrix()

        # Cristales orbitales mágicos
        if self.is_casting:
            glPushMatrix()
            glTranslatef(0, 2.8, 0)
            glRotatef(time * 120, 0, 1, 0)

            for i in range(6):
                angle = i * 60
                orbit_radius = 0.5 + 0.1 * math.sin(time * 3 + i)

                glPushMatrix()
                glRotatef(angle, 0, 1, 0)
                glTranslatef(orbit_radius, math.sin(time * 4 + i) * 0.1, 0)

                crystal_glow = 0.6 + 0.4 * math.sin(time * 5 + i)
                glColor3f(0.8 * crystal_glow, 0.4 * crystal_glow, 1.0 * crystal_glow)
                self.renderer.draw_sphere(0.08, (0.8, 0.4, 1.0), 6, 4)

                glPopMatrix()

            glPopMatrix()

        glPopMatrix()

    def draw_mage_cape(self, time):
        """Dibujar capa mágica flotante"""
        glPushMatrix()
        glTranslatef(0, 1.5, -0.8)

        # Movimiento ondulante de la capa
        cape_wave = math.sin(self.cape_sway) * 8
        glRotatef(cape_wave, 1, 0, 0)

        # Capa semitransparente
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        glColor4f(0.1, 0.1, 0.6, 0.8)

        # Dibujar capa como superficie curvada
        glBegin(GL_TRIANGLE_STRIP)
        segments = 16
        for i in range(segments + 1):
            angle = math.pi * i / segments - math.pi/2

            # Ondulación de la capa
            wave_offset = 0.2 * math.sin(angle * 3 + time * 2)

            radius_top = 1.0
            radius_bottom = 1.4 + wave_offset

            x_top = radius_top * math.cos(angle)
            z_top = radius_top * math.sin(angle)
            x_bottom = radius_bottom * math.cos(angle)
            z_bottom = radius_bottom * math.sin(angle)

            glVertex3f(x_top, 0.5, z_top)
            glVertex3f(x_bottom, -2.0 + wave_offset, z_bottom)
        glEnd()

        glDisable(GL_BLEND)
        glPopMatrix()

class KnightModel(Character3D):
    """Modelo 3D épico del Caballero Paladín"""

    def __init__(self, renderer):
        super().__init__(renderer)
        self.sword_swing_angle = 0
        self.shield_raised = False
        self.plume_sway = 0

    def draw(self, time):
        """Dibujar el modelo completo del caballero"""
        glPushMatrix()

        # Aplicar transformaciones
        glTranslatef(self.position[0], self.position[1] + self.bob_offset, self.position[2])
        glRotatef(self.rotation[1], 0, 1, 0)
        glScalef(*self.scale)

        # Actualizar animaciones
        self.plume_sway += 0.02

        # Dibujar componentes del caballero
        self.draw_knight_body()
        self.draw_knight_head()
        self.draw_knight_helmet(time)
        self.draw_knight_arms()
        self.draw_knight_legs()
        self.draw_knight_sword(time)
        self.draw_knight_shield()
        self.draw_knight_cape(time)

        glPopMatrix()

    def draw_knight_body(self):
        """Dibujar armadura del caballero"""
        # Peto (pecho de armadura)
        glColor3f(0.8, 0.8, 0.9)
        glPushMatrix()
        glTranslatef(0, 1.2, 0)
        self.renderer.draw_cube(0.9, (0.8, 0.8, 0.9))
        glPopMatrix()

        # Hombreras
        glColor3f(0.75, 0.75, 0.85)

        # Hombrera izquierda
        glPushMatrix()
        glTranslatef(-0.9, 1.8, 0)
        self.renderer.draw_sphere(0.35, (0.75, 0.75, 0.85), 8, 6)
        glPopMatrix()

        # Hombrera derecha
        glPushMatrix()
        glTranslatef(0.9, 1.8, 0)
        self.renderer.draw_sphere(0.35, (0.75, 0.75, 0.85), 8, 6)
        glPopMatrix()

        # Cruz sagrada en el pecho
        glColor3f(0.9, 0.8, 0.1)

        # Barra vertical de la cruz
        glPushMatrix()
        glTranslatef(0, 1.4, 0.5)
        glScalef(0.1, 0.6, 0.1)
        self.renderer.draw_cube(1, (0.9, 0.8, 0.1))
        glPopMatrix()

        # Barra horizontal de la cruz
        glPushMatrix()
        glTranslatef(0, 1.6, 0.5)
        glScalef(0.4, 0.1, 0.1)
        self.renderer.draw_cube(1, (0.9, 0.8, 0.1))
        glPopMatrix()

        # Faldones de armadura
        glColor3f(0.7, 0.7, 0.8)
        glPushMatrix()
        glTranslatef(0, 0.2, 0)
        self.renderer.draw_cylinder(0.9, 1.0, 12)
        glPopMatrix()

    def draw_knight_head(self):
        """Dibujar cabeza del caballero"""
        glPushMatrix()
        glTranslatef(0, 2.4, 0)
        glColor3f(0.9, 0.8, 0.7)
        self.renderer.draw_sphere(0.4, (0.9, 0.8, 0.7), 12, 10)

        # Ojos determinados
        glPushMatrix()
        glTranslatef(-0.12, 0.1, 0.35)
        glColor3f(0.2, 0.4, 0.8)
        self.renderer.draw_sphere(0.05, (0.2, 0.4, 0.8), 6, 4)
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0.12, 0.1, 0.35)
        glColor3f(0.2, 0.4, 0.8)
        self.renderer.draw_sphere(0.05, (0.2, 0.4, 0.8), 6, 4)
        glPopMatrix()

        glPopMatrix()

    def draw_knight_helmet(self, time):
        """Dibujar casco épico del caballero"""
        # Casco principal
        glColor3f(0.7, 0.7, 0.8)
        glPushMatrix()
        glTranslatef(0, 2.6, 0)
        self.renderer.draw_sphere(0.45, (0.7, 0.7, 0.8), 12, 10)
        glPopMatrix()

        # Visera
        glPushMatrix()
        glTranslatef(0, 2.5, 0.4)
        glColor3f(0.6, 0.6, 0.7)
        glScalef(0.8, 0.3, 0.1)
        self.renderer.draw_cube(0.5, (0.6, 0.6, 0.7))
        glPopMatrix()

        # Penacho heroico ondulante
        glPushMatrix()
        glTranslatef(0, 3.2, -0.2)

        plume_wave = math.sin(self.plume_sway) * 8
        glRotatef(plume_wave, 1, 0, 0)

        glColor3f(0.8, 0.2, 0.2)

        # Plumas del penacho
        for i in range(7):
            glPushMatrix()
            glTranslatef((i - 3) * 0.08, 0, 0)
            glRotatef(i * 8 - 24, 0, 0, 1)

            # Pluma individual
            height = 0.8 + (3 - abs(i - 3)) * 0.15
            self.renderer.draw_cylinder(0.03, height, 6)

            glPopMatrix()

        glPopMatrix()

    def draw_knight_arms(self):
        """Dibujar brazos blindados del caballero"""
        # Brazo izquierdo (escudo)
        glPushMatrix()
        glTranslatef(-1.2, 2.0, 0)
        glRotatef(25, 0, 0, 1)

        # Hombro
        glColor3f(0.75, 0.75, 0.85)
        self.renderer.draw_sphere(0.3, (0.75, 0.75, 0.85), 8, 6)

        # Brazo superior
        glTranslatef(0, -0.7, 0)
        self.renderer.draw_cylinder(0.2, 1.4, 8)

        # Codo
        glTranslatef(0, -0.8, 0)
        self.renderer.draw_sphere(0.18, (0.75, 0.75, 0.85), 8, 6)

        # Antebrazo
        glTranslatef(0, -0.6, 0)
        glRotatef(10, 0, 0, 1)
        self.renderer.draw_cylinder(0.18, 1.2, 8)

        # Guantelete
        glTranslatef(0, -0.8, 0)
        glColor3f(0.6, 0.6, 0.7)
        self.renderer.draw_cube(0.25, (0.6, 0.6, 0.7))

        glPopMatrix()

        # Brazo derecho (espada)
        glPushMatrix()
        glTranslatef(1.2, 2.0, 0)
        glRotatef(-25, 0, 0, 1)

        glColor3f(0.75, 0.75, 0.85)
        self.renderer.draw_sphere(0.3, (0.75, 0.75, 0.85), 8, 6)

        glTranslatef(0, -0.7, 0)
        self.renderer.draw_cylinder(0.2, 1.4, 8)

        glTranslatef(0, -0.8, 0)
        self.renderer.draw_sphere(0.18, (0.75, 0.75, 0.85), 8, 6)

        glTranslatef(0, -0.6, 0)
        glRotatef(-10, 0, 0, 1)
        self.renderer.draw_cylinder(0.18, 1.2, 8)

        glTranslatef(0, -0.8, 0)
        glColor3f(0.6, 0.6, 0.7)
        self.renderer.draw_cube(0.25, (0.6, 0.6, 0.7))

        glPopMatrix()

    def draw_knight_legs(self):
        """Dibujar piernas blindadas del caballero"""
        # Pierna izquierda
        glPushMatrix()
        glTranslatef(-0.5, -0.2, 0)

        # Muslo blindado
        glColor3f(0.75, 0.75, 0.85)
        self.renderer.draw_cylinder(0.3, 1.5, 8)

        # Rodillera
        glTranslatef(0, -1.2, 0)
        self.renderer.draw_sphere(0.25, (0.6, 0.6, 0.7), 8, 6)

        # Espinillera
        glTranslatef(0, -0.8, 0)
        self.renderer.draw_cylinder(0.25, 1.2, 8)

        # Bota de acero
        glTranslatef(0, -1.0, 0.2)
        glColor3f(0.6, 0.6, 0.7)
        self.renderer.draw_cube(0.3, (0.6, 0.6, 0.7))

        glPopMatrix()

        # Pierna derecha
        glPushMatrix()
        glTranslatef(0.5, -0.2, 0)

        glColor3f(0.75, 0.75, 0.85)
        self.renderer.draw_cylinder(0.3, 1.5, 8)

        glTranslatef(0, -1.2, 0)
        self.renderer.draw_sphere(0.25, (0.6, 0.6, 0.7), 8, 6)

        glTranslatef(0, -0.8, 0)
        self.renderer.draw_cylinder(0.25, 1.2, 8)

        glTranslatef(0, -1.0, 0.2)
        glColor3f(0.6, 0.6, 0.7)
        self.renderer.draw_cube(0.3, (0.6, 0.6, 0.7))

        glPopMatrix()

    def draw_knight_sword(self, time):
        """Dibujar espada legendaria del caballero"""
        glPushMatrix()

        # Animación de ataque
        if self.is_attacking:
            self.sword_swing_angle = 45 * math.sin(time * 8)
            glRotatef(self.sword_swing_angle, 1, 0, 0)

        glTranslatef(1.8, 1.0, 0)
        glRotatef(10, 0, 0, 1)

        # Empuñadura de cuero
        glColor3f(0.4, 0.2, 0.1)
        self.renderer.draw_cylinder(0.06, 0.5, 8)

        # Guarda ornamentada
        glPushMatrix()
        glTranslatef(0, 0.5, 0)
        glColor3f(0.8, 0.8, 0.9)
        glScalef(0.5, 0.08, 0.08)
        self.renderer.draw_cube(1, (0.8, 0.8, 0.9))
        glPopMatrix()

        # Hoja de la espada
        glPushMatrix()
        glTranslatef(0, 0.6, 0)
        glColor3f(0.9, 0.9, 1.0)
        glScalef(0.08, 2.0, 0.03)
        self.renderer.draw_cube(1, (0.9, 0.9, 1.0))
        glPopMatrix()

        # Punta de la espada
        glPushMatrix()
        glTranslatef(0, 2.6, 0)
        glColor3f(0.95, 0.95, 1.0)
        quadric = gluNewQuadric()
        gluQuadricNormals(quadric, GLU_SMOOTH)
        gluCylinder(quadric, 0.08, 0, 0.3, 8, 1)
        gluDeleteQuadric(quadric)
        glPopMatrix()

        # Filo brillante (efecto mágico)
        if self.is_attacking:
            glPushMatrix()
            glTranslatef(0, 1.3, 0.04)
            glColor3f(0.8, 0.9, 1.0)
            glScalef(0.02, 1.6, 0.01)
            self.renderer.draw_cube(1, (0.8, 0.9, 1.0))
            glPopMatrix()

        # Pomo con gema
        glPushMatrix()
        glTranslatef(0, -0.2, 0)
        glColor3f(0.8, 0.8, 0.9)
        self.renderer.draw_sphere(0.12, (0.8, 0.8, 0.9), 8, 6)

        # Gema central
        gem_glow = 0.8 + 0.2 * math.sin(time * 3)
        glColor3f(0.2 * gem_glow, 0.6 * gem_glow, 1.0 * gem_glow)
        self.renderer.draw_sphere(0.06, (0.2, 0.6, 1.0), 6, 4)

        glPopMatrix()
        glPopMatrix()

    def draw_knight_shield(self):
        """Dibujar escudo sagrado del caballero"""
        glPushMatrix()
        glTranslatef(-1.8, 1.2, 0)

        if self.shield_raised:
            glRotatef(-20, 0, 1, 0)
            glTranslatef(0, 0.2, 0)

        # Escudo principal
        glColor3f(0.8, 0.1, 0.1)
        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glScalef(0.15, 1.4, 1.0)
        self.renderer.draw_cylinder(1, 1, 12)
        glPopMatrix()

        # Borde metálico
        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glColor3f(0.6, 0.6, 0.7)
        glScalef(0.05, 1.5, 1.1)
        self.renderer.draw_cylinder(1, 1, 16)
        glPopMatrix()

        # Emblema sagrado (cruz dorada)
        glPushMatrix()
        glTranslatef(0.16, 0, 0)
        glRotatef(90, 0, 1, 0)
        glColor3f(0.9, 0.8, 0.1)

        # Vertical de la cruz
        glPushMatrix()
        glScalef(0.08, 0.6, 0.02)
        self.renderer.draw_cube(1, (0.9, 0.8, 0.1))
        glPopMatrix()

        # Horizontal de la cruz
        glPushMatrix()
        glScalef(0.4, 0.08, 0.02)
        self.renderer.draw_cube(1, (0.9, 0.8, 0.1))
        glPopMatrix()

        glPopMatrix()

        # Remaches decorativos
        glColor3f(0.8, 0.8, 0.9)
        for i in range(8):
            angle = i * 45
            radius = 0.8
            x = 0.12 + radius * 0.1 * math.cos(math.radians(angle))
            y = radius * math.sin(math.radians(angle))

            glPushMatrix()
            glTranslatef(x, y, 0)
            self.renderer.draw_sphere(0.04, (0.8, 0.8, 0.9), 6, 4)
            glPopMatrix()

        glPopMatrix()

    def draw_knight_cape(self, time):
        """Dibujar capa heroica del caballero"""
        glPushMatrix()
        glTranslatef(0, 1.8, -0.9)

        # Movimiento de la capa
        cape_sway = math.sin(time * 1.5) * 6
        glRotatef(cape_sway, 1, 0, 0)

        glColor3f(0.6, 0.1, 0.1)

        # Capa principal
        glBegin(GL_TRIANGLE_STRIP)
        segments = 12
        for i in range(segments + 1):
            angle = math.pi * i / segments - math.pi/2

            # Ondulación de la capa
            wave = 0.1 * math.sin(angle * 4 + time * 3)

            radius_top = 1.2
            radius_bottom = 1.6 + wave
            height = 2.8

            x_top = radius_top * math.cos(angle)
            z_top = radius_top * math.sin(angle)
            x_bottom = radius_bottom * math.cos(angle)
            z_bottom = radius_bottom * math.sin(angle)

            glVertex3f(x_top, 0, z_top)
            glVertex3f(x_bottom, -height + wave * 0.5, z_bottom)
        glEnd()

        # Broche dorado de la capa
        glPushMatrix()
        glTranslatef(0, 0.3, 0)
        glColor3f(0.9, 0.8, 0.1)
        self.renderer.draw_sphere(0.08, (0.9, 0.8, 0.1), 8, 6)
        glPopMatrix()

        glPopMatrix()