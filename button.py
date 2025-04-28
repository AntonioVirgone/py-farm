import pygame


class Button:
    def __init__(self, x, y, width, height, text,
                 on_click=None,
                 font_size=24,
                 base_color=(100, 200, 100),
                 hover_color=(70, 170, 70),
                 click_color=(50, 150, 50)):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.on_click = on_click

        self.hovered = False
        self.clicked = False

        self.font = pygame.font.SysFont(None, font_size)

        self.base_color = base_color
        self.hover_color = hover_color
        self.click_color = click_color

    def draw(self, screen):
        if self.clicked:
            color = self.click_color
        elif self.hovered:
            color = self.hover_color
        else:
            color = self.base_color

        pygame.draw.rect(screen, color, self.rect, border_radius=8)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2, border_radius=8)

        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        mouse_pos = pygame.mouse.get_pos()
        self.hovered = self.rect.collidepoint(mouse_pos)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.hovered:
                self.clicked = True

        if event.type == pygame.MOUSEBUTTONUP:
            if self.clicked and self.hovered:
                self.on_click()
            self.clicked = False
