import pygame
from pygame.locals import *

pygame.init()
fart = True
screen_width = 725
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Brick Breaker")
icon = pygame.image.load('brick.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('minus-big-symbol.png')
playerX = 300
playerY = 400

def player():
  global playerImg, playerX, playerY
  screen.blit(playerImg, (playerX, playerY))

running = True
while running:
  screen.fill((245, 245, 220))
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  player()
  pygame.display.update()