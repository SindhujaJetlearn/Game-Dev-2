#OOPS - Object Oreinted Progamming Structure

#Class - blueprint of an object, which has properties and functions of an object

class Student():
  #Properties / Attributes
  #inbuilt function
  def __init__(self,name,age,grade,favColor,hobby):
    self.name=name
    self.age=age
    self.grade=grade
    self.favColor=favColor
    self.hobby=hobby
    self.intro=" "

  #Function / Methods
  #User defined
  def showDetails(self):
    print("The details of the student are : ")
    print("Name : ",self.name)
    print("Age : ",self.age)
    print("Grade : ",self.grade)
    print("Favourite Color : ",self.favColor)
    print("Hobby : ",self.hobby)
    print()

  def intro_student(self):
    self.intro=input("Please introduce yourself : ")
    print(self.intro)
    print()

#Object for Student class - instance of a class
#init function gets called itself when an object is created
s1=Student("Remi",13,9,"purple","Dancing")

#objectName.functionName() - calling the functions
s1.showDetails()
s1.intro_student()

s2=Student("Mihir",11,"5th","Gold","Playing games")
#objectName.functionName()
s2.showDetails()
s2.intro_student()


"""
#import and initialize pygame
import pygame

pygame.init()

#Create a surface to draw shapes
screen=pygame.display.set_mode((800,600))

#colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

screen.fill("pink")

#create a rectangle class - blueprint of an object
#It has functions and properties of objects
class Rect():
  #init is an inbulit function - properties or attributes
  def __init__(self,color, dimensions):
    self.rect_surface=screen
    self.rect_color=color
    self.rect_dimensions=dimensions

  #function or methods - user defined
  def draw_rect(self):
   self.rect_draw= pygame.draw.rect(self.rect_surface,self.rect_color, self.rect_dimensions)

#Create Objects - instance of class
#init function gets called itself, when an Object is created
greenRect=Rect(green,(50, 20, 100, 120))

#objectName.functionName()
greenRect.draw_rect()

redRect=Rect(red,(150, 200, 200, 150))
redRect.draw_rect()

blueRect = Rect(blue, (300, 400, 200, 200))
blueRect.draw_rect()

purpleRect=Rect("purple",(500,200,150,150))
purpleRect.draw_rect()

while True:
  pygame.display.update()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
"""

'''
def greet():
    print("Hello to you")
    print("My Name is JARVIS")
    print("May I know your name: ")
    userName = input()


#How to call the function
greet()


#How to make a class

class Student():
  #properties/ attributes
  name=" "
  age=12
  grade=""
  house = " "
  classteacher = " "

  #init - inbulit function. Calls iteself when an object is created.
  def __init__(self):
    print("Making a new student ")

  #User defined function
  def getDetails(self):
    self.name=input("Enter your name : ")
    self.age=int(input("Please enter your age : "))
    self.grade=input("Which grade are you in ?  ")
    self.house=input("Which house you belong to ?  ")
    self.classteacher=input("Who is your class teacher ? ")

  #User defined function
  def showDetails(self):
    print()
    print("The name of the student is", self.name)
    print("Age of the student : ", self.age)
    print("Grade of the student : ", self.grade)
    print("House of the student : ", self.house)
    print("Teacher name : ", self.classteacher)
    print()

#Object for Student class
student1= Student()
#objectName.FunctionName()
student1.getDetails()
student1.showDetails()

#Object for Student class
student2= Student()
#objectName.FunctionName()
student2.getDetails()
student2.showDetails()

'''


'''
#draw circle
import pygame

# Initialize Pygame
pygame.init()

# Create a surface to draw on
screen = pygame.display.set_mode((800, 600))

# Set the window title
pygame.display.set_caption("Drawing a Circle")

# Create a clock object
clock = pygame.time.Clock()

# Run the main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw a circle
    pygame.draw.circle(screen, (255, 0, 0), (400, 300), 50)

    # Update the display
    pygame.display.update()

    # Limit the framerate
    clock.tick(60)

'''