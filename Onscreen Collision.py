"""
LESSON: 5.3 - Sprite Collision
TECHNIQUE 2: Onscreen Button
DEMO 1
"""
import pygame
import tsk
import random
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("CodeUI.jpg", 0, 0)
button = tsk.Sprite("MysteryButton.png", 420, 250)

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if button.rect.collidepoint(x, y):
                button.center_x = random.randint(269, 699)
                button.center_y = random.randint(297, 353)

    window.fill((0, 0, 0))
    background.draw()
    button.draw()

    pygame.display.flip()
    c.tick(30)