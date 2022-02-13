
import pygame
from Constants import *

from src.Player import Player
from src.Enemy import Enemy
from src.Bullet import Bullet


pygame.init()
pygame.display.set_caption( WINDOW_TITLE )

background = pygame.image.load('data/img/background.jpg')

window = pygame.display.set_mode( WINDOW_DIMENSION )
canvas = pygame.Surface( WINDOW_DIMENSION )
clock = pygame.time.Clock()
running = True

player = Player()
enemy = Enemy()
bullet = Bullet()

while running:
    dt = clock.tick(60) * .001 * TARGET_FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.LEFT_KEY = True
                
            if event.key == pygame.K_RIGHT:
                player.RIGHT_KEY = True

            if event.key == pygame.K_SPACE:
                bullet.fire(player.position)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.LEFT_KEY = False
            elif event.key == pygame.K_RIGHT:
                player.RIGHT_KEY = False

    if bullet.image.get_rect().colliderect(enemy.image.get_rect()):
        print("aaaaaaaaaaa")
    
                
    # Update
    player.update(dt)
    enemy.update(dt)
    bullet.update(dt)
        
    # Draw
    canvas.blit(background, (0,0))
    
    player.draw(canvas)
    enemy.draw(canvas)
    bullet.draw(canvas)

    
    window.blit(canvas, (0,0))
    pygame.display.update()

