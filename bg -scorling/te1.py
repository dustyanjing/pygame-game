import pygame, sys

pygame.init()
size = width, height = 1250, 674
win = pygame.display.set_mode((width, height))  # 窗口的尺寸
pygame.display.set_caption('pikaqiu')  # 窗口的名字
bg = pygame.image.load("bg1.jpg")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            print('[pygame.MOUSEMOTION]',event.pos,event.rel,event.buttons)
    win.blit(bg, (0, 0))
    pygame.draw.rect(win, (255, 255, 0), (260, 404, 155, 195), 1)
    pygame.draw.rect(win, (255, 255, 0), (484, 212, 155, 195), 1)
    pygame.draw.rect(win, (255, 255, 0), (176, 184, 132, 102), 1)
    pygame.draw.rect(win, (255, 255, 0), (865, 305, 160, 245), 1)
    pygame.display.update()