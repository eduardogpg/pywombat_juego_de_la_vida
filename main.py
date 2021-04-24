import sys
import pygame

from cell import Cell
from cell import generate_cells

WIDTH = 1200
HEIGHT = 800

FPS = 60

start = False
current_second = 0

pygame.init()

fps = pygame.time.Clock()

surface = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('Juego de la vida en PyWombat')

cells = generate_cells(WIDTH, HEIGHT, 30, 30)

sprites = pygame.sprite.Group()
sprites.add(cells)

def start_algorithm():
    for cell in sprites:
        neighborhoods = cell.get_neighborhoods(cells)

        if cell.check:
            if not len(neighborhoods) in (2, 3):
                cell.change_next_state()
        else:
            if len(neighborhoods) == 3:
                cell.change_next_state()

while True:

    time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            current_position = pygame.mouse.get_pos()

            for cell in sprites:
                if cell.rect.collidepoint(current_position):
                    cell.select()

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            start = True

    if start:
        second = time // 200
        
        if second != current_second:
            start_algorithm()

            for cell in sprites:
                cell.update()

            current_second = second

    sprites.draw(surface)
    pygame.display.update()

    fps.tick(FPS)