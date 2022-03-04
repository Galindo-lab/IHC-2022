
import pygame


class Npc():
    def __init__(self,x,y):
        self.font = pygame.font.SysFont('Comic Sans MS', 20)
        self.textsurface = self.font.render('Estoy sufriendo :)', False, (255, 255, 255))
        
        self.position = pygame.math.Vector2(x,y)
        self.rect = pygame.Rect( (x,y), (40,40) )
        self.interaction_area = self.rect.inflate(75,75)
        self.color = (255,255,255)
        self.message_visible = False

    def draw(self, canvas):
        pygame.draw.rect(canvas, self.color, self.rect)
        if self.message_visible:
            canvas.blit(self.textsurface,(self.position.x-20,self.position.y-30))

    def update(self,dt):
        self.message_visible = False
        pass

    def show_message(self):
        self.message_visible = True

