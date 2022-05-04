"""
LESSON: 5.3 - Sprite Collision
WARMUP 4
"""

import pygame
import tsk
import random
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("LivingRoom.jpg", 0, 0)
ball1 = tsk.Sprite("TennisBall.png", 50, 200)
ball2 = tsk.Sprite("TennisBall.png", 500, 500)

h_speed_1 = random.randint(1, 5) * .1
v_speed_1 = random.randint(1, 5) * .1
h_speed_2 = random.randint(1, 5) * .1
v_speed_2 = random.randint(1, 5) * .1

drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False


    # Check for collision
    if pygame.sprite.collide_rect(ball1, ball2):
        h_speed_1 = 0
        v_speed_1 = 0
        h_speed_2 = 0
        v_speed_2 = 0

    # Move the balls
    ball1.center_x += h_speed_1 * c.get_time()
    ball1.center_y += v_speed_1 * c.get_time()
    ball2.center_x += h_speed_2 * c.get_time()
    ball2.center_y += v_speed_2 * c.get_time()

    # Bounce on edges
    if ball1.center_x < 0 or ball1.center_x > 1018:
        h_speed_1 *= -1
    if ball1.center_y < 150 or ball1.center_y > 573:
        v_speed_1 *= -1

    if ball2.center_x < 0 or ball2.center_x > 1018:
        h_speed_2 *= -1
    if ball2.center_y < 180 or ball2.center_y > 573:
        v_speed_2 *= -1

    # Draw
    background.draw()
    ball1.draw()
    ball2.draw()

    pygame.display.flip()
    c.tick(30)