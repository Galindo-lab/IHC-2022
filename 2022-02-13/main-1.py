
import pygame

# incializa el juego
pygame.init()

# caption
pygame.display.set_caption("Learning")

# create the screen
canvas = pygame.Surface((800,600))
screen = pygame.display.set_mode((800,600))
runnig = True
clock = pygame.time.Clock()
TARGET_FPS = 60

# player
playerImg = pygame.image.load('data/img/space-invaders.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

def player(x,y):
    canvas.blit(playerImg, (x,y))

while runnig:
    dt = clock.tick(60) * .001 * TARGET_FPS
     
    for event in pygame.event.get():
        runnig = event.type != pygame.QUIT

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5;
            if event.key == pygame.K_RIGHT:
                playerX_change = 5;
            if event.key == pygame.K_LCTRL:
                print("a")

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change, playerY_change = 0, 0

    canvas.fill( (30, 10, 60) )
                
    playerX += playerX_change * dt

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    
    player(playerX,playerY)
                
    screen.fill( (0,0,0) )
    screen.blit( canvas, (0,0) )
    
    
    
    
    pygame.display.update()
