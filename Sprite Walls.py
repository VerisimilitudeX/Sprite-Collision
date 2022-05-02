"""
LESSON: 5.3 - Sprite Collision
TECHNIQUE 3: Sprite Walls
DEMO 1
"""
import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("Grass.jpg", 0, 0)
ball = tsk.Sprite("GolfBall.png", 50, 250)
bush = tsk.Sprite("BushesRight.png", 600, 350)

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    # old_center is the position the ball was in on the previous frame
    old_center = ball.center
    x, y = pygame.mouse.get_pos()
    
    ball.center = x, y
    
    if pygame.sprite.collide_rect(ball, bush):
        ball.center = old_center

    background.draw()
    bush.draw()
    ball.draw()

    pygame.display.flip()
    c.tick(30)