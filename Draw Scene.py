import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("Desert.jpg", 0, 0)
crab = tsk.Sprite("RockCrab.png", 230, 250)
rock1 = tsk.Sprite("BrownRock1.png", 100, 200)
rock2 = tsk.Sprite("BrownRock2.png", 400, 350)
rock3 = tsk.Sprite("BrownRock3.png", 700, 100)
rock4 = tsk.Sprite("RoundGemPink.png", 700, 400)

sprite_list = [background, rock1, rock2, rock3, rock4]

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False
            
    for sprite in sprite_list:
        sprite.update(c.get_time())
        sprite.draw
        
    pygame.display.flip()
    c.tick(30)
