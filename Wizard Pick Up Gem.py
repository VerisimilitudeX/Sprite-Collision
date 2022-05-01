"""
LESSON: 5.3 - Sprite Collision
TECHNIQUE 1: React to Collision
PRACTICE 1
"""
import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("OutdoorFantasy.jpg", 0, 0)
wizard = tsk.Sprite("Wizard.png", 0, 0)
gem = tsk.Sprite("RoundGemPink.png", 600, 400)

picked_up_gem = False

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    x, y = pygame.mouse.get_pos()
    wizard.center = x, y
    if pygame.sprite.collide_rect(wizard, gem):
        picked_up_gem = True
        
    if picked_up_gem:
        gem.center = x - 12, y + 18

    background.draw()
    wizard.draw()
    gem.draw()

    pygame.display.flip()
    c.tick(30)


# Turn in your Coding Exercise.
