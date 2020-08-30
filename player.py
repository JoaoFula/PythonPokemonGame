import pygame
import config

class Player:
    def __init__(self):
        print("Player created")

    def update(self):
        print("Player updated")

    def render(self, screen):
        pygame.draw.rect(screen, config.WHITE, (10, 10, 10, 10), 2)