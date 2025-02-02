import pygame
import random

class Apple:
    width = 20
    height = 20
    color = (255, 0, 0)
    onScreen = False
    rect = pygame.Rect((500, 500, width, height))
    ava_pos = {}

    def __init__(self, SCR_WIDTH, SCR_HEIGHT):
        self.SCR_WIDTH = SCR_WIDTH
        self.SCR_HEIGHT = SCR_HEIGHT
        self.boundPixelX = int(self.SCR_WIDTH/self.width)
        self.boundPixelY = int(self.SCR_HEIGHT/self.height)

    def getPixelX(self):
        return int(self.rect.x/self.width)
    
    def getPixelY(self):
        return int(self.rect.y/self.height)
    
    def getPixelTuple(self):
        return (self.getPixelX(), self.getPixelY())
    
    def copyApple(self, onScreen, rect):
        if(onScreen == False): return
        self.rect = rect
        return

    def generate(self, occupied):
        if(self.onScreen): return
        self.onScreen = True
        self.ava_pos.clear()
        for rect in occupied:
            self.ava_pos[str(rect[1].x) + " " + str(rect[1].y)] = True
        x = random.randint(0, self.boundPixelX-1)*self.width
        y = random.randint(0, self.boundPixelY-1)*self.height
        while(str(x) + " " + str(y) in self.ava_pos):
            x = random.randint(0, self.boundPixelX-1)*self.width
            y = random.randint(0, self.boundPixelY-1)*self.height
        self.rect = pygame.Rect((x, y, self.width, self.height))

    def collide(self, x, y):
        if(self.rect.x == x and self.rect.y == y):
            self.onScreen = False
            return True
        return False

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)