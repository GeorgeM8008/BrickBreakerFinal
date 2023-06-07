import pygame

#All screen variables and playerY are here to prevent circular importing
screen_width = 725
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
playerY = 460

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