from player_file import player_class
from game_state_file import game_state_class
import pygame


class game:
    def __init__(self, screen):
        self.screen = screen
        self.objects = []
        self.game_state = game_state_class.NONE

    def set_up(self):
        player = player_class(1,1)
        self.player = player
        self.objects.append(player)
        print("Setup")
        self.game_state = game_state_class.RUNNING

    def update(self):
        print("update")
        self.handle_events()
        for object in self.objects:
            object.render(self, self.screen)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state = game_state_class.ENDED
            # handle key events
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_state = game_state_class.ENDED
                elif event.key == pygame.K_w: # up
                    self.player.update_position(0, -1)
                elif event.key == pygame.K_s: # down
                    self.player.update_position(0, 1)
                elif event.key == pygame.K_a: # left
                    self.player.update_position(-1, 0)
                elif event.key == pygame.K_d: # right
                    self.player.update_position(1, 0)