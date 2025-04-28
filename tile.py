import pygame

class Tile:
    def __init__(self, x, y, size, offset_x, offset_y):
        self.grid_pos = (x, y)
        self.size = size
        self.offset_x = offset_x
        self.offset_y = offset_y

        self.rect = pygame.Rect(
            offset_x + x * size,
            offset_y + y * size,
            size, size
        )
