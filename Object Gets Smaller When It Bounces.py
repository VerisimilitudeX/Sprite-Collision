import pygame
import tsk
import random
pygame.init()


window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("Frame.jpg", 0, 0)

ball1 = tsk.Sprite("BigFire.png", 50, 200)

ball2 = tsk.Sprite("BigFire.png", 500, 500)

 

h_speed_1 = random.randint(1, 4) * .1

v_speed_1 = random.randint(1, 4) * .1

h_speed_2 = random.randint(1, 4) * .1

v_speed_2 = random.randint(1, 4) * .1

 

drawing = True

while drawing:

 

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            drawing = False

 

    if pygame.sprite.collide_rect(ball1,ball2):

        x = random.randint(0,1)

        if x == 0:

            ball1.scale += 0.1

            ball2.scale -= 0.1

        else:

            ball2.scale += 0.1

            ball1.scale -= 0.1

 

    ball1.center_x += h_speed_1 * c.get_time()

    ball1.center_y += v_speed_1 * c.get_time()

    ball2.center_x += h_speed_2 * c.get_time()

    ball2.center_y += v_speed_2 * c.get_time()

 

    if ball1.center_x < 0 or ball1.center_x > 1018:

        h_speed_1 *= -1

    if ball1.center_y < 150 or ball1.center_y > 573:

        v_speed_1 *= -1

 

    if ball2.center_x < 0 or ball2.center_x > 1018:

        h_speed_2 *= -1

    if ball2.center_y < 180 or ball2.center_y > 573:

        v_speed_2 *= -1

 

    background.draw()

    ball1.draw()

    ball2.draw()

 

    pygame.display.flip()

    c.tick(30)
