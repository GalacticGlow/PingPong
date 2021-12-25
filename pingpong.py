import pygame
import os
pygame.init()

BG = (69, 69, 69)
MW_W, MW_H = 600, 500
mw = pygame.display.set_mode((MW_W, MW_H))
mw.fill(BG)
clock = pygame.time.Clock()



play = True
game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    mw.fill(BG)
    pygame.display.update()
    clock.tick(69)