import pygame
import sys


pygame.init()
size = width, height = 500, 500
win = pygame.display.set_mode((width, height))  # 窗口的尺寸
pygame.display.set_caption('pikaqiu')  # 窗口的名字


class BG(object):
    def __init__(self, x, y):
        self.image = pygame.image.load("bg1.jpg")
        self.x = x
        self.y = y
        self.hit = []

    def draw(self):
        self.hit = [pygame.draw.rect(win, (255, 255, 0), (self.x + 260, self.y + 404, 150, 190), 1),
                    pygame.draw.rect(win, (255, 255, 0), (self.x + 484, self.y + 212, 150, 190), 1),
                    pygame.draw.rect(win, (255, 255, 0), (self.x + 176, self.y + 184, 127, 90), 1),
                    pygame.draw.rect(win, (255, 255, 0), (self.x + 865, self.y + 305, 160, 240), 1)]
        win.blit(self.image, (self.x, self.y))


class Player(object):
    walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png')]
    walkLeft = [pygame.image.load("l1.png"), pygame.image.load("l2.png"), pygame.image.load("l3.png")]
    walkUP = [pygame.image.load("UP1.png"), pygame.image.load("UP2.png"), pygame.image.load("UP3.png")]
    walkDOWN = [pygame.image.load("d1.png"), pygame.image.load("d2.png"), pygame.image.load("d3.png")]
    walk = pygame.image.load("d1.png")

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.jumpCount = 10
        self.left = True
        self.right = False
        self.up = False
        self.down = False
        self.hp = 2
        self.walkCount = 0
        self.hit_box = (self.x, self.y, 50, 80)

    def draw(self, win):
        if self.walkCount >= 18:
            self.walkCount = 0
        if self.up:
            win.blit(self.walkUP[self.walkCount // 6], (self.x, self.y))
            self.walkCount += 1
        elif self.down:
            win.blit(self.walkDOWN[self.walkCount // 6], (self.x, self.y))
            self.walkCount += 1
        elif self.left:
            win.blit(self.walkLeft[self.walkCount // 6], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(self.walkRight[self.walkCount // 6], (self.x, self.y))
            self.walkCount += 1


speed = [1, 1, 1, 1]
bg = BG(0, 0)
char = Player(50, 200)
clock = pygame.time.Clock()
while True:

    clock.tick(70)
    w = pygame.draw.rect(win, (255, 0, 0), (char.x, char.y, 27, 30), 1)
    bg.draw()
    char.draw(win)
    for i in bg.hit:
        if pygame.Rect.colliderect(i, w):
            if char.left:
                bg.x -= 1
            if char.right:
                bg.x += 1
            if char.up:
                bg.y -= 1
            if char.down:
                bg.y += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        bg.x += speed[0]
        if bg.x >= 1:
            bg.x = 1
            char.x -= 1
        if char.x <= 0:
            char.x = 0
        char.left = True
        char.right = False
        char.up = False
        char.down = False
    elif keys[pygame.K_RIGHT]:
        bg.x -= speed[1]
        if bg.x <= -750:
            bg.x = -750
            char.x += 1
        if char.x >= width - 50:
            char.x = width - 50
        char.right = True
        char.left = False
        char.up = False
        char.down = False
    elif keys[pygame.K_UP]:
        bg.y += speed[2]
        if bg.y >= 1:
            bg.y = 1
            char.y -= 1
        if char.y <= 0:
            char.y = 0
        char.up = True
        char.left = False
        char.right = False
        char.down = False
    elif keys[pygame.K_DOWN]:
        bg.y -= speed[3]
        if bg.y <= -174:
            bg.y = -174
            char.y += 1
        if char.y >= height - 50:
            char.y = height - 50
        char.down = True
        char.left = False
        char.right = False
        char.up = False
    else:
        char.walkCount = 0


    pygame.display.update()



