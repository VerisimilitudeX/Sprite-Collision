"""
LESSON: 5.3 - Sprite Collision
INSTRUCTION 1
"""

import pygame
import tsk
import random
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("FantasyPlains.jpg", 0, 0)
wizard_sheet = tsk.ImageSheet("WizardWalking.png", 4, 6)
wizard = tsk.Sprite(wizard_sheet, 0, 250)
dragon_sheet = tsk.ImageSheet("DragonFlying.png", 4, 6)
dragon = tsk.Sprite(dragon_sheet, 600, 50)

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    # Move the wizard
    wizard.center_x += 0.2 * c.get_time()
    if pygame.sprite.collide_rect(wizard, dragon):
        wizard.center_x = 0
    x, y = pygame.mouse.get_pos()
    if dragon.rect.collidepoint(x, y):  
        dragon.update(c.get_time())
    wizard.update(c.get_time())

    background.draw()
    dragon.draw()
    wizard.draw()

    pygame.display.flip()
    c.tick(30)