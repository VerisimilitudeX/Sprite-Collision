"""
LESSON: 5.3 - Sprite Collision
TECHNIQUE 1: React to Collision
DEMO 1
"""
import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("Stage.png", 0, 0)
bee = tsk.Sprite("Bee.png", 100, 400)
pug = tsk.Sprite("Pug.png", 800, 400)
pug_bee = tsk.Sprite("PugBee.png", 450, 400)
pug.flip_x = True
pug_bee.flip_x = True

have_met = False

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    if pygame.sprite.collide_rect(bee, pug):
        have_met = True

    background.draw()

    if have_met:
        pug_bee.center_y -= 0.1 * c.get_time()
        pug_bee.draw()

    else:
        bee.center_x += 0.1 * c.get_time()
        pug.center_x -= 0.1 * c.get_time()
        bee.draw()
        pug.draw()

    pygame.display.flip()
    c.tick(30)