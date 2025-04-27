import pygame
import random
from tile_plant import TilePlant
from tile_rock import TileRock

class Grid:
    def __init__(self, screen, size, tile_size, offset_x, offset_y):
        self.screen = screen
        self.size = size
        self.tile_size = tile_size
        self.offset_x = offset_x
        self.offset_y = offset_y

        self.tiles = []
        self.create_tiles()

    def create_tiles(self):
        for y in range(self.size):
            row = []
            for x in range(self.size):
                if random.random() < 0.2:  # 20% possibilità di spawnare una roccia
                    row.append(TileRock(x, y, self.tile_size, self.offset_x, self.offset_y))
                else:
                    row.append(TilePlant(x, y, self.tile_size, self.offset_x, self.offset_y))
            self.tiles.append(row)

    def update(self):
        for row in self.tiles:
            for tile in row:
                tile.update()

    def draw(self):
        for row in self.tiles:
            for tile in row:
                tile.draw(self.screen)

    def handle_event(self, event, action, selected_plant):
        points = 0
        harvest = None

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            for row in self.tiles:
                for tile in row:
                    if tile.rect.collidepoint(mx, my):
                        if isinstance(tile, TilePlant) and action == "plant":
                            tile.plant(selected_plant)
                        elif isinstance(tile, TileRock) and action == "destroy":
                            if tile.destroy():
                                # Roccia distrutta -> sostituire con TilePlant vuoto
                                ix, iy = tile.grid_pos
                                self.tiles[iy][ix] = TilePlant(ix, iy, self.tile_size, self.offset_x, self.offset_y)
                        result = tile.harvest()
                        if result:
                            points += 10
                            harvest = result
        return points, harvest
