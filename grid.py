import pygame
import time
from tile import Tile

class Grid:
    def __init__(self, screen, grid_size, tile_size, offset_x, offset_y):
        self.screen = screen
        self.grid_size = grid_size
        self.tile_size = tile_size
        self.offset_x = offset_x
        self.offset_y = offset_y

        self.tiles = []
        for y in range(self.grid_size):
            row = []
            for x in range(self.grid_size):
                tile_x = self.offset_x + x * self.tile_size
                tile_y = self.offset_y + y * self.tile_size
                row.append(Tile(tile_x, tile_y, self.tile_size))
            self.tiles.append(row)

    def handle_event(self, event, selected_action):
        gained_points = 0

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            for row in self.tiles:
                for tile in row:
                    if tile.rect.collidepoint(x, y):
                        if selected_action == "Piantare" and tile.state == 0:
                            tile.plant()
                        elif selected_action == "Distruggere" and tile.state != 0:
                            tile.harvest()
                        elif selected_action == "Raccogliere" and tile.state == 3:
                            tile.harvest()
                            gained_points += 10
                        elif tile.ready:
                            '''
                            tile.harvest()
                            gained_points += 10
                            '''

        return gained_points

    def update(self):
        for row in self.tiles:
            for tile in row:
                tile.update()

    def draw(self):
        for row in self.tiles:
            for tile in row:
                tile.draw(self.screen)
