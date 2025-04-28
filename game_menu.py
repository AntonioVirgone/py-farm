import pygame
from button import Button
from button_color import ButtonColor
from plant import Plant


class GameMenu:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.selected_action = None
        self.selected_plant = "Carota"

        self.buttons = []
        self.plant_buttons = []

        carota = Plant("Carota", ButtonColor((255, 204, 153), (255, 178, 102), (255, 153, 51)), "common", 10, 25, 3, 6)
        pomodoro = Plant("Pomodoro", ButtonColor((255, 153, 153), (255, 102, 102), (255, 51, 51)), "common", 20, 40, 3, 14)
        zucca = Plant("Zucca", ButtonColor((204, 255, 153), (178, 255, 102), (51, 255, 51)), "common", 50, 150, 2, 20)

        self.plant_list = [carota, pomodoro, zucca]
        self.create_buttons()

    def create_buttons(self):
        # Azioni principali
        self.buttons.append(Button(20, 20, 100, 40, "Piantare", self.select_planting))
        self.buttons.append(Button(140, 20, 100, 40, "Distruggere", self.select_destroy))

        # Bottoni per selezionare le piante
        start_x = 260
        for idx, plant in enumerate(self.plant_list):
            btn = Button(start_x + idx * 110, 20, 100, 40, plant.name, lambda p=plant: self.select_plant(p.name), base_color=plant.color.base_color, hover_color=plant.color.hover_color, click_color=plant.color.click_color)
            self.plant_buttons.append(btn)

    def select_planting(self):
        self.selected_action = "plant"

    def select_destroy(self):
        self.selected_action = "destroy"

    def select_plant(self, plant_name):
        self.selected_plant = plant_name

    def draw(self, points, harvest_counts):
        pygame.draw.rect(self.screen, (180, 180, 180), (0, 0, self.width, self.height))

        for button in self.buttons:
            button.draw(self.screen)

        for button in self.plant_buttons:
            button.draw(self.screen)

        font = pygame.font.SysFont(None, 24)
        points_text = font.render(f"Punti: {points}", True, (0, 0, 0))
        self.screen.blit(points_text, (self.width - 200, 10))

        selected_plant_text = font.render(f"Pianta: {self.selected_plant}", True, (0, 0, 0))
        self.screen.blit(selected_plant_text, (self.width - 200, 40))

    def handle_event(self, event):
        for button in self.buttons + self.plant_buttons:
            button.handle_event(event)
