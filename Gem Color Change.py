import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("Desert.jpg", 0, 0)
gem = tsk.Sprite("RoundGemBlue.png", 320, 230)
gem_timer = 0

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if gem.rect.collidepoint(x, y):
                gem.image = "RoundGemRed.png"
                
    if gem.image == "RoundGemRed.png":
        gem_timer += c.get_time()
        if gem_timer > 1000:
            gem_timer = 0
            gem.image = "RoundGemBlue.png"

    background.draw()
    gem.draw()

    pygame.display.flip()
    c.tick(30)
