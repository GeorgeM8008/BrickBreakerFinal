import pygame
import math


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

playerX = 293
playerY = 460
player_width = 125
player_height = 18

class Player:
    def __init__(self, x, y, width, height, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour

    def draw(self, screen):
        pygame.draw.rect(
            screen, self.colour, (self.x, self.y, self.width, self.height))
    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
               mouse_Pos = pygame.mouse.get_pos()
               self.x = mouse_Pos[0] - 62
               player.draw(screen)

        if self.x <= 55:
            self.x = 55
        elif self.x >= 670:
            self.x = 670

ball_radius = 10
class Ball:
    VEL = 5

    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.x_vel = 0
        self.y_vel = -self.VEL

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def set_vel(self, x_vel, y_vel):
        self.x_vel = x_vel
        self.y_vel = y_vel

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


iballX = screen_width/2 - ball_radius
iballY = playerY - 10
ball = Ball(iballX, iballY, ball_radius, (0, 0, 0))
player = Player(playerX, playerY, player_width, player_height, (0, 0, 0))

def ball_col(ball):
    if ball.x - ball_radius <= 0 or ball.x + ball_radius >= screen_width - 10:
        ball.set_vel(ball.x_vel * -1, ball.y_vel)
    if ball.y + ball.radius >= screen_height or ball.y - ball.radius <= 0:
        ball.set_vel(ball.x_vel, ball.y_vel * -1)

def ball_player_col(ball, player):
    if not (ball.x <= player.x + player.width and ball.x >= player.x):
        return
    if not (ball.y + ball.radius >=player.y):
        return

    player_center = player.x + player.width/2
    distance_to_center = ball.x - player_center

    percent_width = distance_to_center / player.width
    angle = percent_width * 90
    angle_radians = math.radians(angle)

    x_vel = math.sin(angle_radians) * ball.VEL
    y_vel = math.cos(angle_radians) * ball.VEL * -1

    ball.set_vel(x_vel, y_vel)
       
       

running = False
while running == False:
    screen.fill((245, 245, 220))
    player.draw(screen)
    ball.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            running = True
    clock.tick(FPS)
    pygame.display.update()
  
while running:
    screen.fill((245, 245, 220))
    player.draw(screen)
    ball.move()
    player.move()
    ball_col(ball)
    ball_player_col(ball, player)
    ball.draw(screen)
  
    clock.tick(FPS)

    pygame.display.update()
pygame.quit()