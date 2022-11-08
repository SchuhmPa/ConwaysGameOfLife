from Box import Box

import sys, pygame
pygame.init()


size = width, height = 900, 600
boxsize = 15
black = (0, 0, 0)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Conways Game of Life')

grid = []
x = 0
y = 0
for i in range(0, ((width * height) // (boxsize * boxsize)) ):
    if ((i*boxsize) % width) == 0 and i != 0:
        x = 0
        y+=boxsize
    
    box = Box(x*boxsize, y, boxsize, i)
    grid.append(box)
    x+=1

for box in grid:
    for box2 in grid:
        if box2.id == (box.id -1 ) \
        or box2.id == (box.id + 1) \
        or box2.id == (box.id - (width // boxsize)) \
        or box2.id == (box.id - (width // boxsize) - 1) \
        or box2.id == (box.id - (width // boxsize) + 1) \
        or box2.id == (box.id + (width // boxsize)) \
        or box2.id == (box.id + (width // boxsize) - 1) \
        or box2.id == (box.id + (width // boxsize) + 1):
            box.neighbours.append(box2)

initPhase = True
def changeInit():
    global initPhase
    initPhase = False

def gameloop():
    while initPhase:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for box in grid:
                    if box.rect.collidepoint(event.pos):
                        box.state = True
                        box.nextState = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN: 
                    changeInit()

        for box in grid:
            if box.state:
                pygame.draw.rect(screen, box.border, box.rect)
            else:
                pygame.draw.rect(screen, box.border, box.rect, 1)

        pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        screen.fill(black)
        
        for box in grid:
            box.calculateState()

        for box in grid:
            box.state = box.nextState

        for box in grid:
            if box.state:
                pygame.draw.rect(screen, box.border, box.rect)
            else:
                pygame.draw.rect(screen, box.border, box.rect, 1)

        pygame.display.flip()
        pygame.time.wait(30)


if __name__ == '__main__':
    gameloop()
