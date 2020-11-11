# SETTING FOR  GAME

import pygame
from pygame.math import Vector2 as vec


# Creating Game Window
screen_width = 610
screen_height = 670
#gameWindow = pygame.display.set_mode((screen_width,screen_height))
top_bottom_buffer = 50
maze_width = screen_width - top_bottom_buffer
maze_height = screen_height - top_bottom_buffer
rows = 40
cols = 30

# GameBackgrounds
logo = pygame.image.load("screen/logo.png")
'''bg1 = pygame.image.load("screen/first.jpg")
bg1 = pygame.transform.scale(bg1, (screen_width,screen_height)).convert_alpha()
bg2 = pygame.image.load("screen/last_2.png")
bg2 = pygame.transform.scale(bg2, (screen_width,screen_height)).convert_alpha()'''

fps = 60

# Colors
black = (0,0,0)
yellow = (255,255,0)
red = (255,0,0)
grey = (107,107,107)
white = (255,255,255)
blue = (0,162,255)
pink = (255,136,139)
orange = (235,128,0)

# Font setting
start_font = 20
font_type = 'candara'

x=0
y=0
