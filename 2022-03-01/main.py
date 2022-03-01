import pygame, time
from conf import *

from src.Player import Player



pygame.init()
pygame.display.set_caption( WINDOW_TITLE )

window = pygame.display.set_mode( WINDOW_DIMENSION )
canvas = pygame.Surface( WINDOW_DIMENSION )
clock = pygame.time.Clock()
running = True


player = Player(100,100)



while running:
    dt = clock.tick(60) * .001 * TARGET_FPS
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update(dt)
    player.draw(canvas)

    window.blit(canvas, (0,0))
    pygame.display.update()
