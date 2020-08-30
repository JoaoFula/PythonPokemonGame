import pygame
import config
from game import Game

pygame.init()

screen = pygame.display.set_mode([600, 400])

pygame.display.set_caption("Pokemon Clone")

game = Game(screen)
game.set_up()
while True:
    game.update()
    pygame.display.flip()
