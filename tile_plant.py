import pygame
import time
from tile import Tile

class TilePlant(Tile):
    def __init__(self, x, y, size, offset_x, offset_y):
        super().__init__(x, y, size, offset_x, offset_y)
        self.state = 0
        self.timer = 0
        self.plant_type = None

    def plant(self, plant_type):
        if self.state == 0:
            self.state = 1
            self.timer = time.time()
            self.plant_type = plant_type

    def harvest(self):
        if self.state == 3:
            self.state = 0
            return self.plant_type
        return None

    def update(self):
        if self.state in [1, 2]:
            if time.time() - self.timer > 5:
                self.state += 1
                self.timer = time.time()

    def draw(self, screen):
        if self.plant_type is None:
            color = (153, 76, 0)
        else:
            color = self.plant_type.color.base_color \
                if (self.state == 1 and (self.plant_type is not None)) else self.plant_type.color.hover_color \
                if (self.state == 2 and (self.plant_type is not None)) else self.plant_type.color.click_color \
                if (self.state == 3 and (self.plant_type is not None)) else (153, 76, 0)


        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 1)
