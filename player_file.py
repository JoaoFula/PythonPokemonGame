import pygame
import config

class player_class:
    def __init__(self, x_position, y_position):
        print("Player created")
        self.position = [x_position, y_position]

    def update(self):
        print("Player updated")

    def update_position(self):


    def render(self, screen):
        pygame.draw.rect(screen, config.WHITE, (self.position[0]*config.SCALE,
                                                self.position[1]*config.SCALE,
                                                config.SCALE,
                                                config.SCALE), 2)