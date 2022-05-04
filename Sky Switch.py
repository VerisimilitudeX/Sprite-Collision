"""
LESSON: 5.3 - Sprite Collision
EXERCISE: Sky Switch
"""

#### ---- SET UP ---- ####

# --- Libraries ---  #

# Import and set up tsk, pygame, and random libraries
import tsk
import random
import pygame
pygame.init()


# --- Variables --- #

# Open a 1018 x 573 window
window = pygame.display.set_mode([1018, 573])

# Create three sprites with images "HillsGrassy.png",
# "Clouds.png", and "LightSwitch.png" (the field and
# clouds images are the full size of the window)
hills = tsk.Sprite("HillsGrassy.png", 1018, 573)
clouds = tsk.Sprite("Clouds.png", 1018, 573)
light = tsk.Sprite("LightSwitch.png", 200, 200)

# Create a starting color for the sky
sky = (231, 42, 53)

#### ---- MAIN LOOP ---- ####

# Create a main loop
running = True
while running:

    # --- Event loop --- #

    # Create an event loop
    # ---> TEST AFTER THESE LINES <--- #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # --- Mouse input --- #

        # If the mouse button was clicked, store the
        # current mouse position
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()

            # If the mouse position is over the switch,
            # create a random color and store it in the
            # sky color variable
            # ---> TEST AFTER THIS LINE <--- #
            if light.rect.collidepoint(x, y):
                r = random.randint(0,255)
                g = random.randint(0,255)
                b = random.randint(0,255)
                sky = [r,g,b]

    # --- Draw --- #

    # Fill the window with the sky color, then draw the
    # background, clouds, and switch on top of it
    window.fill(sky)
    hills.draw()
    clouds.draw()
    light.draw()
#
    # Flip the display
    # ---> TEST AFTER THIS LINE <--- #
    pygame.display.flip()      
    
# Turn in your Coding Exercise.
