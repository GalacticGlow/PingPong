import pygame
import os
pygame.init()

BG = (69, 69, 69)
MW_W, MW_H = 600, 500
mw = pygame.display.set_mode((MW_W, MW_H))
clock = pygame.time.Clock()

file_name = lambda filename: os.path.join(os.path.abspath(__file__+'/..'), filename)
bg = pygame.transform.scale(pygame.image.load(file_name('background.jpg')), (MW_W, MW_H))

play = True
game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    mw.blit(bg, (0, 0))
    pygame.display.update()
    clock.tick(69)