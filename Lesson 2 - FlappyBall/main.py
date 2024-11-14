import pgzrun
from random import randint

TITLE = 'Flappy Ball'
WIDTH = 500
HEIGHT = 400

R = randint(0, 255)
G = randint(0, 255)
B = randint(0, 255)
CLR = (R, G, B)

GRAVITY=2000.0


#Class- Blueprint for ball
class Ball:
  #Properties/Attributes of ball class
  def __init__(self, initial_x, initial_y):
    self.x=initial_x
    self.y=initial_y
    self.vx=200 
    self.vy=0
    self.radius=40

  #Function/Methods
  def drawCircle(self):
    pos=(self.x,self.y)
    screen.draw.filled_circle(pos,self.radius,CLR)

#Object for ball class
ball=Ball(50,100)

def draw():
  screen.clear()
  screen.fill(color="grey")
  ball.drawCircle()

def update(dt):
  #Final velocity formula
  #v = u + (a*t)
  #v- final velocity, u- initial velocity , a- accelaration , t-time taken
  uy=ball.vy
  ball.vy = ball.vy + (GRAVITY *dt)

  #displacement
  #s = (u+v)/2*t
  ball.y += (uy + ball.vy) * 0.5 * dt

  if ball.y > HEIGHT:
    ball.y=HEIGHT - ball.radius
    #inelastic collision
    ball.vy =- ball.vy * 0.9

  ball.x += ball.vx*dt
  if ball.x > WIDTH - ball.radius or ball.x < ball.radius:
    ball.vx = -ball.vx

def on_key_down(key):
  if key == keys.UP:
    ball.vy = -500





pgzrun.go()

