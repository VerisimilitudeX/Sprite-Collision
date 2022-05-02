"""
LESSON: 5.3 - Sprite Collision
EXERCISE: The Joy Of Energy
"""

#### ---- SET UP ---- ####

# --- Libraries ---  #

# Import the tsk library
import tsk

# Import the pygame library
import pygame

# Import the random library
import random

# Initialize pygame
pygame.init()

# --- Animation variables --- #

# Open a new window of size [1018, 573] and assign to
# window
window = pygame.display.set_mode([1018, 573])

# Create a new Clock and assign it to c
c = pygame.time.Clock()

# Create a new SPRITE object called background
# using the "ScienceLab.jpg" image at (0, 0)
background = pygame.Sprite("Sciencelab.jpg", 0, 0)

# Create a new SPRITE object called robot
# using the "RobotOff.png" image at (420, 200)
robot = pygame.Sprite("RobotOff.png", 420, 200)

# Create a new boolean called robot_on, set to False
robot_on = False

#### ---- MAIN LOOP ---- ####

# Create a variable called drawing and assign it True
drawing = True

# Loop while drawing
while drawing:

    # --- Event loop --- #

    # Create an event loop
    for event in pygame.event.get():

        #  If the event is equal to the QUIT event
        if event.type == pygame.QUIT:

            # Set drawing to False
            drawing = False

        # --- Mouse input --- #

        # Elif the event type is MOUSEBUTTONDOWN
        elif event.type == pygame.MOUSEBUTTONDOWN:

            # Store the mouse position in x, y
            x, y = pygame.mouse.get_pos()

            # Use COLLIDEPOINT to see if the mouse
            # overlaps with the robot
            robot_on = robot.rect.collidepoint(x, y)

                # If robot_on is True
                if robot_on == True:

                    # Set robot_on to False
                    robot_on = False

                    # Set the IMAGE of the robot to
                    # "RobotOff.png"
                    robot.image = "RobotOff.png"

                # Else
                else:

                    # Set robot_on to True
                    robot_on = True

                    # Set the IMAGE of the robot to
                    # "RobotDance.png"
                    # ---> TEST AFTER THIS LINE <--- #
                    robot.image = "RobotDance.png"

    # --- Move robot --- #

    # If robot_on is true
    if robot_on == True:

        # Store the robot's CENTER
        # position in variables x and y
        x, y = robot.center

        # Declare a variable called timing_adjust
        # set to c.get_time() * 0.1
        timing_Adjust = c.get_time() * 0.1

        # Increment x by a random number between -4
        # and 4 multiplied by timing_adjust
        x += random.randint(-4, 4) * timing_adjust

        # Increment y by a random number between -4
        # and 4 multiplied by timing_adjust
        y += random.randint(-4, 4) * timing_adjust

        # Set the robot's CENTER back to x, y
        # ---> TEST AFTER THIS LINE <--- #
        robot.center = x, y

        # If a random number between 1 and
        # 5 is equal to 1
        if random.randint(1, 5) == 1:

            # Set the robot's flip x to the
            # opposite of itself
            # ---> TEST AFTER THIS LINE <--- #
            if robot.flip_x:
                robot.flip_x = False
            else:
                robot.flip_x = True

    # --- Animate and draw --- #

    # DRAW the background
    background.draw

    # DRAW the robot
    robot.draw
    
    # Tick c with a framerate of 30
    c.tick(30)

    # Flip the display
    # ---> TEST AFTER THIS LINE <--- #
    pygame.display.flip()

# Turn in your Coding Exercise.