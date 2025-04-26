import pygame
import time

class Tile:
    def __init__(self, x, y, size):
        self.rect = pygame.Rect(x, y, size, size)
        self.state = 0  # 0 = vuoto, 1 = piantato, 2 = crescita, 3 = maturo
        self.timer_start = None
        self.ready = False

    def plant(self):
        self.state = 1
        self.timer_start = time.time()
        self.ready = False

    def harvest(self):
        self.state = 0
        self.timer_start = None
        self.ready = False

    def update(self):
        if self.timer_start:
            elapsed = time.time() - self.timer_start
            if elapsed > 10:
                self.state = 3
                self.ready = True
            elif elapsed > 5:
                self.state = 2

    def draw(self, surface):
        colors = {
            0: (153, 76, 0),  # vuoto
            1: (100, 255, 100),  # piantato
            2: (50, 200, 50),    # crescita
            3: (0, 150, 0),      # maturo
        }
        pygame.draw.rect(surface, colors[self.state], self.rect)
        pygame.draw.rect(surface, (0, 0, 0), self.rect, 1)  # bordo nero
