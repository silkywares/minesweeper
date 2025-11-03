import pygame
from pygame.math import Vector2
import numpy
import random

GRID_DIM = 1024
CELL_DIM = 64
PADDING = 64

def draw_grid():
    line_count = GRID_DIM / CELL_DIM

    for i in range(int(line_count)):
        pygame.draw.line(screen, "black", ((i*CELL_DIM)+CELL_DIM,PADDING), ((i*CELL_DIM)+CELL_DIM,GRID_DIM), 1)
        pygame.draw.line(screen, "black", (PADDING,(i*CELL_DIM)+CELL_DIM), (GRID_DIM,(i*CELL_DIM)+CELL_DIM), 1)

def grid_vector_randomizer():
    size = int(GRID_DIM / CELL_DIM)
    grid = []
    for y in range(size):
        row = []
        for x in range(size):
            angle = random.uniform(0,360)
            #vector = Vector2(1,0).rotate(angle)
            row.append(angle)
        grid.append(row)
    return grid

def perlin_noise(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            angle = grid[y][x]                  # get the stored angle
            text_surface = font.render(f"{int(angle)}", True, (0, 0, 0))
            screen.blit(text_surface, (x*CELL_DIM-9+PADDING, y*CELL_DIM-9+PADDING))

pygame.init()
screen = pygame.display.set_mode((GRID_DIM+PADDING,GRID_DIM+PADDING))
clock = pygame.time.Clock()
running = True 
font = pygame.font.Font(None, 24)

grid_numbers = grid_vector_randomizer()

#screen.fill("tan")

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("tan")
    draw_grid()
    perlin_noise(grid_numbers)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()