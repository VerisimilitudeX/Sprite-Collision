"""
LESSON: 5.4 - Sprites in Lists
WARMUP 1
"""
import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("SkyMountains.jpg", 0, 0)
puffin_sheet = tsk.ImageSheet("Puffin_Fly.png", 5, 6)
puffin = tsk.Sprite(puffin_sheet, 0, 200)
sprite_list = [puffin]

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

        # Check for mouse down and reset puffin here
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if puffin.rect.collidepoint(mouse_x, mouse_y):
                puffin.center_x = 0

    background.draw()

    puffin.center_x += 0.2 * c.get_time()
    puffin.update(c.get_time())
    puffin.draw()
    pygame.display.flip()

    c.tick(30)