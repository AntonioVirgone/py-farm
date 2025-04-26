import pygame

class GameMenu:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.rect = pygame.Rect(0, 0, width, height)
        self.font = pygame.font.SysFont('Arial', 24)

        self.buttons = []
        self.selected_action = None
        self.create_buttons()

    def create_buttons(self):
        actions = ["Piantare", "Distruggere", "Raccogliere"]
        for i, action in enumerate(actions):
            btn_width, btn_height = 150, 40
            x = 20 + i * (btn_width + 20)
            y = (self.height - btn_height) // 2
            rect = pygame.Rect(x, y, btn_width, btn_height)
            self.buttons.append((rect, action))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if self.rect.collidepoint(x, y):
                for rect, action in self.buttons:
                    if rect.collidepoint(x, y):
                        self.selected_action = action
                        print(f"Azione selezionata: {action}")

    def draw(self, points):
        pygame.draw.rect(self.screen, (180, 180, 180), self.rect)

        for rect, text in self.buttons:
            color = (0, 0, 255) if self.selected_action == text else (100, 100, 255)
            pygame.draw.rect(self.screen, color, rect)
            label = self.font.render(text, True, (255, 255, 255))
            label_rect = label.get_rect(center=rect.center)
            self.screen.blit(label, label_rect)

        points_label = self.font.render(f"Punti: {points}", True, (0, 0, 0))
        self.screen.blit(points_label, (self.width - 150, 30))
