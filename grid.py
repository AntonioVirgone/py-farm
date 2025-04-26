import random

import pygame
from tile import Tile
from tile_rock import TileRock


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
                # --- Aggiungiamo casualmente le rocce! ---
                if random.random() < 0.1:  # 10% di probabilità di avere una roccia
                    row.append(TileRock(tile_x, tile_y, self.tile_size))
                else:
                    row.append(Tile(tile_x, tile_y, self.tile_size))
            self.tiles.append(row)

    def handle_event(self, event, selected_action):
        gained_points = 0

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            for i, row in enumerate(self.tiles):
                for j, tile in enumerate(row):
                    if tile.rect.collidepoint(x, y):
                        # --- Se è una roccia ---
                        if isinstance(tile, TileRock):
                            if selected_action == "Piantare" and tile.state == 0:
                                tile.working()
                            if selected_action == "Distruggere" and tile.state == 3:
                                # Sostituisci dinamicamente la roccia con un Tile normale
                                tile_x = tile.rect.x
                                tile_y = tile.rect.y
                                self.tiles[i][j] = Tile(tile_x, tile_y, self.tile_size)
                                print(f"Roccia distrutta a ({i},{j}), sostituita con terreno libero!")

                        # --- Se è un terreno normale ---
                        else:
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
