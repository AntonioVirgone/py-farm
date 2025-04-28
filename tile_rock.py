import pygame
from tile import Tile

class TileRock(Tile):
    def __init__(self, x, y, size, offset_x, offset_y):
        super().__init__(x, y, size, offset_x, offset_y)
        self.state = 1

    def destroy(self):
        if self.state == 1:
            self.state = 0
            return True
        return False

    def harvest(self):
        return None

    def update(self):
        pass

    def draw(self, screen):
        color = (100, 100, 100) if self.state == 1 else (220, 220, 220)
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 1)
