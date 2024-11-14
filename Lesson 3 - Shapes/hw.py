import pygame
pygame.init()

screen = pygame.display.set_mode([500, 500])
pygame.display.set_caption("Rectangle Expansion")

class Rect:
    def __init__(self, color, position, size, width=0):
        self.color = color
        self.position = position
        self.size = size 
        self.width = width
        self.screen = screen

    def drawRect(self):
        pygame.draw.rect(self.screen, self.color, (*self.position, *self.size), self.width)

    def expandRect(self, d):
        self.size = (self.size[0] + d, self.size[1] + d)

redRect = Rect("red", (200, 200), (60, 60))
greenRect = Rect("green", (200, 200), (100, 100))
yellowRect = Rect("yellow", (200, 200), (150, 150), 2)
purpleRect = Rect("purple", (200, 200), (200, 200), 5)

blackRectangles = []

running = True
while running:
    screen.fill("white")
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            redRect.drawRect()
            greenRect.drawRect()
            yellowRect.drawRect()
            purpleRect.drawRect()

        if event.type == pygame.MOUSEBUTTONUP:
            redRect.expandRect(2)
            greenRect.expandRect(3)
            yellowRect.expandRect(4)
            purpleRect.expandRect(5)

        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            blackRectangles.append(pos)

    for pos in blackRectangles:
        blackRect = Rect("black", pos, (5, 5))
        blackRect.drawRect()

        
    redRect.drawRect()
    greenRect.drawRect()
    yellowRect.drawRect()
    purpleRect.drawRect()

    pygame.display.update()