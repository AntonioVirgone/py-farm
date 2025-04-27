import pygame

class Button:
    def __init__(self, x, y, width, height, text, on_click=None, font_size=24):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.on_click = on_click

        self.color_idle = (200, 200, 200)
        self.color_hover = (170, 170, 170)

        self.font = pygame.font.SysFont(None, font_size)
        self.hovered = False

    def draw(self, screen):
        color = self.color_hover if self.hovered else self.color_idle
        pygame.draw.rect(screen, color, self.rect)

        text_surface = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos) and self.on_click:
                self.on_click()
