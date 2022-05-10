import pygame
import tsk
import random

pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("Space.jpg", 0, 0)
ship = tsk.Sprite("RoundShip.png", 0, 0)
planet = tsk.Sprite("DesertPlanet.png", 800, 200)

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False
    have_met = False
    x, y = pygame.mouse.get_pos()
    ship.center = x, y
    if pygame.sprite.collide_rect(ship, planet):
        have_met = True

    if have_met:
        planet.center_x = random.randint(0, 573)
        planet.draw()
        
    background.draw()
    planet.draw()
    ship.draw()

    pygame.display.flip()
    c.tick(30)
