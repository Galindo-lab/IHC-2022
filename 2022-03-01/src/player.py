
import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self,x,y):
        self.position = pygame.math.Vector2(x,y)
        self.rect = pygame.Rect( (x,y), (20,20) )
        self.max_speed = 5
