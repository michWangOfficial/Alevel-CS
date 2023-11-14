"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
import math
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255,0,0)
BLUE = (0,0,255)
ROOFBRICK = (192, 73, 56)
BROWN = (173, 78, 26)
SKYBLUE = (108, 210, 255)
FORESTGREEN = (166, 235, 121)
SUNYELLOW = (245, 214, 40)

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (800, 600)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
sun_surf = pygame.Surface((100, 100), pygame.SRCALPHA)
sun_rect = sun_surf.get_rect(topleft = ((50,100)))
print(sun_rect)
pygame.draw.circle(sun_surf, SUNYELLOW, (50,50), 50)
print(sun_rect.center)
rotate_center = (400,500)
dif_x = rotate_center[0] - sun_rect.center[0]
dif_y = rotate_center[1] - sun_rect.center[1]
radius = math.sqrt(dif_x**2+dif_y**2)
print(radius)
angle = math.degrees(math.atan(dif_y/dif_x))
print(sun_rect.center)
print(angle)
print(radius*(math.cos(angle)))
print(radius*(math.sin(math.radians(angle))))
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
     #draw the sun
    
    # --- Go ahead and update the screen with what we've drawn.
    screen.fill((255,255,255))
    screen.blit(sun_surf, sun_rect)
    pygame.display.flip()
    sun_rect.center = (
        rotate_center[0] - radius*(math.cos(math.radians(angle))),
        rotate_center[1] - radius*(math.sin(math.radians(angle))),
        )
    angle = angle+0.5
    # --- Limit to 60 frames per second
    clock.tick(60)
 

# Close the window and quit.
pygame.quit()