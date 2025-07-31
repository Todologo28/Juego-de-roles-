import pygame
import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from data.game_data import GameState, PlayerData

class GameEngine:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800), pygame.DOUBLEBUF | pygame.OPENGL)
        pygame.display.set_caption("RPG 3D Epico")
        self.running = True
        self.game_state = GameState.CHARACTER_SELECT
        self.player_data = PlayerData()
        
        glEnable(GL_DEPTH_TEST)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, 1200/800, 0.1, 100.0)
        
        print("Motor inicializado correctamente")
        print("Controles: 1=Mago, 2=Caballero, ESC=Salir")

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("Saliendo del juego...")
                    self.running = False
                elif event.key == pygame.K_1:
                    print("Has elegido al Mago Epico!")
                    print("Maestro de las artes arcanas")
                    pygame.time.wait(2000)
                    self.running = False
                elif event.key == pygame.K_2:
                    print("Has elegido al Caballero Valiente!")
                    print("Guerrero sagrado de honor")
                    pygame.time.wait(2000)
                    self.running = False

    def render(self):
        glClearColor(0.1, 0.1, 0.4, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(5, 5, 10, 0, 0, 0, 0, 1, 0)
        
        glPushMatrix()
        glRotatef(pygame.time.get_ticks() * 0.1, 1, 1, 0)
        
        glColor3f(1.0, 0.8, 0.2)
        glBegin(GL_QUADS)
        glVertex3f(-1, -1, 1)
        glVertex3f(1, -1, 1)
        glVertex3f(1, 1, 1)
        glVertex3f(-1, 1, 1)
        glVertex3f(-1, -1, -1)
        glVertex3f(-1, 1, -1)
        glVertex3f(1, 1, -1)
        glVertex3f(1, -1, -1)
        glEnd()
        
        glPopMatrix()
        pygame.display.flip()

    def run(self):
        print("=" * 50)
        print("ELIGE TU DESTINO")
        print("=" * 50)
        print("1 - ARCHIMAGO SUPREMO")
        print("    Maestro de las artes arcanas elementales")
        print()
        print("2 - PALADIN INVENCIBLE")
        print("    Guerrero sagrado de honor inquebrantable")
        print("=" * 50)
        print("Presiona 1 o 2 para seleccionar")
        print("ESC para salir")
        print("=" * 50)
        
        clock = pygame.time.Clock()
        while self.running:
            self.handle_events()
            self.render()
            clock.tick(60)
        
        pygame.quit()
        print("Gracias por probar RPG 3D Epico!")
