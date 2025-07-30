# Añadir métodos faltantes:
def draw_cone(self, radius=1.0, height=2.0, slices=16):
    """Dibujar cono"""
    quadric = gluNewQuadric()
    gluQuadricNormals(quadric, GLU_SMOOTH)

    if self.wireframe_mode:
        gluQuadricDrawStyle(quadric, GLU_LINE)
    else:
        gluQuadricDrawStyle(quadric, GLU_FILL)

    gluCylinder(quadric, radius, 0, height, slices, 1)

    # Base del cono
    glPushMatrix()
    glRotatef(180, 1, 0, 0)
    gluDisk(quadric, 0, radius, slices, 1)
    glPopMatrix()

    gluDeleteQuadric(quadric)

def set_material(self, ambient, diffuse, specular, shininess):
    """Establecer material"""
    glMaterialfv(GL_FRONT, GL_AMBIENT, ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, shininess)

def draw_cone(self, radius=1.0, height=2.0, slices=16):
    """Dibujar cono épico"""
    quadric = gluNewQuadric()
    gluQuadricNormals(quadric, GLU_SMOOTH)

    if self.wireframe_mode:
        gluQuadricDrawStyle(quadric, GLU_LINE)
    else:
        gluQuadricDrawStyle(quadric, GLU_FILL)

    # Cono principal
    gluCylinder(quadric, radius, 0, height, slices, 1)

    # Base del cono
    glPushMatrix()
    glRotatef(180, 1, 0, 0)
    gluDisk(quadric, 0, radius, slices, 1)
    glPopMatrix()

    gluDeleteQuadric(quadric)

def set_material(self, ambient, diffuse, specular, shininess):
    """Establecer material para efectos de iluminación"""
    glMaterialfv(GL_FRONT, GL_AMBIENT, ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, shininess)

def hsv_to_rgb(self, h, s, v):
    """Convertir HSV a RGB para efectos de color"""
    import colorsys
    return colorsys.hsv_to_rgb(h, s, v)

def draw_octahedron(self, size=1.0):
    """Dibujar octaedro para cristales mágicos"""
    vertices = [
        ( 0,  size,  0),  # Top
        ( size,  0,  0),  # Right
        ( 0,  0,  size),  # Front
        (-size,  0,  0),  # Left
        ( 0,  0, -size),  # Back
        ( 0, -size,  0)   # Bottom
    ]

    faces = [
        (0, 1, 2), (0, 2, 3), (0, 3, 4), (0, 4, 1),  # Top faces
        (5, 2, 1), (5, 3, 2), (5, 4, 3), (5, 1, 4)   # Bottom faces
    ]

    glBegin(GL_TRIANGLES)
    for face in faces:
        for vertex_idx in face:
            vertex = vertices[vertex_idx]
            # Calculate normal (pointing outward from center)
            normal = [v/size for v in vertex]
            glNormal3f(*normal)
            glVertex3f(*vertex)
    glEnd()