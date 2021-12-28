import pygame
import os
from random import randint
pygame.init()

GREEN = (0, 255, 51)
DARK_BLUE = (0, 0, 100)

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

class Outcome():
    def __init__(self, w, h):
        self.rect = pygame.Rect(0, 0, w, h)
        self.rect.center = (MW_W//2, MW_H//2)
        self.font = pygame.font.SysFont('Arial', 69)
        self.font2 = pygame.font.SysFont('Arial', 30)
        self.text_lose1 = self.font.render('Игрок 1 выиграл!!!', True, GREEN)
        self.text_lose2 = self.font.render('Игрок 2 выиграл!!!', True, GREEN)
        self.text_restart = self.font2.render('R - начать сначала', True, GREEN)
        self.lose1_rect = self.text_lose1.get_rect(center=(MW_W//2, MW_H//2))
        self.lose2_rect = self.text_lose2.get_rect(center=(MW_W//2, MW_H//2))
        self.restart_rect = self.text_restart.get_rect(center=(MW_W//2, MW_H//2+60))        
    def lose1(self):
        pygame.draw.rect(mw, DARK_BLUE, self.rect)
        mw.blit(self.text_lose1, (self.lose1_rect))
        mw.blit(self.text_restart, (self.restart_rect))
    def lose2(self):
        pygame.draw.rect(mw, DARK_BLUE, self.rect)
        mw.blit(self.text_lose2, (self.lose2_rect))
        mw.blit(self.text_restart, (self.restart_rect))     

player1 = Player(0, 0)
player2 = Player(MW_W - player1.rect.width + 15, MW_H - player1.rect.height + 15)
ball = Ball(MW_W/2, randint(100, MW_H - 100))
outcome = Outcome(500, 200)
play = True
game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                ball.rect.x = MW_W/2
                ball.rect.y = randint(100, MW_H - 100)
                player1.rect.x = 0
                player1.rect.y = 0
                player2.rect.x = MW_W - player1.rect.width + 15
                player2.rect.y = MW_H - player1.rect.height + 15
                ball.speed_x = 3
                ball.speed_y = 3
                play = True

    if play:
        mw.blit(bg, (0, 0))
        if ball.rect.x <= 0:
            outcome.lose2()
            play = False
        if ball.rect.x + 45 >= MW_W:
            outcome.lose1()
            play = False
        if ball.rect.y + 45 >= MW_H or ball.rect.y <= 0:
            ball.speed_y = -ball.speed_y
        if ball.colliderect(player1) or ball.colliderect(player2):
            ball.speed_x = -ball.speed_x
        player1.update_L()
        player2.update_R()
        ball.update()
    pygame.display.update()
    clock.tick(69)