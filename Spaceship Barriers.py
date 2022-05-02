"""
LESSON: 5.3 - Sprite Collision
TECHNIQUE 3: Sprite Walls
PRACTICE 1
"""
import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("Space.jpg", 0, 0)
ship_sheet = tsk.ImageSheet("RoundShipSpin.png", 5, 3)
ship = tsk.Sprite(ship_sheet, 100, 300)
barrier = tsk.Sprite("ForceBarrier.png", 600, 0)

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False
    
    old_center = ship.center
    
    if tsk.is_key_down(pygame.K_LEFT):
        ship.center_x -= 0.2 * c.get_time()

    if tsk.is_key_down(pygame.K_RIGHT):
        ship.center_x += 0.2 * c.get_time()
    
    if pygame.sprite.collide_rect(ship, barrier):
        ship.center = old_center

    background.draw()
    barrier.draw()
    ship.draw()
    ship.update(c.get_time())

    pygame.display.flip()
    c.tick(30)


# Turn in your Coding Exercise.
