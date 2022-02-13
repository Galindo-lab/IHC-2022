
import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load('data/img/space-ship.png')
        self.rect = self.image.get_rect()
        self.max_speed = 3
        self.position = pygame.math.Vector2(random.randint(0,800), 50)
        self.change = pygame.math.Vector2(3, 3)

    def draw(self, display):
        display.blit(self.image, (self.rect.x, self.rect.y))

    def update(self, dt):
        self.movement(dt)
        self.rect = self.position

    def movement(self, dt):
        self.position.x += self.change.x * dt
        
        if self.position.x <= 0:            
            self.position.x = 0
            self.change.x = self.max_speed;
            self.position.y += 40
        elif self.position.x >= 736:
            self.position.x = 736
            self.change.x = -self.max_speed;
            self.position.y += 40
        
