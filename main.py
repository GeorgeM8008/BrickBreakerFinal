##George Mi, CS30, May 23th

#Importing all the modules I need
import pygame
import math
#Importing the Ball class from the other file
from Calc_ball import Ball
import Calc_ball

#Initializes all imported pygame modules
pygame.init()

#Font and size of letters that are being printed on the screen
LIVES_FONT = pygame.font.SysFont("ariel.ttf", 42)
#Number of lives the player has
lives = 3

#Dimensions of the screen and initializing it
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

#Variable running that beings as false, you need to click to start
running = False

#Sets the header as Brick Breaker
pygame.display.set_caption("Brick Breaker")
#Sets the icon as an image of Brick Breaker
icon = pygame.image.load('brick.png')
pygame.display.set_icon(icon)

#Speed the game runs at
FPS = 60
clock = pygame.time.Clock()

#Initial position and size of the platform
playerX = 293
playerY = 460
player_width = 125
player_height = 18

'''Player class includes drawing the platform and it's movement based on
the mouse. Also set's boundaries for the player.'''
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

        if self.x <= 0:
            self.x = 0
        elif self.x >= 670:
            self.x = 670

'''Brick class includes drawing an individual brick, detecting a collision,
and changing colour based on it's health'''
class Brick:
    def __init__(self, x, y, width, height, health, colours):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = health
        self.max_health = health
        self.colours = colours
        self.colour = colours[0]

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.width, self.height))

    def collide(self, ball):
        if not (ball.x <= self.x + self.width and ball.x >= self.x):
            return False
        if not (ball.y - ball.radius <= self.y + self.height):
            return False

        self.hit()
        ball.set_vel(ball.x_vel, ball.y_vel * -1)
        return True

    def hit(self):
        self.health -= 1
        self.colour = self.interpolate(
            *self.colours, self.health/self.max_health)
    @staticmethod
    def interpolate(color_a, color_b, t):
        # 'color_a' and 'color_b' are RGB tuples
        # 't' is a value between 0.0 and 1.0
        # this is a naive interpolation
        return tuple(int(a + (b - a) * t) for a, b in zip(color_a, color_b))
      
#The ball
ball = Ball(Calc_ball.iballX, Calc_ball.iballY, Calc_ball.ball_radius, (0, 0, 0))

#The platform
player = Player(playerX, playerY, player_width, player_height, (0, 0, 0))

#The bricks
bricks = generate_bricks(3, 10)

#Resets the ball after it hits the floor
def reset():
    global lives, running
    pygame.time.delay(500)
    lives -= 1
    ball.x = screen_width/2 - 10
    ball.y = playerY - 10
    ball.set_vel(0, ball.VEL * -1)

#Displays text if you lose
def display_text(text):
    text_render = LIVES_FONT.render(text, 1, "red")
    screen.blit(text_render, (screen_width/2 - text_render.get_width() /
                               2, screen_height/2 - text_render.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)

#Ball collision with walls, flips it's velocities
def ball_col(ball):
    global running, lives
    if ball.x - Calc_ball.ball_radius <= 0 or ball.x + Calc_ball.ball_radius >= screen_width - 10:
        ball.set_vel(ball.x_vel * -1, ball.y_vel)
    if ball.y - ball.radius <= 0:
        ball.set_vel(ball.x_vel, ball.y_vel * -1)
    if ball.y + ball.radius >= 500:
        reset()

'''Ball collision with player platform, changes velocity at different angeles depending on where it hit the platform'''
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

#Creates bricks in rows and columns
def generate_bricks(rows, cols):
    gap = 2
    brick_width = screen_width // cols - gap
    brick_height = 20

    bricks = []
    for row in range(rows):
        for col in range(cols):
            brick = Brick(col * brick_width + gap * col, row * brick_height +
                          gap * row, brick_width, brick_height, 2, [(0, 0, 255), (255, 255, 0)])
            bricks.append(brick)
    return bricks

'''Before running is true, it displays all the components frozen until
the player clicks their mouse'''
while running == False:
    screen.fill((245, 245, 220))
  
    player.draw(screen)
    ball.draw(screen)
  
    for brick in bricks:
        brick.draw(screen)

    lives_text = LIVES_FONT.render(f"Lives: {lives}", 1, "black")
    screen.blit(lives_text, (10, screen_height - lives_text.get_height() - 9))

      
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            running = True
    clock.tick(FPS)
    pygame.display.update()

'''When running, goes through all the functions until either all the bricks are gone
or the player runs out of lives'''
while running == True:
    screen.fill((245, 245, 220))
    player.draw(screen)
    ball.move()
    player.move()
    ball_col(ball)
    ball_player_col(ball, player)
    ball.draw(screen)
    for brick in bricks:
        brick.draw(screen)
    lives_text = LIVES_FONT.render(f"Lives: {lives}", 1, "black")
    screen.blit(lives_text, (10, screen_height - lives_text.get_height() - 9))

    for brick in bricks[:]:
        brick.collide(ball)

        if brick.health <= 0:
            bricks.remove(brick)
    if lives <= 0:
        bricks = generate_bricks(3, 10)
        lives = 3
        reset()
        display_text("You Lost!")

    if len(bricks) == 0:
        bricks = generate_bricks(3, 10)
        lives = 3
        reset()
        display_text("You Won!")

    clock.tick(FPS)

#Continually updates the screen
    pygame.display.update()
#Pygame quits if running ever becomes false again
pygame.quit()