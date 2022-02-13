
import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load('data/img/circle.png')
        self.rect = self.image.get_rect()
        self.max_speed = -10
        self.position = pygame.math.Vector2(0,0)
        self.change = pygame.math.Vector2(0, 0)
        self.status = "ready"

    def draw(self, display):
        if self.status == "fire":
            display.blit(self.image, (self.rect.x, self.rect.y))

    def update(self, dt):
        if self.status == "fire":
            self.movement(dt)
            self.rect = self.position

    def movement(self, dt):
        self.position.y += self.max_speed * dt
        if self.position.y <= 0:
            self.status = "ready"
            
    def fire(self, position):
        if self.status == "ready":
            self.position.x, self.position.y = position.x+16, position.y - 16
            self.status = "fire"
        
        
