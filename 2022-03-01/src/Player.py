
import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self,x,y):
        self.position = pygame.math.Vector2(x,y)
        self.change = pygame.math.Vector2(0,0)
        self.rect = pygame.Rect( (x,y), (40,40) )
        self.max_speed = 5
        self.color = (255,0,0)

    def draw(self, canvas):
        pygame.draw.rect(canvas, self.color, self.rect)
        

    def update(self, dt):
        self.input()
        
        self.position += self.change * self.max_speed * dt
        self.rect.x = self.position.x
        self.rect.y = self.position.y
g
        self.change.x,self.change.y = 0, 0
        pass

    def input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_UP]:
            self.change.y = -1
        elif keys[pygame.K_DOWN]:
            self.change.y = 1
        else:
            self.change.y = 0

        if keys[pygame.K_LEFT]:
            self.change.x = -1
        elif keys[pygame.K_RIGHT]:
            self.change.x = 1
        else:
            self.change.x = 0
