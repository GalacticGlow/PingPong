import pygame
import os
from random import randint
pygame.init()

BG = (69, 69, 69)
MW_W, MW_H = 600, 500
mw = pygame.display.set_mode((MW_W, MW_H))
clock = pygame.time.Clock()

file_name = lambda filename: os.path.join(os.path.abspath(__file__+'/..'), filename)
bg = pygame.transform.scale(pygame.image.load(file_name('background.jpg')), (MW_W, MW_H))

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y, w, h):
        super().__init__()
        self.rect = pygame.Rect(x, y, w, h)
        self.image = pygame.image.load(file_name(image))
    def show(self):
        mw.blit(self.image, self.rect)

class Player(GameSprite):
    def __init__(self, x, y):
        super().__init__('platform.png', x, y, 50, 150)
        self.speed = 3
    def update_L(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.y - self.speed > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.y + self.speed < MW_H - self.rect.height + 15:
            self.rect.y += self.speed
        self.show()
    def update_R(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y - self.speed > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y + self.speed < MW_H - self.rect.height + 15:
            self.rect.y += self.speed
        self.show()
    def collidepoint(self, x,y):
        return self.rect.collidepoint(x,y)
    def colliderect(self, rect):
        return self.rect.colliderect(rect)
    
class Ball(GameSprite):
    def __init__(self, x, y):
        super().__init__('ballz.png', x, y, 50, 50)
        self.speed_x, self.speed_y = 3, 3
        self.image = pygame.transform.scale(pygame.image.load(file_name('ballz.png')), (45, 45))
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        self.show()
    def colliderect(self, rect):
        return self.rect.colliderect(rect)

player1 = Player(0, 0)
player2 = Player(MW_W - player1.rect.width + 15, MW_H - player1.rect.height + 15)
ball = Ball(100, 100)
play = True
game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    if play:
        if ball.rect.x <= 0 or ball.rect.x + 45 >= MW_W:
            play = False
        elif ball.rect.y + 45 >= MW_H or ball.rect.y <= 0:
            ball.speed_y = -ball.speed_y
        elif ball.colliderect(player1) or ball.colliderect(player2):
            ball.speed_x = -ball.speed_x
        mw.blit(bg, (0, 0))
        player1.update_L()
        player2.update_R()
        ball.update()
    pygame.display.update()
    clock.tick(69)