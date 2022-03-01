
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
        self.position += self.change * dt
        self.change.x = 0
        self.change.y = 0
        pass

    def move_left(self):
        self.change.x = -self.max_speed

    def move_right(self):
        self.change.x = self.max_speed

    def move_up(self):
        self.change.y = -self.max_speed

    def move_down(self):
        self.change.y = -self.max_speed
