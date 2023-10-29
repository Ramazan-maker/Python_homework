import pygame
from controllable import Controllable
class Block(Controllable):

    def __init__(self, size, color):
        self.size = size
        self.color = color
        self.position = [0,0]
        super().__init__()
        self.obj = pygame.Surface(size)


    def default_controls(self):
        return (
            {"key": pygame.K_w, "action": lambda: self.moveUp},
            {"key": pygame.K_a, "action": lambda: self.moveLeft},
            {"key": pygame.K_d, "action": lambda: self.moveRight},
            {"key": pygame.K_s, "action": lambda: self.moveDown}
        )     


    def moveUp(self):
        self.position[1] -=1
    
    def moveDown(self):
        self.position[1] +=1

    def moveLeft(self):
        self.position[0] -=1

    def moveRight(self):
        self.position[0] +=1
    
    def show(self):
        self.obj.fill(self.color)

    