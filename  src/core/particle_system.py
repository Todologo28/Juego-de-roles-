"""
Sistema de partículas épico para efectos visuales
"""

import random
import math
from OpenGL.GL import *

class Particle:
    """Partícula individual"""

    def __init__(self, position, velocity, color, life_time=2.0, size=0.1):
        self.position = list(position)
        self.velocity = list(velocity)
        self.color = list(color)
        self.life_time = life_time
        self.max_life_time = life_time
        self.size = size
        self.initial_size = size
        self.gravity = -5.0
        self.alive = True

    def update(self, dt):
        """Actualizar partícula"""
        if not self.alive:
            return

        # Actualizar posición
        self.position[0] += self.velocity[0] * dt
        self.position[1] += self.velocity[1] * dt
        self.position[2] += self.velocity[2] * dt

        # Aplicar gravedad
        self.velocity[1] += self.gravity * dt

        # Reducir vida
        self.life_time -= dt
        if self.life_time <= 0:
            self.alive = False
            return

        # Fade out
        life_ratio = self.life_time / self.max_life_time
        self.color[3] = life_ratio  # Alpha
        self.size = self.initial_size * (0.5 + 0.5 * life_ratio)

    def render(self, renderer):
        """Renderizar partícula"""
        if not self.alive:
            return

        glPushMatrix()
        glTranslatef(*self.position)

        # Configurar transparencia
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        glColor4f(*self.color)
        renderer.draw_sphere(self.size, self.color[:3], 4, 4)

        glDisable(GL_BLEND)
        glPopMatrix()

class ParticleSystem:
    """Sistema de partículas épico"""

    def __init__(self, renderer):
        self.renderer = renderer
        self.particles = []
        self.max_particles = 1000

    def emit_explosion(self, position, color=(1, 0.5, 0), count=50):
        """Emitir explosión épica"""
        for _ in range(count):
            # Velocidad aleatoria en todas las direcciones
            velocity = [
                random.uniform(-8, 8),
                random.uniform(2, 10),
                random.uniform(-8, 8)
            ]

            # Color con variación
            particle_color = [
                color[0] + random.uniform(-0.2, 0.2),
                color[1] + random.uniform(-0.2, 0.2),
                color[2] + random.uniform(-0.2, 0.2),
                1.0
            ]

            # Clamp colors
            for i in range(3):
                particle_color[i] = max(0, min(1, particle_color[i]))

            particle = Particle(
                position.copy(),
                velocity,
                particle_color,
                life_time=random.uniform(1.0, 3.0),
                size=random.uniform(0.05, 0.2)
            )

            self.add_particle(particle)

    def emit_fire(self, position, intensity=1.0):
        """Emitir fuego épico"""
        count = int(20 * intensity)

        for _ in range(count):
            # Llamas hacia arriba con algo de dispersión
            velocity = [
                random.uniform(-2, 2) * intensity,
                random.uniform(3, 8) * intensity,
                random.uniform(-2, 2) * intensity
            ]

            # Colores de fuego
            fire_colors = [
                [1.0, 0.8, 0.2, 1.0],  # Amarillo
                [1.0, 0.4, 0.1, 1.0],  # Naranja
                [0.9, 0.2, 0.0, 1.0],  # Rojo
            ]

            color = random.choice(fire_colors)

            particle = Particle(
                [position[0] + random.uniform(-0.5, 0.5),
                 position[1],
                 position[2] + random.uniform(-0.5, 0.5)],
                velocity,
                color,
                life_time=random.uniform(0.5, 2.0),
                size=random.uniform(0.1, 0.3)
            )
            particle.gravity = -2.0  # Menos gravedad para el fuego

            self.add_particle(particle)

    def emit_ice(self, position, intensity=1.0):
        """Emitir cristales de hielo"""
        count = int(30 * intensity)

        for _ in range(count):
            # Cristales que caen y se dispersan
            velocity = [
                random.uniform(-5, 5) * intensity,
                random.uniform(-2, 4) * intensity,
                random.uniform(-5, 5) * intensity
            ]

            # Colores fríos
            ice_color = [
                0.7 + random.uniform(-0.2, 0.2),
                0.9 + random.uniform(-0.1, 0.1),
                1.0,
                1.0
            ]

            particle = Particle(
                position.copy(),
                velocity,
                ice_color,
                life_time=random.uniform(1.5, 3.0),
                size=random.uniform(0.05, 0.15)
            )

            self.add_particle(particle)

    def emit_lightning(self, start_pos, end_pos):
        """Emitir chispas de rayo"""
        # Calcular puntos a lo largo del rayo
        steps = 20
        for i in range(steps):
            t = i / steps

            position = [
                start_pos[0] + t * (end_pos[0] - start_pos[0]),
                start_pos[1] + t * (end_pos[1] - start_pos[1]),
                start_pos[2] + t * (end_pos[2] - start_pos[2])
            ]

            # Añadir ruido a la posición
            position[0] += random.uniform(-0.5, 0.5)
            position[1] += random.uniform(-0.5, 0.5)
            position[2] += random.uniform(-0.5, 0.5)

            # Chispas eléctricas
            for _ in range(3):
                velocity = [
                    random.uniform(-3, 3),
                    random.uniform(-3, 3),
                    random.uniform(-3, 3)
                ]

                electric_color = [
                    1.0,
                    1.0,
                    0.8 + random.uniform(-0.2, 0.2),
                    1.0
                ]

                particle = Particle(
                    position.copy(),
                    velocity,
                    electric_color,
                    life_time=random.uniform(0.2, 0.8),
                    size=random.uniform(0.02, 0.08)
                )
                particle.gravity = 0  # Sin gravedad para chispas

                self.add_particle(particle)

    def emit_healing(self, position, intensity=1.0):
        """Emitir partículas de curación"""
        count = int(25 * intensity)

        for _ in range(count):
            # Movimiento suave hacia arriba en espiral
            angle = random.uniform(0, 2 * math.pi)
            radius = random.uniform(0.5, 2.0) * intensity

            velocity = [
                math.cos(angle) * 2,
                random.uniform(2, 6) * intensity,
                math.sin(angle) * 2
            ]

            # Verde curativo brillante
            heal_color = [
                0.2 + random.uniform(-0.1, 0.1),
                1.0,
                0.3 + random.uniform(-0.1, 0.1),
                1.0
            ]

            start_pos = [
                position[0] + math.cos(angle) * radius,
                position[1] + random.uniform(-0.5, 0.5),
                position[2] + math.sin(angle) * radius
            ]

            particle = Particle(
                start_pos,
                velocity,
                heal_color,
                life_time=random.uniform(1.0, 2.5),
                size=random.uniform(0.08, 0.15)
            )
            particle.gravity = -1.0  # Poca gravedad

            self.add_particle(particle)

    def emit_blood(self, position, direction, intensity=1.0):
        """Emitir salpicaduras de sangre"""
        count = int(15 * intensity)

        for _ in range(count):
            # Salpicadura en la dirección del golpe
            velocity = [
                direction[0] * random.uniform(2, 6) + random.uniform(-2, 2),
                random.uniform(1, 4),
                direction[2] * random.uniform(2, 6) + random.uniform(-2, 2)
            ]

            # Rojo sangre
            blood_color = [
                0.8 + random.uniform(-0.2, 0.1),
                0.1 + random.uniform(-0.05, 0.05),
                0.1 + random.uniform(-0.05, 0.05),
                1.0
            ]

            particle = Particle(
                position.copy(),
                velocity,
                blood_color,
                life_time=random.uniform(1.0, 2.0),
                size=random.uniform(0.03, 0.1)
            )

            self.add_particle(particle)

    def emit_magic_aura(self, position, color=(0.7, 0.3, 1.0)):
        """Emitir aura mágica continua"""
        for _ in range(10):
            # Movimiento circular flotante
            angle = random.uniform(0, 2 * math.pi)
            radius = random.uniform(1.0, 2.5)

            velocity = [
                math.cos(angle) * 0.5,
                random.uniform(0.5, 2.0),
                math.sin(angle) * 0.5
            ]

            aura_color = [
                color[0] + random.uniform(-0.2, 0.2),
                color[1] + random.uniform(-0.2, 0.2),
                color[2] + random.uniform(-0.2, 0.2),
                0.6
            ]

            # Clamp colors
            for i in range(3):
                aura_color[i] = max(0, min(1, aura_color[i]))

            start_pos = [
                position[0] + math.cos(angle) * radius,
                position[1] + random.uniform(-1, 1),
                position[2] + math.sin(angle) * radius
            ]

            particle = Particle(
                start_pos,
                velocity,
                aura_color,
                life_time=random.uniform(2.0, 4.0),
                size=random.uniform(0.05, 0.12)
            )
            particle.gravity = 0  # Flotante

            self.add_particle(particle)

    def add_particle(self, particle):
        """Añadir partícula al sistema"""
        if len(self.particles) < self.max_particles:
            self.particles.append(particle)

    def update(self, dt):
        """Actualizar todas las partículas"""
        # Actualizar partículas existentes
        for particle in self.particles[:]:
            particle.update(dt)
            if not particle.alive:
                self
