# Bouncing Balls Simulation
# WorldOnAScreen (https://www.youtube.com/channel/UCJCSiOFqLz9sg6WZQ225jBg)
# Created 14th September 2015


# vv is the vertical velocity
# sv is the vertical displacement


import pygame
import random
import math


# Constants (Created through trial and error rather than using SI units)
g = -150 # Acceleration of free-fall, set negative to fall downwards
e = 0.95 # Coefficient of restitution (by how much the speed changes on bounce with ground)
eball = 0.95 # Coefficient of restitution between balls
t = 0.04 # Speed of simulation (time between successive calls of physics engine, in arbitrary units)


background_colour = (255, 255, 235)
(width, height) = (100, 700)


class Ball(object):

    def __init__(self, (x, y), vv, size):
        self.x = x
        self.y = y
        self.vv = vv
        self.size = size
        self.colour = (255, 0, 0)
        self.mass = size ** 3 # Assume mass is proportional to the volume of the balls (so proportional to volume)

    def display(self):
        pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.size, 0)

    def move(self): # Use SUVAT equations to create motion
        self.vv = self.vv - (g * t) # v = u + at
        sv = (self.vv * t) + (g * (0.5 * t * t)) # s = ut + (1/2)at^2
        self.y += sv

    def bouncewall(self): # Check for collision with walls                
        if self.y + self.size > height: # Bottom edge
            self.vv = -e * self.vv
    
    def bounceball(self): # Instructions for collision with ball directly above it
        balltocheck = balls.index(self) + 1 # Identifies the ball that is directly above self
        if balltocheck < len(balls): # Prevents searching for a ball above the top ball
            otherball = balls[balltocheck]
            if abs(self.y - otherball.y) < (self.size + otherball.size): # Determines whether or not the ball above self is in contact with self
                self.vv = ((self.mass * self.vv) + (otherball.mass * otherball.vv) - (otherball.mass * eball) * (self.vv - otherball.vv))/(self.mass + otherball.mass) # Change velocity of both balls (collide)
                otherball.vv = ((otherball.mass * otherball.vv) + (self.mass * self.vv) - (self.mass * eball) * (otherball.vv - self.vv))/(otherball.mass + self.mass)
                otherball.y = self.y - self.size - otherball.size # Prevents the balls from overlapping



screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncing Ball")


# Create the balls
numberofballs = 3
scalefactor = 0.6 # The scale factor by which the ball's radius is reduced with each successive ball (doesn't work well for larger numbers)
balls = []
ballheight = 600 # Initial height of bottom ball (remember that a greater number means further down the screen)
ballsize = 30 # Radius of the bottom ball
for i in range(numberofballs):
    ball = Ball((width/2, ballheight), 0, ballsize)
    balls.append(ball)
    ballheight -= int(ballsize + ballsize * scalefactor)
    ballsize = int(ballsize * scalefactor)


running = True
while running: # Keeps the window open until user quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background_colour)
    
    for ball in balls:
        ball.move()
        ball.bounceball()
        ball.bouncewall()
        ball.display()

    pygame.display.flip()
