from PIL import Image
import PIL
import pygame


class sprite_sheet_reader:

    def __init__(self, imageName, tileSize):
        self.spritesheet = Image.open(imageName)
        self.tileSize = tileSize
        self.margin = 1

    def get_tile(self, tileX, tileY):
        posX = (self.tileSize * tileX) + (self.margin * (tileX + 1))
        posY = (self.tileSize * tileY) + (self.margin * (tileY + 1))
        box = (posX, posY, posX + self.tileSize, posY + self.tileSize)
        tile2 = self.spritesheet.crop(box)
        tile2 = tile2.resize((32,32), PIL.Image.ANTIALIAS)
        mode = tile2.mode
        size = tile2.size

        data = tile2.tobytes()
        tile1 = pygame.image.fromstring(data, size, mode)

        return tile1



