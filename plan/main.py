
import pygame
import sys
import random


pygame.init()
Window = pygame.display.set_mode((640, 960))
BG = pygame.image.load('bg.png')

SM = pygame.mixer.Sound("boom.wav")
pygame.mixer.music.load("bgm.wav")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1, 0)


class BOSS(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("BOSS.png")
        self.rect = self.image.get_rect()
        self.show = False
        self.bullet = pygame.image.load("bullet_p.png")
        self.bullet_rect = self.bullet.get_rect()
        self.speed = [random.randint(1, 5), random.randint(1, 5)]
        self.width, self.height = 19, 19
        self.bu = []

    def draw(self):
        Window.blit(self.image, (40, 60))
        self.show = True


class BOSS_B(pygame.sprite.Sprite):

    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("bullet_p.png")
        self.rect = self.image.get_rect()
        self.show = False
        self.speed = [random.randint(1, 5), random.randint(1, 5)]
        self.width, self.height = 19, 19
        self.rect.left, self.rect.top = position

    def move(self):
        self.rect = self.rect.move(self.speed[0], self.speed[1])
        if self.rect.right < 0:
            self.rect.left = 640
        elif self.rect.left > 640:
            self.rect.right = 0
        elif self.rect.bottom < 0:
            self.rect.top = 960
        elif self.rect.top > 960:
            self.rect.bottom = 0


class ENEMY(pygame.sprite.Sprite):

    def __init__(self, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('enemy_p.png')
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = random.randint(0, 550), random.randint(-600, 0)

    def move(self):
        if self.rect.top < 960:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.rect.left, self.rect.top = random.randint(0, 550), random.randint(-600, 0)


class BULLET(pygame.sprite.Sprite):

    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('bullet_2.png')
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = 10
        self.active = True
        self.mark = pygame.mask.from_surface(self.image)

    def move(self):
        self.rect.top -= self.speed

    def reset(self, position):
        self.rect.left, self.rect.top = position
        self.active = True


class PLAYER(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('player_p.png')
        self.rect = self.image.get_rect()
        self.rect.width = 127
        self.rect.height = 127
        self.rect.left, self.rect.top = position

    def move(self):
        self.rect.top = event.pos[1] - 50
        self.rect.left = event.pos[0] - 50

    def draw(self):
        Window.blit(self.image, (self.rect.left, self.rect.top))


class sup(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('bullet_2.png')
        self.rect = self.image.get_rect()
        self.rect.left = random.randint(0, 550)
        self.rect.top = random.randint(-1000, -100)

    def move(self):
        self.rect.top += 3
        if self.rect.top >= 960:
            self.rect.top = random.randint(-1000, -100)
            self.rect.left = random.randint(0, 550)
        Window.blit(self.image, self.rect)

    def reset(self):
        self.rect.left = random.randint(0, 550)
        self.rect.top = random.randint(-1000, -100)


FPS = 500
sCOUNT = 0
E_LOSE = []
LOSE = False
lose_count = 0
B1 = []
B2 = []
B2D = False

E1 = []
sup = sup()
boss = BOSS()
boss_b = []
boss_HP = 100
HP = 3
score = 0
CLOCK = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 30, True)
P1 = PLAYER([250, 650])

run = True

for i in range(5):
    E1.append(ENEMY(random.randint(1, 3)))

for j in range(7):
    boss_b.append(BOSS_B([100, 100]))


def draw():
    if score >= 5:
        global boss_HP
        global run
        global HP
        boss.draw()
        E1.clear()
        for shut in boss_b:
            shut.move()
            SM.play()
            Window.blit(shut.image, shut.rect)
            if pygame.Rect.colliderect(shut.rect, P1.rect):
                HP -= 1
                boss_b.pop(boss_b.index(shut.rect))
        for hit in B1:
            if pygame.Rect.colliderect(hit.rect, boss.rect):
                B1.pop(B1.index(hit.rect))
                boss_HP -= 1
        for hit1 in B2:
            if pygame.Rect.colliderect(hit1.rect, boss.rect):
                B2.pop(B2.index(hit1.rect))
                boss_HP -= 1
    if boss_HP == 0:
        text_win = font.render("YOU  WIN", 16, (0, 0, 0))
        Window.blit(text_win, (200, 500))
        run = False

    P1.draw()
    sup.move()
    text_SCORE = font.render('Score: ' + str(score), 1, (0, 0, 0))
    text_HP = font.render('HP: ' + str(HP), 1, (0, 0, 0))

    Window.blit(text_SCORE, (0, 0))
    Window.blit(text_HP, (0, 30))
    for e in E1:
        e.move()
        Window.blit(e.image, e.rect)
    if LOSE:
        text_LOSE = font.render("YOU  LOSE", 16, (0, 0, 0))
        Window.blit(text_LOSE, (200, 500))
    pygame.display.update()


while run:
    CLOCK.tick(FPS)
    Window.blit(BG, (0, 0))

    if sCOUNT >= 0:
        sCOUNT += 1
    if sCOUNT >= 40:
        sCOUNT = 0
        B1.append(BULLET(P1.rect.midtop))
        B2.append(BULLET((P1.rect.left, P1.rect.top)))
    for b in B1:
        if b.rect.top <= 0:
            B1.pop(B1.index(b))
        if b.active:
            b.move()
            Window.blit(b.image, b.rect)
    if B2D:
        for b in B2:
            if b.rect.top <= 0:
                B2.pop(B2.index(b))
            if b.active:
                b.move()
                Window.blit(b.image, b.rect)
    draw()

    if pygame.Rect.colliderect(P1.rect, sup.rect):
        sup.reset()
        B2D = True

    for each in E1:
        for i in B1:
            if pygame.Rect.colliderect(i.rect, each.rect):
                B1.pop(B1.index(i))
                each.reset()
                score += 1
        for j in B2:
            if pygame.Rect.colliderect(j.rect, each.rect):
                B2.pop(B2.index(j))
                each.reset()
                score += 1
        if pygame.Rect.colliderect(each.rect, P1.rect):
            each.reset()
            HP -= 1

    if HP <= 0:
        HP = 0
        run = False

    for each in E1:
        if each.rect.top >= 960:
            score -= 5
        if pygame.Rect.colliderect(P1.rect, each.rect):
            HP -= 1
            each.reset()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            if event.buttons[0] == 1:
                P1.move()

