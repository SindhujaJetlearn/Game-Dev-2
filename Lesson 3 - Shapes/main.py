import pygame
pygame.init()

#global variables
screen = pygame.display.set_mode([500,500])
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white=(255,255,255)
yellow = (255,255,0)
black=(0,0,0)

screen.fill(white)

position=(300,300)
radius=50
wid=2
pygame.draw.circle(screen,red,position,radius,wid)
pygame.display.update()

class myCircle():
  def __init__(self,color, pos, rad, wid=0):
    self.color = color
    self.pos = pos
    self.rad = rad
    self.wid = wid
    self.screen = screen

  def draw(self):
    pygame.draw.circle(self.screen, self.color, self.pos, self.rad, self.wid)

  def grow(self,r):
    self.rad = self.rad+r
    pygame.draw.circle(self.screen, self.color, self.pos, self.rad, self.wid )


#Creating Objects
blueCircle=myCircle(blue,position,radius+90,4)
redCircle=myCircle(red,position,radius+60,1)
yellowCircle=myCircle(yellow,position,radius+45,6)
greenCircle = myCircle(green, position,radius+30, 3)

while True:
  for event in pygame.event.get():
    #mouse is clicked
    if(event.type ==pygame.MOUSEBUTTONDOWN):
      blueCircle.draw()
      redCircle.draw()
      yellowCircle.draw()
      greenCircle.draw()
      pygame.display.update()
    #mouse is released
    elif (event.type == pygame.MOUSEBUTTONUP):
      blueCircle.grow(1)
      redCircle.grow(2)
      yellowCircle.grow(3)
      greenCircle.grow(4)
      pygame.display.update()
    #mouse move
    elif (event.type == pygame.MOUSEMOTION):
      pos=pygame.mouse.get_pos()
      blackCircle = myCircle(black, pos, 5)
      blackCircle.draw()
      pygame.display.update()



