import pygame

class Box():
    def __init__(self, x, y, boxsize, id):
        self.id = id
        self.width = self.height = boxsize
        self.color = 0, 0 ,0
        self.border = 255, 255, 255
        self.state = False
        self.nextState = False
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.neighbours = []
    
    def switchState(self):
        self.nextState = not(self.state)

    def calculateState(self):
        neighbourCount = 0
        for cell in self.neighbours:
            if cell.state: 
                neighbourCount += 1

        if self.state == False and neighbourCount == 3:
            self.switchState()

        if self.state == True and (neighbourCount > 3 or neighbourCount < 2):
            self.switchState()
