import pygame
import config

class player_class:
    def __init__(self, x_position, y_position):
        print("Player created")
        self.position = [x_position, y_position]
        self.image = pygame.image.load("imgs/player_down.png")
        self.image = pygame.transform.scale(self.image, (config.SCALE, config.SCALE))
        self.rect = pygame.Rect(self.position[0]*config.SCALE,
                                self.position[1]*config.SCALE,
                                config.SCALE,
                                config.SCALE)

    def update(self):
        print("Player updated")

    def update_position(self, x_change, y_change):
        self.position[0] += x_change
        self.position[1] += y_change
        self.rect = pygame.Rect(self.position[0]*config.SCALE,
                                self.position[1]*config.SCALE,
                                config.SCALE,
                                config.SCALE)

    def render(self, screen):
        screen.blit(self.image, self.rect)
