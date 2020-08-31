from player_file import player_class
from game_state_file import game_state_class
import pygame
import config


class game:
    def __init__(self, screen):
        self.screen = screen
        self.objects = []
        self.game_state = game_state_class.NONE
        self.map = []

    def set_up(self):
        player = player_class(1,1)
        self.player = player
        self.objects.append(player)
        print("Setup")
        self.game_state = game_state_class.RUNNING
        self.load_map("01")


    def update(self):
        # temporary screen clearence
        self.screen.fill(config.BLACK)
        print("update")
        self.handle_events()
        self.render_map(self.screen)
        for object in self.objects:
            object.render(self.screen)


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

    def load_map(self, file_name):
        with open('maps/'+file_name+'.txt') as map_file:
            for line in map_file:
                tiles=[]
                for i in range(0, len(line)-1, 2):
                    tiles.append(line[i])
                self.map.append(tiles)



    def render_map(self, screen):
        y_pos = 0
        for line in self.map:
            x_pos = 0
            for tile in line:
                image = map_tile_image[tile]
                rect = pygame.Rect(x_pos*config.SCALE,
                                y_pos*config.SCALE,
                                config.SCALE,
                                config.SCALE)
                screen.blit(image, rect)
                x_pos += 1
            y_pos += 1


map_tile_image = {
    "G": pygame.image.load("imgs/grass1.png"),
    "W": pygame.image.load("imgs/water.png")
}