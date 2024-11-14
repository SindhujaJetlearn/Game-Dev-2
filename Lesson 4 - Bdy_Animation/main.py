import pygame
import time

pygame.init()

#Screen
WIDTH=600
HEIGHT=600

display_surface=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Birthday Greeting Card")

img=pygame.image.load("bg1.jpg")
#to change the size of the image
image=pygame.transform.scale(img,(WIDTH,HEIGHT))

while True:
  display_surface.fill((255,255,255))
  display_surface.blit(image,(0,0))
  font=pygame.font.SysFont("Times New Roman",72)
  text1=font.render("Happy",True,(0,0,0))
  text2=font.render("Birthday! ",True,(0,0,0))
  display_surface.blit(text1,(210,180))
  display_surface.blit(text2,(160,264))
  pygame.display.update()
  time.sleep(3)

  image2=pygame.image.load("bg2.jpg")
  font2=pygame.font.SysFont("Arial",50)
  text3=font2.render("Have a Bright Future! ",True,(0,0,0))
  display_surface.fill((255,255,255))
  display_surface.blit(image2,(0,0))
  display_surface.blit(text3,(30,30))
  pygame.display.update()
  time.sleep(3)  

  image3 = pygame.image.load("bg3.jpg")
  display_surface.fill((255, 255, 255))
  display_surface.blit(image3, (0, 0))
  pygame.display.update()
  time.sleep(2)
















