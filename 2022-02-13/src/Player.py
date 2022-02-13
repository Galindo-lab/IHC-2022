
import pygame


class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        self.image = pygame.image.load('data/img/space-invaders.png')
        self.rect = self.image.get_rect()
        self.max_speed = 5
        self.position = pygame.math.Vector2(370, 480)
        self.change = pygame.math.Vector2(0, 0)

        # controles 
        self.LEFT_KEY, self.RIGHT_KEY = False, False
        
    def draw(self, display):
        display.blit(self.image, (self.rect.x, self.rect.y))

    def update(self, dt):
        self.horizontal_movement(dt)
        self.rect = self.position

    def horizontal_movement(self, dt):
        self.change.x = 0
        
        if self.LEFT_KEY:
            self.change.x = -self.max_speed
        if self.RIGHT_KEY:
            self.change.x = self.max_speed

        self.position.x += self.change.x * dt
            
        if self.position.x <= 0:
             self.position.x = 0
        elif self.position.x >= 736:
             self.position.x = 736


       
            



