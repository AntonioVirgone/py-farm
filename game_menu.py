import pygame
from button import Button

class GameMenu:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.selected_action = None
        self.selected_plant = "Carota"

        self.buttons = []
        self.plant_list = ["Carota", "Pomodoro", "Zucca"]
        self.create_buttons()

    def create_buttons(self):
        self.buttons.append(Button(20, 20, 100, 40, "Piantare", self.select_planting))
        self.buttons.append(Button(140, 20, 100, 40, "Distruggere", self.select_destroy))

    def select_planting(self):
        self.selected_action = "plant"

    def select_destroy(self):
        self.selected_action = "destroy"

    def draw(self, points, harvest_counts):
        pygame.draw.rect(self.screen, (180, 180, 180), (0, 0, self.width, self.height))

        for button in self.buttons:
            button.draw(self.screen)

        font = pygame.font.SysFont(None, 24)
        points_text = font.render(f"Punti: {points}", True, (0, 0, 0))
        self.screen.blit(points_text, (self.width - 200, 10))

        # Mostra il tipo di pianta selezionata
        selected_plant_text = font.render(f"Pianta: {self.selected_plant}", True, (0, 0, 0))
        self.screen.blit(selected_plant_text, (self.width - 200, 40))

    def handle_event(self, event):
        for button in self.buttons:
            button.handle_event(event)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                self.selected_plant = "Carota"
            elif event.key == pygame.K_2:
                self.selected_plant = "Pomodoro"
            elif event.key == pygame.K_3:
                self.selected_plant = "Zucca"
