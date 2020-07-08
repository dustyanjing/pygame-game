import pygame


class Player(object):
    walkRight = [pygame.image.load('l1.png'), pygame.image.load('l2.png'), pygame.image.load('l3.png')]
    walkLeft = [pygame.image.load("fl1.png"), pygame.image.load("fl2.png"), pygame.image.load("fl3.png")]
    char = pygame.image.load("l1.png")

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.hp = 2
        self.walkCount = 0
        self.hit_box = (self.x, self.y, 50, 80)

    def draw(self, win):
        if self.walkCount >= 15:
            self.walkCount = 0

        if self.left:
            win.blit(self.walkLeft[self.walkCount // 5], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(self.walkRight[self.walkCount // 5], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.char, (self.x, self.y))
        self.hit_box = (self.x, self.y, 50, 80)
        #pygame.draw.rect(win, (255, 0, 0), self.hit_box, 2)
        pygame.draw.rect(win, (255, 128, 0), (self.hit_box[0], self.hit_box[1] - 10, 50, 8))
        pygame.draw.rect(win, (0, 128, 0), (self.hit_box[0], self.hit_box[1]-10, 50-self.hp*25, 8))


