# Bouncing Balls Simulation
# WorldOnAScreen (https://www.youtube.com/channel/UCJCSiOFqLz9sg6WZQ225jBg)
# Created 26th August 2015


# vh and vv are the horizontal and vertical velocities
# sh and sv are the horizontal and vertical displacements


import pygame
import random


# Constants (Arbitrary, non-SI units)
g = -250 # Acceleration of free-fall, set negative to fall downwards
e = 0.9 # Coefficient of restitution (by how much the speed changes on bounce)
t = 0.04 # Speed of simulation


background_colour = (255, 255, 235)
(width, height) = (800, 800)


class Ball(object):

    def __init__(self, (x, y), vh, vv, size):
        self.x = x
        self.y = y
        self.vh = vh
        self.vv = vv
        self.size = size
        self.colour = (255, 0, 0)

    def display(self):
        pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.size, 0)

    def move(self): # Use SUVAT equations to describe the motion of particles
        self.vv = self.vv - (g * t) # v = u + at
        sv = (self.vv * t) + (g * (0.5 * t * t)) # s = ut + (1/2)at^2
        sh = self.vh * t
        self.x += sh
        self.y += sv

    def bounce(self): # Collision with edges of window
        if self.y < self.size: # Top edge
            self.vv = -e * self.vv # Apply change in velocity
            self.y = self.size # Set position so it rests on the edge
                    
        elif self.x + self.size > width: # Right edge
            self.vh = -e * self.vh
            self.x = width - self.size
            
        elif self.y + self.size > height: # Bottom edge
            self.vv = -e * self.vv
            self.y = height - self.size
            
        elif self.x - size < 0: # Left edge
            self.vh = -e * self.vh
            self.x = size
                    

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncing Ball")


# Create the ball
size = 15
x = random.randint(200, 500)
y = random.randint(50,350)
vh = random.randint(100, 120)
vv = random.randint(-80, -60)
ball = Ball((x, y), vh, vv, size)


running = True
while running: # Keeps the window open until user quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background_colour)
    
    ball.move()
    ball.bounce()
    ball.display()

    pygame.display.flip()



# Note that when e is set to 1, the ball will appear to gain some energy on bouncing.
# This is due to the way in which the bounces are handled: instead of just changing the
# direction of the velocity, the ball is placed so that the side lies tangent to it.
# This prevents the ball from appearing to get 'stuck' to the side, at the cost of a
# small reduction in the accuracy of the simulation.
