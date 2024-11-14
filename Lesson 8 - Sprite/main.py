import pygame
pygame.init()

pygame.display.set_caption('Rocket in Space')
screen_width=700
screen_height=500
screen=pygame.display.set_mode([screen_width,screen_height])

#Player Class
class Player(pygame.sprite.Sprite):
  #Attribute
  def __init__(self):
    #Super extracts attributes of sprite class (Parent class)
    super().__init__()
    self.image=pygame.image.load("character1.png")
    self.image=pygame.transform.scale(self.image,(70,100))
    self.rect=self.image.get_rect()

  #Function
  def update(self,pressed_keys):
    if(pressed_keys[pygame.K_UP]):
      self.rect.move_ip(0,-5)
    if(pressed_keys[pygame.K_DOWN]):
      self.rect.move_ip(0,5)
    if(pressed_keys[pygame.K_RIGHT]):
      self.rect.move_ip(5,0)
    if(pressed_keys[pygame.K_LEFT]):
      self.rect.move_ip(-5,0)

    #Make the sprite stay inside the screen
    if self.rect.left < 0:
      self.rect.left = 0
    if self.rect.right > screen_width:
      self.rect.right = screen_width
    if self.rect.top < 0:
      self.rect.top = 0
    if self.rect.bottom > screen_height:
      self.rect.bottom = screen_height

#Create a group
sprites=pygame.sprite.Group()

def startGame():
  #Create the object
  rocket=Player()
  sprites.add(rocket)

  #Infinite loop to start game
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        exit(0)

    pressed_keys=pygame.key.get_pressed()
    rocket.update(pressed_keys)
    screen.blit(pygame.image.load("background.png"),(0,0))
    sprites.draw(screen)
    pygame.display.update()

startGame()










