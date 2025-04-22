import random
import sys
import pygame

from pygame import *
from easygui import *

import datetime

from  board import Board

pygame.init()
fps = pygame.time.Clock()

GRID_WIDTH = 10
GRID_HEIGHT = 20
WINDOW_PADDING = 10
CUBE_WIDTH = 30
BOARD_SCORE_HEIGHT = 50

WIDTH = (CUBE_WIDTH * GRID_WIDTH) + (2 * WINDOW_PADDING)
HEIGHT = (CUBE_WIDTH * GRID_HEIGHT) + (2 * WINDOW_PADDING) + BOARD_SCORE_HEIGHT

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (100, 100, 100)

all_shapes = []
current_shape = None

board = Board(pygame=pygame, window_padding=WINDOW_PADDING, board_score_height=BOARD_SCORE_HEIGHT, width=WIDTH, height=HEIGHT, grid_width=GRID_WIDTH, grid_height=GRID_HEIGHT, cube_width=CUBE_WIDTH)

window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Tetris !')

def init():
    pass

def draw(canvas: Surface):
    board.draw(canvas=canvas)
    
def keydown(event):

    if event.key == K_DOWN:
        board.move_down()
    elif event.key == K_LEFT:
        board.move_left()
    elif event.key == K_RIGHT:
        board.move_right()
    elif event.key == K_UP:
        board.rotate()

init()
while True:
    
    draw(window)
    keys = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        
        if event.type == KEYDOWN:
            keydown(event)
        elif event.type == pygame.USEREVENT:
            board.move_down()
        elif event.type == QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()
        
    pygame.display.update()
    fps.tick(60)
