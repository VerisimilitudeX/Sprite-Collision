import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("CodeUI.jpg", 0, 0)
yes_button = tsk.Sprite("YesButton.png", 270, 250)
no_button = tsk.Sprite("NoButton.png", 570, 250)

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if yes_button.rect.collidepoint(x, y):
                print("Yes!")
            if no_button.rect.collidepoint(x, y):
                print("No!")

    window.fill((0, 0, 0))
    background.draw()
    yes_button.draw()
    no_button.draw()

    pygame.display.flip()
    c.tick(30)
