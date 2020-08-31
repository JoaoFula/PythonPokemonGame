import pygame
import config
from game_file import game
from game_state_file import game_state_class


pygame.init()
screen = pygame.display.set_mode([config.SCREEN_WIDTH, config.SCREEN_HEIGHT])

pygame.display.set_caption("Pokemon Clone")

clock = pygame.time.Clock()
game = game(screen)
game.set_up()

while game.game_state == game_state_class.RUNNING:
    clock.tick(50)
    game.update()
    pygame.display.flip()
