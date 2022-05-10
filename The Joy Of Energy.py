import tsk



import pygame



import random

pygame.init()



pygame.display.set_mode([1018, 573])


c = pygame.time.Clock()


background = tsk.Sprite("ScienceLab.jpg", 0, 0)


robot = tsk.Sprite("RobotOff.png", 420, 200)


robot_on = False


drawing = True

while drawing:


    for event in pygame.event.get():

        if event.type == pygame.QUIT:


            drawing = False

        elif event.type == pygame.MOUSEBUTTONDOWN:


            x, y = pygame.mouse.get_pos()


            mouse = robot.rect.collidepoint(x, y)

            if robot_on == True:

                robot_on = False

                robot.image = "RobotOff.png"


            else:


                robot_on = True


                robot.image = "RobotDance.png"


    if robot_on == True:

 
        x, y = robot.center

 
        timing_adjust = c.get_time() * 0.1

 

        x += random.randint(-4, 4) * timing_adjust

 
        y += random.randint(-4, 4) * timing_adjust

 
        robot_center = x, y

 
        if random.randint(1, 5) == 1:

            if robot.flip_x:

                robot.flip_x = False

            else:

                robot.flip_x = True


    background.draw()

    robot.draw()


    c.tick(30)

    pygame.display.flip()

