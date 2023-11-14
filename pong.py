"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BROWN = (173, 78, 26)


def draw_stick_figure(screen, x, y):
    # Head
    pygame.draw.ellipse(screen, BLACK, [1+x,y,10,10], 0)
 
    # Legs
    pygame.draw.line(screen, BLACK ,[5+x,17+y], [10+x,27+y], 2)
    pygame.draw.line(screen, BLACK, [5+x,17+y], [x,27+y], 2)
 
    # Body
    pygame.draw.line(screen, RED, [5+x,17+y], [5+x,7+y], 2)
 
    # Arms
    pygame.draw.line(screen, RED, [5+x,7+y], [9+x,17+y], 2)
    pygame.draw.line(screen, RED, [5+x,7+y], [1+x,17+y], 2)

pygame.init()

x=int(120)
y=int(100)



x1 = int(input("The place you throw the ball in x-axis: "))
y1 = int(input("The place you throw the ball in y-axis: "))
x2 = x1 + 120
y2 = y1 + 100


x_movement = (x1/y1)/2
y_movement = 0.5
# Game logic


pygame.mouse.set_visible(False)
# Drawing section


# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    pos = pygame.mouse.get_pos()
    x_stick = pos[0]
    y_stick = pos[1]
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    draw_stick_figure(screen, x_stick, y_stick)
    pygame.draw.rect(screen, BROWN, [120, 100, 500, 200],2)
    #player1 controlling paddle
    pygame.draw.line(screen, GREEN, [120, y_stick-25], [120, y_stick+25], 4)
    #player2 controlling paddle
    pygame.draw.line(screen, GREEN, [620, 100], [620, 150], 4)
    pygame.draw.ellipse(screen, BLACK, [x2,y2,50,50], 2)
    if (((x1 <= 0 and x1 >= -5) and (y2 >= y_stick-25 and y2 <= y_stick+25)) or x1 >= 450) :
      x_movement = x_movement * (-1)
    if (y1 <= 0 or y1 >= 150) :
      y_movement = y_movement * (-1)
    
    if x1 <= -5:
       
       x1 = 5
       y1 = 5

    
    x1 = x1 + x_movement
    y1 = y1 + y_movement
    x2 = x1 + 120
    y2 = y1 + 100
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(600)
 
# Close the window and quit.
pygame.quit()