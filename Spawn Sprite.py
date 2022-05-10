import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("OutdoorHills.jpg", 0, 0)
beehive = tsk.Sprite("Beehive.png", 50, 100)
bees = []

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Bee!")
            bee = tsk.Sprite("Bee.png", beehive.center_x, beehive.center_y)
            bees.append(bee)

    for bee in bees:
        bee.center_x += 0.5 * c.get_time()

    background.draw()
    beehive.draw()
    for bee in bees:
        bee.draw()

    pygame.display.flip()
    c.tick(30)
