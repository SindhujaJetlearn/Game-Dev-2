import pygame
from time import *

pygame.init()
screen = pygame.display.set_mode((500, 500))

player=pygame.image.load("character.png")
background=pygame.image.load("background.png")

player_x = 100
player_y = 10

keys = [False, False, False, False]

while player_y < 400:
  screen.blit(background,(0,0))
  screen.blit(player,(player_x,player_y))
  pygame.display.update()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit(0)
    if event.type == pygame.KEYDOWN : #pressed 
      if event.key == pygame.K_UP:
        keys[0]=True
      if event.key == pygame.K_LEFT:
        keys[1]=True
      if event.key==pygame.K_DOWN:
        keys[2]=True
      if event.key==pygame.K_RIGHT:
        keys[3]=True

      #3.To check a key is released -KEYUP
    if event.type==pygame.KEYUP:
      if event.key==pygame.K_UP:
        keys[0]=False
      if event.key==pygame.K_LEFT:
        keys[1]=False
      if event.key==pygame.K_DOWN:
        keys[2]=False
      if event.key==pygame.K_RIGHT:
        keys[3]=False

  if keys[0]: #up
    if player_y > 0:
      player_y -= 7
  if keys[2]:#down
    if player_y <399:
      player_y += 7
  if keys[1]: #left
    if player_x > 0:
      player_x-=7
  if keys[3]:#right
    if player_x< 399:
      player_x+=7

  player_y += 5
  sleep(0.05)

print("Game Over !")

















