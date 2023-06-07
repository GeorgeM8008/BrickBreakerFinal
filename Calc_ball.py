import pygame
import main

ball_radius = 10

class ball:
    VEL = 5
    def __init__(self, x, y, radius, colour):
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = colour
        self.x_vel = 0
        self.y_vel = -self.VEL

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel
    def set_vel(self, x_vel, y_vel):
        self.x_vel = x_vel
        self.y_vel = y_vel
    def draw(self):
        pygame.draw.circle(main.screen, self.colour, (self.x, self.y), self.radius)