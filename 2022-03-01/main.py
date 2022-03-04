import pygame, time
from conf import *

from src.Player import Player
from src.Npc import Npc


pygame.init()
pygame.font.init() 

pygame.display.set_caption( WINDOW_TITLE )

window = pygame.display.set_mode( WINDOW_DIMENSION )
canvas = pygame.Surface( WINDOW_DIMENSION )
clock = pygame.time.Clock()
running = True


player = Player(100,100)
npc = Npc(200,200)


while running:
    dt = clock.tick(60) * .001 * TARGET_FPS
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    canvas.fill( (0,0,0) )
    player.draw(canvas)
    npc.draw(canvas)
    
    player.update(dt)
    npc.update(dt)

    if player.rect.colliderect(npc.interaction_area):
        npc.show_message()
        npc.color = (0,0,255)
    else:
        npc.color = (255,255,255)
    
    window.blit(canvas, (0,0))
    pygame.display.update()
