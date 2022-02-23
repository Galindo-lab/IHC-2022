import pygame, time
import conf as conf

pygame.init()
pygame.display.set_caption( WINDOW_TITLE )

window = pygame.display.set_mode( WINDOW_DIMENSION )
canvas = pygame.Surface( WINDOW_DIMENSION )
clock = pygame.time.Clock()
running = True


while running:
    dt = clock.tick(60) * .001 * TARGET_FPS
