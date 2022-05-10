import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("LivingRoom.jpg", 0, 0)
ball = tsk.Sprite("TennisBall.png", 0, 0)
vase1 = tsk.Sprite("BushVase1.png", 250, 400)
vase2 = tsk.Sprite("BushVase2.png", 350, -100)
vase3 = tsk.Sprite("BushVase3.png", 500, 400)

ball_x_speed = 0.15
ball_y_speed = 0.18

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    ball.center_x += ball_x_speed * c.get_time()
    ball.center_y += ball_y_speed * c.get_time()

    if pygame.sprite.collide_rect(ball, vase1):
        ball_y_speed = -0.18
    
    if pygame.sprite.collide_rect(ball, vase2):
        ball_y_speed = 0.18

    if pygame.sprite.collide_rect(ball, vase3):
        ball_y_speed = -0.18

    if ball.center_x >= 1018 or ball.center_y >= 573 or ball.center_y <= 0:
        drawing = False

    background.draw()
    vase2.draw()
    ball.draw()
    vase1.draw()
    vase3.draw()

    pygame.display.flip()

    c.tick(30)
