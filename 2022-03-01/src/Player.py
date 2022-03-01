
import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self,x,y):
        self.position = pygame.math.Vector2(x,y)
        self.rect = pygame.Rect( (x,y), (20,20) )
        self.max_speed = 5
        self.color = (255,0,0)

    def draw(self, canvas):
        pygame.draw.rect(canvas, self.color, self.rect)
        

    def update(self, dt):
        
