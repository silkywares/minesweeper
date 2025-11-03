import pygame

SCREEN_DIM = 512
CELL_DIM = 32

def draw_grid():
    line_count = SCREEN_DIM / CELL_DIM
    i = 0
    for i in range(int(line_count)):
        pygame.draw.line(screen, "black", ((i*CELL_DIM)+CELL_DIM,0), ((i*CELL_DIM)+CELL_DIM,SCREEN_DIM), 1)
        pygame.draw.line(screen, "black", (0,(i*CELL_DIM)+CELL_DIM), (SCREEN_DIM,(i*CELL_DIM)+CELL_DIM), 1)
        

pygame.init()
screen = pygame.display.set_mode((SCREEN_DIM,SCREEN_DIM))
clock = pygame.time.Clock()
running = True 

font = pygame.font.Font(None, 36)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("tan")
    draw_grid()
    text_surface = font.render("Hello Pygame!", True, (0, 0, 0))
    screen.blit(text_surface, (50, 50))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()