import pygame
pygame.init()

screen=pygame.display.set_mode((600,600))
screen.fill((144,188,143))
pygame.display.update()

#Load and blit the images on the screen
subwaysurfer=pygame.image.load('subwaysurfer.png')
screen.blit(subwaysurfer,(150,50))

ludo=pygame.image.load('ludo.png')
screen.blit(ludo,(150,150))

templerun=pygame.image.load('templerun.png')
screen.blit(templerun,(150,250))

candycrush=pygame.image.load('candycrush.jpg')
screen.blit(candycrush,(150,350))

#Texts on screen
font=pygame.font.SysFont("Times New Roman",36)

text1=font.render("Ludo",True,(0,0,0))
screen.blit(text1,(350,70))

text2=font.render("Candy crush",True,(0,0,0))
screen.blit(text2,(350,170))

text3=font.render("Subway Surfer",True,(0,0,0))
screen.blit(text3,(350,270))

text4=font.render("Temple run",True,(0,0,0))
screen.blit(text4,(350,370))

pygame.display.update()

while True:
  event=pygame.event.poll()

  if event.type == pygame.MOUSEBUTTONDOWN : #mouse click
    pos=pygame.mouse.get_pos()
    print(pos)
    pygame.draw.circle(screen,(0,0,0),pos,10,0)
    pygame.display.update()

  if event.type == pygame.MOUSEBUTTONUP: #mouse release
    pos2=pygame.mouse.get_pos()
    pygame.draw.line(screen,(0,0,0),pos,pos2,5)
    pygame.draw.circle(screen,(0,0,0),pos2,10,0)
    pygame.display.update()





