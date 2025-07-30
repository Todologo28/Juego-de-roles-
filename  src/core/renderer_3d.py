"""
Sistema de renderizado 3D épico para RPG
"""

import math
import random
from OpenGL.GL import *
from OpenGL.GLU import *

class Renderer3D:
    """Sistema de renderizado 3D avanzado"""

    def __init__(self):
        self.camera_angle_x = 0
        self.camera_angle_y = 0
        self.camera_distance = 15
        self.lighting_enabled = True
        self.wireframe_mode = False

        self.setup_lighting()

    def setup_lighting(self):
        """Configurar iluminación épica"""
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_LIGHT1)

        # Luz principal (sol épico)
        light_pos = [5.0, 10.0, 5.0, 1.0]
        light_ambient = [0.3, 0.3, 0.4, 1.0]
        light_diffuse = [1.0, 0.9, 0.8, 1.0]
        light_specular = [1.0, 1.0, 1.0, 1.0]

        glLightfv(GL_LIGHT0, GL_POSITION, light_pos)
        glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
        glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)

        # Luz dramática (roja)
        dramatic_pos = [-5.0, 5.0, -5.0, 1.0]
        dramatic_diffuse = [0.8, 0.2, 0.2, 1.0]

        glLightfv(GL_LIGHT1, GL_POSITION, dramatic_pos)
        glLightfv(GL_LIGHT1, GL_DIFFUSE, dramatic_diffuse)

        # Material por defecto
        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

    def setup_camera(self, angle_x=20, angle_y=45, distance=15):
        """Configurar cámara épica"""
        self.camera_angle_x = angle_x
        self.camera_angle_y = angle_y
        self.camera_distance = distance

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        # Posición de cámara cinematográfica
        gluLookAt(
            distance * math.cos(math.radians(angle_y)) * math.cos(math.radians(angle_x)),
            distance * math.sin(math.radians(angle_x)),
            distance * math.sin(math.radians(angle_y)) * math.cos(math.radians(angle_x)),
            0, 0, 0,  # Mirar al centro
            0, 1, 0   # Vector up
        )

    def clear_screen(self, r=0.1, g=0.1, b=0.2):
        """Limpiar pantalla con color épico"""
        glClearColor(r, g, b, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    def draw_cube(self, size=1.0, color=(1, 1, 1)):
        """Dibujar cubo épico con efectos"""
        glColor3f(*color)

        if self.wireframe_mode:
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        else:
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

        glBegin(GL_QUADS)

        # Cara frontal
        glNormal3f(0, 0, 1)
        glVertex3f(-size, -size,  size)
        glVertex3f( size, -size,  size)
        glVertex3f( size,  size,  size)
        glVertex3f(-size,  size,  size)

        # Cara trasera
        glNormal3f(0, 0, -1)
        glVertex3f(-size, -size, -size)
        glVertex3f(-size,  size, -size)
        glVertex3f( size,  size, -size)
        glVertex3f( size, -size, -size)

        # Cara superior
        glNormal3f(0, 1, 0)
        glVertex3f(-size,  size, -size)
        glVertex3f(-size,  size,  size)
        glVertex3f( size,  size,  size)
        glVertex3f( size,  size, -size)

        # Cara inferior
        glNormal3f(0, -1, 0)
        glVertex3f(-size, -size, -size)
        glVertex3f( size, -size, -size)
        glVertex3f( size, -size,  size)
        glVertex3f(-size, -size,  size)

        # Cara derecha
        glNormal3f(1, 0, 0)
        glVertex3f( size, -size, -size)
        glVertex3f( size,  size, -size)
        glVertex3f( size,  size,  size)
        glVertex3f( size, -size,  size)

        # Cara izquierda
        glNormal3f(-1, 0, 0)
        glVertex3f(-size, -size, -size)
        glVertex3f(-size, -size,  size)
        glVertex3f(-size,  size,  size)
        glVertex3f(-size,  size, -size)

        glEnd()

    def draw_sphere(self, radius=1.0, color=(1, 1, 1), slices=16, stacks=16):
        """Dibujar esfera épica"""
        glColor3f(*color)

        quadric = gluNewQuadric()
        gluQuadricNormals(quadric, GLU_SMOOTH)
        gluQuadricTexture(quadric, GL_TRUE)

        if self.wireframe_mode:
            gluQuadricDrawStyle(quadric, GLU_LINE)
        else:
            gluQuadricDrawStyle(quadric, GLU_FILL)

        gluSphere(quadric, radius, slices, stacks)
        gluDeleteQuadric(quadric)

    def draw_cylinder(self, radius=1.0, height=2.0, slices=16):
        """Dibujar cilindro épico"""
        quadric = gluNewQuadric()
        gluQuadricNormals(quadric, GLU_SMOOTH)

        if self.wireframe_mode:
            gluQuadricDrawStyle(quadric, GLU_LINE)
        else:
            gluQuadricDrawStyle(quadric, GLU_FILL)

        # Cilindro
        gluCylinder(quadric, radius, radius, height, slices, 1)

        # Tapa inferior
        glPushMatrix()
        glRotatef(180, 1, 0, 0)
        gluDisk(quadric, 0, radius, slices, 1)
        glPopMatrix()

        # Tapa superior
        glPushMatrix()
        glTranslatef(0, 0, height)
        gluDisk(quadric, 0, radius, slices, 1)
        glPopMatrix()

        gluDeleteQuadric(quadric)

    def draw_floor(self, size=20):
        """Dibujar suelo épico de batalla"""
        glColor3f(0.3, 0.3, 0.35)

        glBegin(GL_QUADS)
        glNormal3f(0, 1, 0)
        glVertex3f(-size, -2, -size)
        glVertex3f( size, -2, -size)
        glVertex3f( size, -2,  size)
        glVertex3f(-size, -2,  size)
        glEnd()

        # Líneas de cuadrícula épicas
        glColor3f(0.4, 0.4, 0.5)
        glBegin(GL_LINES)

        for i in range(-size, size + 1, 2):
            # Líneas horizontales
            glVertex3f(-size, -1.9, i)
            glVertex3f( size, -1.9, i)

            # Líneas verticales
            glVertex3f(i, -1.9, -size)
            glVertex3f(i, -1.9,  size)

        glEnd()

    def draw_background_elements(self, time):
        """Dibujar elementos de fondo épicos"""
        # Pilares místicos
        for i in range(4):
            angle = i * 90
            x = 12 * math.cos(math.radians(angle))
            z = 12 * math.sin(math.radians(angle))

            glPushMatrix()
            glTranslatef(x, 0, z)
            glColor3f(0.6, 0.6, 0.7)
            self.draw_cylinder(0.5, 8, 12)

            # Antorcha en la cima
            glTranslatef(0, 0, 8.5)
            glColor3f(1, 0.7, 0.2)

            # Efecto de llama parpadeante
            flame_intensity = 0.8 + 0.2 * math.sin(time * 3 + i)
            glColor3f(flame_intensity, 0.7 * flame_intensity, 0.2)
            self.draw_sphere(0.3, (flame_intensity, 0.7 * flame_intensity, 0.2), 8, 6)

            glPopMatrix()

    def draw_magic_circle(self, radius=8, time=0):
        """Dibujar círculo mágico épico"""
        glColor3f(0.7, 0.3, 1.0)
        glBegin(GL_LINE_LOOP)

        segments = 60
        for i in range(segments):
            angle = 2 * math.pi * i / segments
            x = radius * math.cos(angle + time * 0.5)
            z = radius * math.sin(angle + time * 0.5)
            glVertex3f(x, -1.8, z)

        glEnd()

        # Símbolos místicos
        glColor3f(0.5, 0.2, 0.8)
        for i in range(8):
            angle = i * 45 + time * 10
            x = (radius * 0.7) * math.cos(math.radians(angle))
            z = (radius * 0.7) * math.sin(math.radians(angle))

            glPushMatrix()
            glTranslatef(x, -1.7, z)
            glRotatef(angle, 0, 1, 0)
            self.draw_cube(0.2, (0.5, 0.2, 0.8))
            glPopMatrix()

    def draw_damage_number(self, damage, position, time_alive):
        """Dibujar números de daño flotantes"""
        if time_alive > 2.0:
            return

        # Calcular posición flotante
        float_y = position[1] + time_alive * 2
        alpha = max(0, 1 - time_alive / 2)

        glPushMatrix()
        glTranslatef(position[0], float_y, position[2])

        # Color según tipo de daño
        if damage > 50:
            glColor4f(1, 0, 0, alpha)  # Rojo para daño crítico
        elif damage > 20:
            glColor4f(1, 0.5, 0, alpha)  # Naranja para daño normal
        else:
            glColor4f(1, 1, 1, alpha)  # Blanco para daño menor

        # Representar número con cubitos
        num_str = str(int(damage))
        x_offset = -len(num_str) * 0.1

        for digit in num_str:
            digit_val = int(digit)
            for i in range(digit_val):
                glPushMatrix()
                glTranslatef(x_offset, i * 0.1, 0)
                self.draw_cube(0.05)
                glPopMatrix()
            x_offset += 0.2

        glPopMatrix()

    def draw_spell_effect(self, spell_type, position, intensity=1.0, time=0):
        """Dibujar efectos de hechizos épicos"""
        glPushMatrix()
        glTranslatef(*position)

        if spell_type == "fireball":
            # Bola de fuego épica
            for i in range(3):
                glPushMatrix()
                glRotatef(time * 100 + i * 120, 0, 1, 0)
                glTranslatef(intensity * 0.5, 0, 0)

                fire_color = (
                    1.0,
                    0.5 + 0.3 * math.sin(time * 5),
                    0.1 * math.sin(time * 3)
                )
                glColor3f(*fire_color)
                self.draw_sphere(0.3 * intensity, fire_color, 8, 6)
                glPopMatrix()

        elif spell_type == "ice_shard":
            # Cristal de hielo
            glColor3f(0.7, 0.9, 1.0)
            glRotatef(time * 50, 0, 1, 0)

            for i in range(6):
                glPushMatrix()
                glRotatef(i * 60, 0, 1, 0)
                glTranslatef(0, 0, intensity * 0.8)
                glScalef(0.2, 0.2, 1.5)
                self.draw_cube(intensity * 0.5, (0.7, 0.9, 1.0))
                glPopMatrix()

        elif spell_type == "lightning":
            # Rayo eléctrico
            glColor3f(1, 1, 0.8)
            segments = 8

            glBegin(GL_LINE_STRIP)
            for i in range(segments):
                y = (i / segments) * intensity * 3
                x = 0.5 * math.sin(time * 10 + i) * intensity
                z = 0.3 * math.cos(time * 15 + i) * intensity
                glVertex3f(x, y, z)
            glEnd()

        elif spell_type == "heal":
            # Efecto de curación
            glColor3f(0.2, 1.0, 0.3)

            for i in range(12):
                angle = i * 30 + time * 50
                radius = 1.5 * intensity
                x = radius * math.cos(math.radians(angle))
                z = radius * math.sin(math.radians(angle))
                y = 2 * math.sin(time * 3 + i * 0.5) * intensity

                glPushMatrix()
                glTranslatef(x, y, z)
                self.draw_sphere(0.1 * intensity, (0.2, 1.0, 0.3), 6, 4)
                glPopMatrix()

        glPopMatrix()

    def toggle_wireframe(self):
        """Alternar modo wireframe"""
        self.wireframe_mode = not self.wireframe_mode

    def toggle_lighting(self):
        """Alternar iluminación"""
        self.lighting_enabled = not self.lighting_enabled
        if self.lighting_enabled:
            glEnable(GL_LIGHTING)
        else:
            glDisable(GL_LIGHTING)

    def update_camera(self, angle_x_delta=0, angle_y_delta=0, distance_delta=0):
        """Actualizar cámara dinámicamente"""
        self.camera_angle_x += angle_x_delta
        self.camera_angle_y += angle_y_delta
        self.camera_distance += distance_delta

        # Limitar ángulos
        self.camera_angle_x = max(-80, min(80, self.camera_angle_x))
        self.camera_distance = max(5, min(30, self.camera_distance))ñ