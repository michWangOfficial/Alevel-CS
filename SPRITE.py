import pygame
import random
 
# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0) 

alien_x = 1
alien_y = 0
leftOrRight = 1


class Alien(pygame.sprite.Sprite):
 
    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its size. """
 
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
 
class Base(pygame.sprite.Sprite):
    
 
    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its size. """
 
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()

# Initialize Pygame
pygame.init()
 
# Set the height and width of the screen
screen_width = 700
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])
 
# This is a list of all the alien
alien_list = pygame.sprite.Group()
 
# This is a list of every Base
base_list = pygame.sprite.Group()

# This is a list of all the Sprite
all_sprite_list = pygame.sprite.Group()
 

#Creating some aliens
for i in range(14):
    # This represents a block
    alien = Alien(BLACK, 20, 15)
 
    if i >= 0 and i <= 4:
        alien.rect.x = 100*i+80
        alien.rect.y = 90
    
    if i >= 5 and i <= 8:
        alien.rect.x = 100*i-370
        alien.rect.y = 195

    if i >= 9 and i <= 13:
        alien.rect.x = 100*i-820
        alien.rect.y = 300
 
    # Add the block to the list of objects
    alien_list.add(alien)
    all_sprite_list.add(alien)
 
#Creating some bases
for i in range(3):
    
    base = Base(GREEN,100,20)

    base.rect.x = 185*i + 70
    base.rect.y = 550
    base_list.add(base)
    all_sprite_list.add(base)
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
score = 0
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
    
    
    # Clear the screen
    screen.fill(WHITE)
    #buliding aliens and bases
    
    
    
    for alien in alien_list:
        alien.rect.x += leftOrRight
    alien_x += leftOrRight

    if alien_x == 0:
        leftOrRight = leftOrRight*-1 
        for alien in alien_list: 
            alien.rect.y += 10 

    if alien_x == 150:
        leftOrRight = leftOrRight*-1
        for alien in alien_list:
            alien.rect.y += 10  



    alien_list.draw(screen)
    base_list.draw(screen)
 
    
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)
 
pygame.quit()