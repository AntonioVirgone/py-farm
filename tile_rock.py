import pygame
import time

class TileRock:
    def __init__(self, x, y, size):
        self.rect = pygame.Rect(x, y, size, size)
        self.state = 0  # 0 = rock, 1 = working, 2 = destroy, 3 = remove
        self.timer_start = None
        self.ready = False

    def working(self):
        self.state = 1
        self.timer_start = time.time()
        self.ready = False

    def destroy(self):
        self.state = 2
        self.timer_start = None
        self.ready = False

    def update(self):
        if self.timer_start:
            elapsed = time.time() - self.timer_start
            if elapsed > 15:
                self.state = 3
                self.ready = True
            elif elapsed > 7:
                self.state = 2

    def draw(self, surface):
        colors = {
            0: (128, 128, 128),  # rock
            1: (192, 192, 192),  # working
            2: (224, 224, 224),  # destroy
            3: (102, 51, 0),      # remove
        }
        pygame.draw.rect(surface, colors[self.state], self.rect)
        pygame.draw.rect(surface, (0, 0, 0), self.rect, 1)  # bordo nero
