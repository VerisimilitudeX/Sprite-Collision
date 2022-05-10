import tsk
import random
import pygame
pygame.init()

window = pygame.display.set_mode([1018, 573])

hills = tsk.Sprite("HillsGrassy.png", 1018, 573)
clouds = tsk.Sprite("Clouds.png", 1018, 573)
light = tsk.Sprite("LightSwitch.png", 200, 200)

sky = (231, 42, 53)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()

            if light.rect.collidepoint(x, y):
                r = random.randint(0,255)
                g = random.randint(0,255)
                b = random.randint(0,255)
                sky = [r,g,b]

    window.fill(sky)
    hills.draw()
    clouds.draw()
    light.draw()

    pygame.display.flip()      
