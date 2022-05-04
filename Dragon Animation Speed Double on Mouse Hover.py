"""
LESSON: 5.3 - Sprite Collision
WARMUP 3
"""

import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("FantasyPlains.jpg", 0, 0)
sheet = tsk.ImageSheet("DragonFlying.png", 4, 6)
dragon = tsk.Sprite(sheet, 350, 100)
dragon.image_animation_rate = 30

drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    # Check for mouse collision
    x, y = pygame.mouse.get_pos()
    if dragon.rect.collidepoint(x, y):
        dragon.image_animation_rate = 60
    else:
        dragon.image_animation_rate = 30

    dragon.update(c.get_time())
    background.draw()
    dragon.draw()

    pygame.display.flip()

    c.tick(30)