import pygame
from button import Button
import colors
import config as c

class Image_button(Button):
    def __init__(self, x, y, w, h, image, on_click=lambda x: None, padding=0):
        super().__init__(x, y, w, h, "")
        self.state = 'normal'
        self.on_click = on_click
        self.image = pygame.image.load(image)
        self.num = int(image.split(".")[0].split("/")[1].split("_")[1])


    @property
    def back_color(self):
        return dict(normal=c.button_normal_back_color,
                    hover=colors.YELLOW1,
                    pressed=colors.WHITE)[self.state]

    def draw(self, surface):
        bounds = self.bounds
        pygame.draw.rect(surface, self.back_color, pygame.Rect(bounds.x - 1, bounds.y - 1, bounds.width + 3, bounds.height + 2))
        surface.blit(self.image, self.bounds)
