import pygame
from pygame.locals import *

pygame.init()


screen_width = 725
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

rows = 6
cols = 6


pygame.display.set_caption("Brick Breaker")
icon = pygame.image.load('brick.png')
pygame.display.set_icon(icon)

#Speed the game runs at
FPS = 60
clock = pygame.time.Clock()

red_brick = pygame.image.load('Red_brick.png')
green_brick = pygame.image.load('Green_brick.png')
blue_brick = pygame.image.load('Blue_brick .png')

playerImg = pygame.image.load('platform.png')
playerX = 300
playerY = 400


def player(x):
  screen.blit(playerImg, (x, playerY))

ball_radius = 10

class Ball:
    VEL = 5
    def __init__(self, x, y, radius, colour):
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = colour
        self.rect = Rect(self.x, self.y, ball_radius * 2, ball_radius * 2)
        self.x_vel = 5
        self.y_vel = -self.VEL

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel
    def set_vel(self, x_vel, y_vel):
        self.x_vel = x_vel
        self.y_vel = y_vel
    def draw(self):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.radius)
    def ball_paddle_collide(self, ):
        if self.rect.colliderect(player(playerX)):
            ball.set_vel(ball.x_vel, ball.y_vel * -1)



iballX = screen_width/2 - ball_radius
iballY = playerY + 31
ball = Ball(iballX, iballY, ball_radius, (0, 0, 0))

def ball_col(ball):
    if ball.x - ball_radius <= 0 or ball.x + ball_radius >= screen_width - 10:
        ball.set_vel(ball.x_vel * -1, ball.y_vel)
    if ball.y + ball.radius >= screen_height or ball.y - ball.radius <= 0:
        ball.set_vel(ball.x_vel, ball.y_vel * -1)



        
     

       
       
player(playerX)
running = False
while running == False:
    screen.fill((245, 245, 220))
    player(playerX)
    ball.draw()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            running = True
    clock.tick(FPS)
    pygame.display.update()
  
while running:
    screen.fill((245, 245, 220))
    player(playerX - 55)
    ball.move()
    ball_col(ball)
    ball.ball_paddle_collide()
    all.draw()
  
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            mouse_Pos = pygame.mouse.get_pos()
            playerX = mouse_Pos[0]

    if playerX <= 55:
        playerX = 55
    elif playerX >= 670:
        playerX = 670
  
    clock.tick(FPS)
  

    pygame.display.update()
pygame.quit()