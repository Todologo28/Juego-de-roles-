def draw(self, time):
    """Dibujar el modelo completo del mago"""
    glPushMatrix()

    # Aplicar transformaciones
    glTranslatef(*self.position)
    glRotatef(self.rotation[1], 0, 1, 0)
    glScalef(*self.scale)

    # Actualizar fases de animación
    self.orb_pulse_phase += 0.05
    self.crystal_rotation += 2
    self.cape_wave += 0.03

    # Dibujar componentes
    self.draw_body()
    self.draw_cape(time)
    self.draw_head()
    self.draw_hat()
    self.draw_arms()
    self.draw_legs()
    self.draw_magic_staff(time)
    self.draw_aura(time)

    glPopMatrix()

def draw_body(self):
    """Dibujar cuerpo del mago"""
    glPushMatrix()
    glTranslatef(0, 1.6, 0)

    # Material del cuerpo
    self.renderer.set_material(
        [0.1, 0.05, 0.2, 1.0],  # Ambient púrpura oscuro
        [0.3, 0.2, 0.8, 1.0],   # Diffuse púrpura
        [0.5, 0.4, 1.0, 1.0],   # Specular azul brillante
        [50.0]                   # Shininess
    )

    glColor3f(0.28, 0.2, 0.83)
    self.renderer.draw_cylinder(0.9, 2.8, 16)

    # Detalles dorados en el cuerpo
    glColor3f(1.0, 0.84, 0.0)
    for i in range(4):
        glPushMatrix()
        glTranslatef(0, -1 + i * 0.7, 0)
        glRotatef(i * 90, 0, 1, 0)
        glTranslatef(0.85, 0, 0)
        self.renderer.draw_sphere(0.08, (1, 0.84, 0), 8, 6)
        glPopMatrix()

    glPopMatrix()

def draw_cape(self, time):
    """Dibujar capa flotante mágica"""
    glPushMatrix()
    glTranslatef(0, 1.5, -0.3)

    # Movimiento ondulante de la capa
    wave_offset = math.sin(self.cape_wave) * 0.1
    glRotatef(wave_offset * 10, 1, 0, 0)

    # Material de la capa
    self.renderer.set_material(
        [0.05, 0.02, 0.15, 0.8],
        [0.2, 0.1, 0.4, 0.8],
        [0.3, 0.15, 0.6, 0.8],
        [30.0]
    )

    glColor4f(0.18, 0.11, 0.42, 0.85)

    # Dibujar capa como cilindro abierto
    glBegin(GL_QUAD_STRIP)
    segments = 24
    for i in range(segments + 1):
        angle = math.pi * 1.5 * i / segments - math.pi * 0.75
        radius_top = 1.3
        radius_bottom = 1.7
        height = 3.2

        # Añadir ondulación
        wave = math.sin(angle * 3 + time * 2) * 0.1

        x_top = (radius_top + wave * 0.3) * math.cos(angle)
        z_top = (radius_top + wave * 0.3) * math.sin(angle)
        x_bottom = (radius_bottom + wave) * math.cos(angle)
        z_bottom = (radius_bottom + wave) * math.sin(angle)

        glNormal3f(math.cos(angle), 0, math.sin(angle))
        glVertex3f(x_top, 0, z_top)
        glVertex3f(x_bottom, -height, z_bottom + wave * 0.5)
    glEnd()

    glPopMatrix()

def draw_head(self):
    """Dibujar cabeza del mago"""
    glPushMatrix()
    glTranslatef(0, 3.4, 0)

    # Cabeza
    glColor3f(1.0, 0.86, 0.67)  # Color piel
    self.renderer.draw_sphere(0.65, (1.0, 0.86, 0.67), 20, 16)

    # Ojos brillantes mágicos
    eye_glow = 0.8 + math.sin(time * 3) * 0.2

    glPushMatrix()
    glTranslatef(-0.18, 0.1, 0.55)
    glColor3f(0.3 * eye_glow, 0.8 * eye_glow, 1.0 * eye_glow)
    self.renderer.draw_sphere(0.08, (0.3, 0.8, 1.0), 12, 8)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.18, 0.1, 0.55)
    glColor3f(0.3 * eye_glow, 0.8 * eye_glow, 1.0 * eye_glow)
    self.renderer.draw_sphere(0.08, (0.3, 0.8, 1.0), 12, 8)
    glPopMatrix()

    # Barba mística
    glPushMatrix()
    glTranslatef(0, -0.4, 0.35)
    glColor3f(0.85, 0.85, 0.85)
    glScalef(1, 1.5, 0.8)
    self.renderer.draw_sphere(0.45, (0.85, 0.85, 0.85), 16, 10)
    glPopMatrix()

    glPopMatrix()

def draw_hat(self):
    """Dibujar sombrero de archimago"""
    glPushMatrix()
    glTranslatef(0, 4.8, 0)
    glRotatef(8, 0, 0, 1)  # Inclinación

    # Sombrero principal
    glColor3f(0.05, 0.05, 0.1)
    self.renderer.draw_cone(0.9, 2.2, 16)

    # Borde del sombrero
    glPushMatrix()
    glTranslatef(0, -0.1, 0)
    glColor3f(0.1, 0.1, 0.2)
    self.renderer.draw_cylinder(1.1, 0.2, 20)
    glPopMatrix()

    # Símbolos mágicos en el sombrero
    glColor3f(1.0, 0.8, 0.0)
    for i in range(8):
        angle = i * math.pi / 4
        glPushMatrix()
        glRotatef(angle * 180 / math.pi, 0, 1, 0)
        glTranslatef(0.7, 0.3 + i * 0.15, 0)
        symbol_glow = 0.8 + math.sin(time * 2 + i) * 0.2
        self.renderer.draw_sphere(0.05, (1.0, 0.8 * symbol_glow, 0), 8, 6)
        glPopMatrix()

    # Estrella en la punta
    glPushMatrix()
    glTranslatef(0.2, 2.0, 0)
    glRotatef(time * 60, 0, 1, 0)
    glColor3f(1.0, 1.0, 0.8)
    self.draw_star(0.15)
    glPopMatrix()

    glPopMatrix()

def draw_arms(self):
    """Dibujar brazos del mago"""
    # Brazo izquierdo
    glPushMatrix()
    glTranslatef(-1.3, 2.8, 0)
    glRotatef(20, 0, 0, 1)

    # Hombro
    glColor3f(0.28, 0.2, 0.83)
    self.renderer.draw_sphere(0.35, (0.28, 0.2, 0.83), 12, 8)

    # Brazo superior
    glTranslatef(0, -0.8, 0)
    glRotatef(15, 0, 0, 1)
    self.renderer.draw_cylinder(0.25, 1.6, 12)

    # Antebrazo
    glTranslatef(0, -1.2, 0)
    glRotatef(10, 0, 0, 1)
    self.renderer.draw_cylinder(0.2, 1.3, 12)

    # Mano
    glTranslatef(0, -1.0, 0)
    glColor3f(1.0, 0.86, 0.67)
    self.renderer.draw_sphere(0.28, (1.0, 0.86, 0.67), 12, 8)

    glPopMatrix()

    # Brazo derecho (con bastón)
    glPushMatrix()
    glTranslatef(1.3, 2.8, 0)
    glRotatef(-20, 0, 0, 1)

    glColor3f(0.28, 0.2, 0.83)
    self.renderer.draw_sphere(0.35, (0.28, 0.2, 0.83), 12, 8)

    glTranslatef(0, -0.8, 0)
    glRotatef(-15, 0, 0, 1)
    self.renderer.draw_cylinder(0.25, 1.6, 12)

    glTranslatef(0, -1.2, 0)
    glRotatef(-10, 0, 0, 1)
    self.renderer.draw_cylinder(0.2, 1.3, 12)

    glTranslatef(0, -1.0, 0)
    glColor3f(1.0, 0.86, 0.67)
    self.renderer.draw_sphere(0.28, (1.0, 0.86, 0.67), 12, 8)

    glPopMatrix()

def draw_legs(self):
    """Dibujar piernas del mago"""
    # Pierna izquierda
    glPushMatrix()
    glTranslatef(-0.5, 0.4, 0)

    # Muslo
    glColor3f(0.28, 0.2, 0.83)
    self.renderer.draw_cylinder(0.35, 1.8, 12)

    # Pantorrilla
    glTranslatef(0, -1.3, 0)
    self.renderer.draw_cylinder(0.28, 1.5, 12)

    # Bota mágica
    glTranslatef(0, -1.2, 0.2)
    glColor3f(0.1, 0.05, 0.2)
    self.renderer.draw_cube(0.35, (0.15, 0.1, 0.25))

    glPopMatrix()

    # Pierna derecha
    glPushMatrix()
    glTranslatef(0.5, 0.4, 0)

    glColor3f(0.28, 0.2, 0.83)
    self.renderer.draw_cylinder(0.35, 1.8, 12)

    glTranslatef(0, -1.3, 0)
    self.renderer.draw_cylinder(0.28, 1.5, 12)

    glTranslatef(0, -1.2, 0.2)
    glColor3f(0.1, 0.05, 0.2)
    self.renderer.draw_cube(0.35, (0.15, 0.1, 0.25))

    glPopMatrix()

def draw_magic_staff(self, time):
    """Dibujar bastón mágico supremo"""
    glPushMatrix()
    glTranslatef(2.4, 2.5, 0)
    glRotatef(-15, 0, 0, 1)

    # Bastón principal
    glColor3f(0.55, 0.27, 0.07)
    self.renderer.draw_cylinder(0.08, 4.2, 16)

    # Anillos decorativos
    glColor3f(1.0, 0.84, 0.0)
    for i in range(4):
        glPushMatrix()
        glTranslatef(0, 0.5 + i * 0.8, 0)
        glRotatef(90, 1, 0, 0)
        self.renderer.draw_cylinder(0.12, 0.06, 12)
        glPopMatrix()

    # Orbe mágico supremo
    glPushMatrix()
    glTranslatef(0, 4.5, 0)

    # Pulso mágico
    orb_scale = 1.0 + math.sin(self.orb_pulse_phase) * 0.2
    glScalef(orb_scale, orb_scale, orb_scale)

    # Orbe principal
    orb_intensity = 0.8 + math.sin(time * 4) * 0.2
    glColor3f(0, 1.0 * orb_intensity, 1.0 * orb_intensity)
    self.renderer.draw_sphere(0.45, (0, 1.0, 1.0), 20, 16)

    # Núcleo brillante
    glColor3f(1.0, 1.0, 1.0)
    self.renderer.draw_sphere(0.2, (1.0, 1.0, 1.0), 12, 10)

    glPopMatrix()

    # Cristales orbitales
    glPushMatrix()
    glTranslatef(0, 4.5, 0)
    glRotatef(self.crystal_rotation, 0, 1, 0)

    for i in range(8):
        angle = i * math.pi / 4
        glPushMatrix()

        orbit_radius = 0.7 + math.sin(time * 2 + i) * 0.1
        glTranslatef(
            math.cos(angle) * orbit_radius,
            math.sin(time * 3 + i) * 0.15,
            math.sin(angle) * orbit_radius
        )

        glRotatef(time * 180 + i * 45, 1, 1, 0)

        # Color del cristal según posición
        hue = i / 8.0
        color = self.renderer.hsv_to_rgb(hue, 1.0, 1.0)
        glColor3f(*color)

        self.renderer.draw_octahedron(0.12)
        glPopMatrix()

    glPopMatrix()

    glPopMatrix()

def draw_aura(self, time):
    """Dibujar aura mágica del mago"""
    glDisable(GL_LIGHTING)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE)

    # Aura base
    glPushMatrix()
    glTranslatef(0, 0, 0)
    glRotatef(self.aura_rotation, 0, 1, 0)

    aura_alpha = 0.3 + math.sin(time * 2) * 0.1
    glColor4f(0.3, 0.7, 1.0, aura_alpha)

    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0, 0.05, 0)
    segments = 32
    for i in range(segments + 1):
        angle = 2 * math.pi * i / segments
        radius = 2.2 + math.sin(angle * 4 + time * 3) * 0.3
        glVertex3f(math.cos(angle) * radius, 0.05, math.sin(angle) * radius)
    glEnd()

    glPopMatrix()

    # Partículas mágicas ascendentes
    for i in range(20):
        glPushMatrix()

        # Posición orbital
        angle = (i / 20.0) * 2 * math.pi + time * 0.5
        radius = 1.5 + math.sin(time * 2 + i) * 0.5
        height = (time * 2 + i) % 8

        glTranslatef(
            math.cos(angle) * radius,
            height,
            math.sin(angle) * radius
        )

        # Color y tamaño de partícula
        particle_alpha = 1.0 - (height / 8.0)
        hue = (i / 20.0 + time * 0.1) % 1.0
        color = self.renderer.hsv_to_rgb(hue, 0.8, 1.0)

        glColor4f(color[0], color[1], color[2], particle_alpha * 0.8)

        size = 0.1 + math.sin(time * 4 + i) * 0.05
        glBegin(GL_QUADS)
        glVertex3f(-size, -size, 0)
        glVertex3f( size, -size, 0)
        glVertex3f( size,  size, 0)
        glVertex3f(-size,  size, 0)
        glEnd()

        glPopMatrix()

    glDisable(GL_BLEND)
    glEnable(GL_LIGHTING)

def draw_star(self, size):
    """Dibujar estrella mágica"""
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

        # Triángulo
        glVertex3f(0, 0, 0)
        glVertex3f(x1, 0, z1)
        glVertex3f(x_mid, 0, z_mid)

        glVertex3f(0, 0, 0)
        glVertex3f(x_mid, 0, z_mid)
        glVertex3f(x2, 0, z2)
    glEnd()

class KnightModel(Character3D):
    """Modelo 3D épico del Paladín Invencible"""

    def __init__(self, renderer):
        super().__init__(renderer)
        self.sword_glow = 0
        self.shield_rotation = 0
        self.plume_sway = 0

    def draw(self, time):
        """Dibujar el modelo completo del caballero"""
        glPushMatrix()

        # Aplicar transformaciones
        glTranslatef(*self.position)
        glRotatef(self.rotation[1], 0, 1, 0)
        glScalef(*self.scale)

        # Actualizar animaciones
        self.sword_glow += 0.04
        self.shield_rotation += 0.5
        self.plume_sway += 0.03

        # Dibujar componentes
        self.draw_body()
        self.draw_head()
        self.draw_helmet(time)
        self.draw_arms()
        self.draw_legs()
        self.draw_sword(time)
        self.draw_shield(time)
        self.draw_aura(time)

        glPopMatrix()

    def draw_body(self):
        """Dibujar cuerpo blindado del caballero"""
        glPushMatrix()
        glTranslatef(0, 1.6, 0)

        # Armadura base
        self.renderer.set_material(
            [0.1, 0.1, 0.15, 1.0],
            [0.4, 0.5, 0.7, 1.0],
            [0.8, 0.8, 0.9, 1.0],
            [80.0]
        )

        glColor3f(0.44, 0.5, 0.78)
        self.renderer.draw_cube(0.9, (0.44, 0.5, 0.78))

        # Pechera decorativa
        glPushMatrix()
        glTranslatef(0, 0.1, 0.85)
        glColor3f(0.25, 0.41, 0.88)
        self.renderer.draw_cube(0.7, (0.25, 0.41, 0.88))
        glPopMatrix()

        # Símbolo sagrado en el pecho
        glPushMatrix()
        glTranslatef(0, 0.3, 1.2)
        glColor3f(1.0, 0.84, 0.0)
        self.renderer.draw_cylinder(0.35, 0.05, 16)

        # Cruz sagrada
        glColor3f(1.0, 1.0, 1.0)
        glBegin(GL_QUADS)
        # Vertical
        glVertex3f(-0.05, -0.25, 0.02)
        glVertex3f( 0.05, -0.25, 0.02)
        glVertex3f( 0.05,  0.25, 0.02)
        glVertex3f(-0.05,  0.25, 0.02)
        # Horizontal
        glVertex3f(-0.2, -0.05, 0.02)
        glVertex3f( 0.2, -0.05, 0.02)
        glVertex3f( 0.2,  0.05, 0.02)
        glVertex3f(-0.2,  0.05, 0.02)
        glEnd()

        glPopMatrix()

        # Detalles de armadura
        glColor3f(1.0, 0.84, 0.0)
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:  # Saltar el centro
                    continue
                glPushMatrix()
                glTranslatef((i-1) * 0.6, (j-1) * 0.6, 0.85)
                self.renderer.draw_sphere(0.06, (1.0, 0.84, 0.0), 8, 6)
                glPopMatrix()

        glPopMatrix()

    def draw_head(self):
        """Dibujar cabeza del caballero"""
        glPushMatrix()
        glTranslatef(0, 3.4, 0)

        # Cabeza
        glColor3f(1.0, 0.86, 0.67)
        self.renderer.draw_sphere(0.65, (1.0, 0.86, 0.67), 20, 16)

        # Ojos determinados
        glPushMatrix()
        glTranslatef(-0.15, 0.1, 0.55)
        glColor3f(0.2, 0.4, 0.8)
        self.renderer.draw_sphere(0.06, (0.2, 0.4, 0.8), 8, 6)
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0.15, 0.1, 0.55)
        glColor3f(0.2, 0.4, 0.8)
        self.renderer.draw_sphere(0.06, (0.2, 0.4, 0.8), 8, 6)
        glPopMatrix()

        glPopMatrix()

    def draw_helmet(self, time):
        """Dibujar casco épico del paladín"""
        glPushMatrix()
        glTranslatef(0, 3.6, 0)

        # Casco base
        self.renderer.set_material(
            [0.1, 0.15, 0.2, 1.0],
            [0.25, 0.41, 0.88, 1.0],
            [0.7, 0.8, 1.0, 1.0],
            [100.0]
        )

        glColor3f(0.25, 0.41, 0.88)
        glBegin(GL_QUAD_STRIP)
        segments = 16
        for i in range(segments + 1):
            angle = math.pi * i / segments
            x = 0.75 * math.sin(angle)
            y = 0.75 * math.cos(angle)
            z_front = 0.4
            z_back = -0.4

            glNormal3f(x, y, 0)
            glVertex3f(x, y, z_front)
            glVertex3f(x, y, z_back)
        glEnd()

        # Visera
        glPushMatrix()
        glTranslatef(0, -0.2, 0.6)
        glColor3f(0.17, 0.25, 0.31)
        self.renderer.draw_cube(0.4, (0.17, 0.25, 0.31))
        glPopMatrix()

        # Pluma heroica
        glPushMatrix()
        glTranslatef(0, 1.3, -0.4)
        plume_sway = math.sin(self.plume_sway) * 8
        glRotatef(plume_sway, 1, 0, 0)

        glColor3f(0.8, 0.1, 0.1)
        glBegin(GL_TRIANGLES)
        for i in range(8):
            angle = i * math.pi / 4
            x1 = 0.05 * math.cos(angle)
            z1 = 0.05 * math.sin(angle)
            x2 = 0.02 * math.cos(angle)
            z2 = 0.02 * math.sin(angle)

            glVertex3f(x1, 0, z1)
            glVertex3f(x2, 1.2, z2)
            glVertex3f(0, 1.5, 0)
        glEnd()

        glPopMatrix()

        # Cuernos decorativos
        glColor3f(1.0, 0.84, 0.0)

        glPushMatrix()
        glTranslatef(-0.4, 0.8, 0)
        glRotatef(-20, 0, 0, 1)
        self.renderer.draw_cone(0.08, 0.6, 8)
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0.4, 0.8, 0)
        glRotatef(20, 0, 0, 1)
        self.renderer.draw_cone(0.08, 0.6, 8)
        glPopMatrix()

        glPopMatrix()

    def draw_arms(self):
        """Dibujar brazos blindados"""
        # Brazo izquierdo
        glPushMatrix()
        glTranslatef(-1.4, 2.8, 0)
        glRotatef(25, 0, 0, 1)

        # Hombrera masiva
        glColor3f(0.25, 0.41, 0.88)
        self.renderer.draw_sphere(0.5, (0.25, 0.41, 0.88), 12, 8)

        # Brazo superior
        glTranslatef(0, -0.9, 0)
        glRotatef(15, 0, 0, 1)
        self.renderer.draw_cylinder(0.3, 1.8, 12)

        # Codo
        glTranslatef(0, -1.0, 0)
        self.renderer.draw_sphere(0.25, (0.25, 0.41, 0.88), 10, 8)

        glTranslatef(0, -0.8, 0)
        glRotatef(-10, 0, 0, 1)
        self.renderer.draw_cylinder(0.25, 1.5, 12)

        glTranslatef(0, -1.0, 0)
        glColor3f(0.17, 0.25, 0.31)
        self.renderer.draw_cube(0.35, (0.17, 0.25, 0.31))

        glPopMatrix()

    def draw_legs(self):
        """Dibujar piernas blindadas"""
        # Pierna izquierda
        glPushMatrix()
        glTranslatef(-0.6, 0.3, 0)

        # Muslo blindado
        glColor3f(0.25, 0.41, 0.88)
        self.renderer.draw_cylinder(0.4, 2.0, 12)

        # Rodillera
        glTranslatef(0, -1.2, 0)
        self.renderer.draw_sphere(0.3, (0.17, 0.25, 0.31), 12, 8)

        # Espinillera
        glTranslatef(0, -0.8, 0)
        self.renderer.draw_cylinder(0.32, 1.6, 12)

        # Bota de acero
        glTranslatef(0, -1.2, 0.3)
        glColor3f(0.17, 0.25, 0.31)
        self.renderer.draw_cube(0.4, (0.17, 0.25, 0.31))

        glPopMatrix()

        # Pierna derecha
        glPushMatrix()
        glTranslatef(0.6, 0.3, 0)

        glColor3f(0.25, 0.41, 0.88)
        self.renderer.draw_cylinder(0.4, 2.0, 12)

        glTranslatef(0, -1.2, 0)
        self.renderer.draw_sphere(0.3, (0.17, 0.25, 0.31), 12, 8)

        glTranslatef(0, -0.8, 0)
        self.renderer.draw_cylinder(0.32, 1.6, 12)

        glTranslatef(0, -1.2, 0.3)
        glColor3f(0.17, 0.25, 0.31)
        self.renderer.draw_cube(0.4, (0.17, 0.25, 0.31))

        glPopMatrix()

    def draw_sword(self, time):
        """Dibujar espada legendaria"""
        glPushMatrix()
        glTranslatef(2.4, 2.5, 0)
        glRotatef(-20, 0, 0, 1)

        # Hoja de la espada
        sword_glow_intensity = 0.8 + math.sin(self.sword_glow) * 0.2

        glPushMatrix()
        glTranslatef(0, 2, 0)
        glScalef(0.2, 3.8, 0.5)

        # Hoja principal
        glColor3f(0.9 * sword_glow_intensity, 0.9 * sword_glow_intensity, 0.95 * sword_glow_intensity)
        self.renderer.draw_cube(1, (0.9, 0.9, 0.95))

        glPopMatrix()

        # Filo mágico brillante
        glPushMatrix()
        glTranslatef(0, 2, 0.26)
        glScalef(0.05, 3.6, 0.1)

        glColor3f(0.3, 0.7, 1.0)
        glDisable(GL_LIGHTING)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE)

        glColor4f(0.3, 0.7, 1.0, 0.8 * sword_glow_intensity)
        self.renderer.draw_cube(1, (0.3, 0.7, 1.0))

        glDisable(GL_BLEND)
        glEnable(GL_LIGHTING)
        glPopMatrix()

        # Guarda ornamentada
        glPushMatrix()
        glTranslatef(0, 0.1, 0)
        glRotatef(90, 0, 0, 1)
        glColor3f(1.0, 0.84, 0.0)
        self.renderer.draw_cylinder(0.15, 1.2, 12)

        # Detalles de la guarda
        for i in range(4):
            glPushMatrix()
            glRotatef(i * 90, 1, 0, 0)
            glTranslatef(0, 0.5, 0)
            self.renderer.draw_sphere(0.08, (1.0, 0.84, 0.0), 8, 6)
            glPopMatrix()

        glPopMatrix()

        # Empuñadura
        glPushMatrix()
        glTranslatef(0, -0.4, 0)
        glColor3f(0.55, 0.27, 0.07)
        self.renderer.draw_cylinder(0.12, 0.8, 16)

        # Envolturas de cuero
        glColor3f(0.4, 0.2, 0.05)
        for i in range(5):
            glPushMatrix()
            glTranslatef(0, -0.3 + i * 0.15, 0)
            glRotatef(90, 1, 0, 0)
            self.renderer.draw_cylinder(0.13, 0.05, 12)
            glPopMatrix()

        glPopMatrix()

        # Pomo con gema
        glPushMatrix()
        glTranslatef(0, -1, 0)
        glColor3f(1.0, 0.84, 0.0)
        self.renderer.draw_sphere(0.18, (1.0, 0.84, 0.0), 12, 8)

        # Gema central
        glColor3f(1.0, 0.2, 0.2)
        gem_glow = 0.8 + math.sin(time * 3) * 0.2
        self.renderer.draw_sphere(0.08, (1.0 * gem_glow, 0.2, 0.2), 8, 6)

        glPopMatrix()

        glPopMatrix()

    def draw_shield(self, time):
        """Dibujar escudo sagrado"""
        glPushMatrix()
        glTranslatef(-2.2, 2.2, 0)
        glRotatef(90, 0, 0, 1)
        glRotatef(self.shield_rotation * 0.1, 0, 1, 0)

        # Base del escudo
        glColor3f(1.0, 0.84, 0.0)
        self.renderer.draw_cylinder(1.1, 0.2, 12)

        # Borde reforzado
        glPushMatrix()
        glColor3f(0.17, 0.25, 0.31)
        glTranslatef(0, 0, 0.1)

        glBegin(GL_QUAD_STRIP)
        segments = 24
        for i in range(segments + 1):
            angle = 2 * math.pi * i / segments
            inner_radius = 1.05
            outer_radius = 1.15

            x_inner = inner_radius * math.cos(angle)
            y_inner = inner_radius * math.sin(angle)
            x_outer = outer_radius * math.cos(angle)
            y_outer = outer_radius * math.sin(angle)

            glNormal3f(0, 0, 1)
            glVertex3f(x_inner, y_inner, 0)
            glVertex3f(x_outer, y_outer, 0)
        glEnd()

        glPopMatrix()

        # Emblema central brillante
        glPushMatrix()
        glTranslatef(0, 0, 0.15)

        emblem_glow = 0.8 + math.sin(time * 2) * 0.2
        glColor3f(1.0, 0.2 * emblem_glow, 0.2 * emblem_glow)
        self.renderer.draw_cylinder(0.4, 0.05, 8)

        # Cruz sagrada brillante
        glColor3f(1.0 * emblem_glow, 1.0 * emblem_glow, 1.0 * emblem_glow)

        # Vertical de la cruz
        glBegin(GL_QUADS)
        glNormal3f(0, 0, 1)
        glVertex3f(-0.08, -0.3, 0.01)
        glVertex3f( 0.08, -0.3, 0.01)
        glVertex3f( 0.08,  0.3, 0.01)
        glVertex3f(-0.08,  0.3, 0.01)
        glEnd()

        # Horizontal de la cruz
        glBegin(GL_QUADS)
        glNormal3f(0, 0, 1)
        glVertex3f(-0.25, -0.08, 0.01)
        glVertex3f( 0.25, -0.08, 0.01)
        glVertex3f( 0.25,  0.08, 0.01)
        glVertex3f(-0.25,  0.08, 0.01)
        glEnd()

        glPopMatrix()

        # Detalles decorativos
        glColor3f(1.0, 0.84, 0.0)
        for i in range(8):
            angle = i * math.pi / 4
            glPushMatrix()
            glTranslatef(
                math.cos(angle) * 0.8,
                math.sin(angle) * 0.8,
                0.12
            )
            self.renderer.draw_sphere(0.05, (1.0, 0.84, 0.0), 6, 4)
            glPopMatrix()

        glPopMatrix()

    def draw_aura(self, time):
        """Dibujar aura heroica del caballero"""
        glDisable(GL_LIGHTING)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE)

        # Aura base dorada
        glPushMatrix()
        glTranslatef(0, 0, 0)
        glRotatef(-self.aura_rotation * 0.5, 0, 1, 0)

        aura_alpha = 0.25 + math.sin(time * 1.5) * 0.1
        glColor4f(1.0, 0.8, 0.2, aura_alpha)

        glBegin(GL_TRIANGLE_FAN)
        glVertex3f(0, 0.05, 0)
        segments = 32
        for i in range(segments + 1):
            angle = 2 * math.pi * i / segments
            radius = 2.4 + math.sin(angle * 6 + time * 2) * 0.2
            glVertex3f(math.cos(angle) * radius, 0.05, math.sin(angle) * radius)
        glEnd()

        glPopMatrix()

        # Rayos de luz sagrada
        for i in range(12):
            glPushMatrix()

            angle = (i / 12.0) * 2 * math.pi + time * 0.3
            distance = 3 + math.sin(time * 2 + i) * 0.5
            height = 1 + math.sin(time * 3 + i) * 0.5

            glTranslatef(
                math.cos(angle) * distance,
                height,
                math.sin(angle) * distance
            )

            glRotatef(angle * 180 / math.pi, 0, 1, 0)

            # Color del rayo
            ray_alpha = 0.6 + math.sin(time * 4 + i) * 0.3
            glColor4f(1.0, 1.0, 0.8, ray_alpha * 0.4)

            # Dibujar rayo como línea vertical brillante
            glBegin(GL_QUADS)
            width = 0.02
            glVertex3f(-width, 0, 0)
            glVertex3f( width, 0, 0)
            glVertex3f( width, 2, 0)
            glVertex3f(-width, 2, 0)
            glEnd()

            glPopMatrix()

        # Partículas de luz ascendentes
        for i in range(15):
            glPushMatrix()

            # Movimiento espiral
            spiral_angle = (time * 0.8 + i * 0.4) % (2 * math.pi)
            radius = 1.2 + i * 0.1
            height = (time * 1.5 + i * 0.3) % 6

            glTranslatef(
                math.cos(spiral_angle) * radius,
                height,
                math.sin(spiral_angle) * radius
            )

            # Color y brillo de partícula
            particle_alpha = 1.0 - (height / 6.0)
            glColor4f(1.0, 0.9, 0.6, particle_alpha * 0.7)

            size = 0.08 + math.sin(time * 5 + i) * 0.03
            glBegin(GL_QUADS)
            glVertex3f(-size, -size, 0)
            glVertex3f( size, -size, 0)
            glVertex3f( size,  size, 0)
            glVertex3f(-size,  size, 0)
            glEnd()

            glPopMatrix()

        glDisable(GL_BLEND)
        glEnable(GL_LIGHTING))

        # Antebrazo
        glTranslatef(0, -0.8, 0)
        glRotatef(10, 0, 0, 1)
        self.renderer.draw_cylinder(0.25, 1.5, 12)

        # Guantelete
        glTranslatef(0, -1.0, 0)
        glColor3f(0.17, 0.25, 0.31)
        self.renderer.draw_cube(0.35, (0.17, 0.25, 0.31))

        glPopMatrix()

        # Brazo derecho (similar)
        glPushMatrix()
        glTranslatef(1.4, 2.8, 0)
        glRotatef(-25, 0, 0, 1)

        glColor3f(0.25, 0.41, 0.88)
        self.renderer.draw_sphere(0.5, (0.25, 0.41, 0.88), 12, 8)

        glTranslatef(0, -0.9, 0)
        glRotatef(-15, 0, 0, 1)
        self.renderer.draw_cylinder(0.3, 1.8, 12)

        glTranslatef(0, -1.0, 0)
        self.renderer.draw_sphere(0.25, (0.25, 0.41, 0.88), 10, 8"""
Modelos 3D épicos de los personajes jugadores
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

        # Animaciones
        self.breathing_phase = 0
        self.hover_phase = 0
        self.aura_rotation = 0

        # Estados
        self.is_animating = False
        self.animation_type = None

    def update_animation(self, time):
        """Actualizar animaciones del personaje"""
        self.breathing_phase += 0.02
        self.hover_phase += 0.015
        self.aura_rotation += 1.5

        # Respiración sutil
        self.position[1] = math.sin(self.breathing_phase) * 0.03

        # Rotación sutil
        self.rotation[1] = math.sin(time * 0.3) * 3

class MageModel(Character3D):
    """Modelo 3D épico del Archimago Supremo"""

    def __init__(self, renderer):
        super().__init__(renderer)
        self.orb_pulse_phase = 0
        self.crystal_rotation = 0
        self.cape_wave = 0

    def draw(self, time):
        """