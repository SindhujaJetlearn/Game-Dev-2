import pygame
import random
import time

# Initialize Pygame
pygame.init()
pygame.display.set_caption('Recycle Marathon')
# Set the height and width of the screen
screen_width = 900
screen_height = 700
screen = pygame.display.set_mode([screen_width, screen_height])

def changeBackground(img):
  background=pygame.image.load(img)
  bg=pygame.transform.scale(background,(screen_width, screen_height))
  screen.blit(bg,(0,0))

class Bin(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image=pygame.image.load('bin.png')
    self.image=pygame.transform.scale(self.image,(40,60))
    self.rect=self.image.get_rect()

#Recyclable sprite
class Recyclable(pygame.sprite.Sprite):
  def __init__(self, img):
    super().__init__()
    self.image = pygame.image.load(img)
    self.image = pygame.transform.scale(self.image, (30, 30))
    self.rect = self.image.get_rect()

#Non_recyclable sprite
class Non_recyclable(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load('plastic.png')
    self.image = pygame.transform.scale(self.image, (40, 40))
    self.rect = self.image.get_rect()

#List of images for Recyclable class
images = ["item1.png", "item2.png", "item3.png"]

#Create sprite groups
item_list = pygame.sprite.Group()  #recyclable
plastic_list = pygame.sprite.Group()  #non-recyclable
allsprites = pygame.sprite.Group()

bin=Bin()
allsprites.add(bin)

#create recyclable item sprites
for i in range(50):
  item=Recyclable(random.choice(images))
  item.rect.x=random.randrange(screen_width)
  item.rect.y=random.randrange(screen_height)
  item_list.add(item)
  allsprites.add(item)

#create plastic
for i in range(20):
  plastic = Non_recyclable()
  plastic.rect.x = random.randrange(screen_width)
  plastic.rect.y = random.randrange(screen_height)
  plastic_list.add(plastic)
  allsprites.add(plastic)



#initialize essential variables
# Define colour
WHITE = (255, 255, 255)
RED = (255, 0, 0)

playing = True
score = 0

clock = pygame.time.Clock()
start_time = time.time() #fetch the current time

#font to print score on screen
myFont = pygame.font.SysFont("Times New Roman", 22)
text = myFont.render("Score =" + str(0), True, WHITE)


while playing:
  #can be used to control speed
  clock.tick(60)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      playing=False

  timeElapsed=time.time()-start_time
  if timeElapsed >=60:
    if score >20:
      screen.fill("green")
      text=myFont.render("Bin loot successful",True,RED)
      screen.blit(text,(250,40))
    else:
      screen.fill("red")
      text=myFont.render("Better luck next time",True,WHITE)
      screen.blit(text,(250,40))
  else:
    changeBackground("bground.png")
    countDown = myFont.render("Time Left:" + str(60 - int(timeElapsed)), True, WHITE)
    screen.blit(countDown, (20, 10))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
      if bin.rect.y >0:
        bin.rect.y -= 5

    if keys[pygame.K_DOWN]:
      if bin.rect.y < 630:
        bin.rect.y +=5

    if keys[pygame.K_RIGHT]:
      if bin.rect.x < 850:
        bin.rect.x +=5

    if keys[pygame.K_LEFT]:
      if bin.rect.x > 0:
        bin.rect.x -=5

    item_hit_list=pygame.sprite.spritecollide(bin, item_list, True)
    for item in item_hit_list:
      score +=1
      point = myFont.render("Score =" + str(score), True, WHITE)

    plastic_hit_list = pygame.sprite.spritecollide(bin, plastic_list, True)
    for plastic in plastic_hit_list:
      score -= 5
      point = myFont.render("Score =" + str(score), True, WHITE)


  screen.blit(point, (20, 50))
  allsprites.draw(screen)
  pygame.display.update()     

pygame.quit()










