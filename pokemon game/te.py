import pygame
import sys
import random

pygame.init()
size = width, height = 500, 500
win = pygame.display.set_mode((width, height))  # 窗口的尺寸
pygame.display.set_caption('POKEMON')  # 窗口的名字
pygame.mixer.music.load("m_1.wav")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1, 0)
SM = pygame.mixer.Sound("m_2.wav")


class BG(object):
    def __init__(self, x, y):
        self.image = pygame.image.load("bg1.jpg")
        self.image1 = pygame.image.load("jn1.ico")
        self.rect = self.image1.get_rect()
        self.x = x
        self.y = y
        self.hit = []
        self.ent = []

    def draw(self):
        self.rect = self.image1.get_rect()
        self.rect.left = self.x
        self.rect.top = self.y

        self.hit = [pygame.draw.rect(win, (255, 255, 0), (self.x + 260, self.y + 404, 150, 190), 1),
                    pygame.draw.rect(win, (255, 255, 0), (self.x + 484, self.y + 212, 150, 190), 1),
                    pygame.draw.rect(win, (255, 255, 0), (self.x + 176, self.y + 184, 127, 90), 1),
                    pygame.draw.rect(win, (255, 255, 0), (self.x + 865, self.y + 305, 160, 240), 1)]

        self.ent = [pygame.draw.rect(win, (255, 255, 0), (self.x + 226, self.y + 250, 30, 40), 1),
                    pygame.draw.rect(win, (255, 255, 0), (self.x + 355, self.y + 555, 30, 50), 1),
                    pygame.draw.rect(win, (255, 255, 0), (self.x + 580, self.y + 367, 30, 50), 1)]
        win.blit(self.image, (self.x, self.y))


class ball(object):
    def __init__(self, x, y):
        self.Ball = pygame.image.load("jn1.ico")
        self.rect = self.Ball.get_rect()
        self.rect.top = y
        self.rect.left = x

    def draw(self):
        win.blit(self.Ball, (self.rect.left, self.rect.top))


class FIGHT_MAP(object):
    def __init__(self):
        self.image = pygame.image.load("set1.png")
        self.back = pygame.image.load("set3.png")
        self.back_pos = pygame.draw.rect(win, (255, 255, 0), (200, 300, 15, 30), 1)

    def draw(self):

        win.blit(self.image, (0, 0))
        win.blit(self.back, (200, 300))


class FIGHT_MAP2(object):
    def __init__(self):
        self.image = pygame.image.load("set4.png")
        self.back = pygame.image.load("set3.png")
        self.back_pos = pygame.draw.rect(win, (255, 255, 0), (200, 450, 15, 30), 1)

    def draw(self):

        win.blit(self.image, (0, 0))
        win.blit(self.back, (200, 450))


class FIGHT_MAP3(object):
    def __init__(self):
        self.image = pygame.image.load("set5.png")
        self.image2 = pygame.image.load("d3.png")
        self.back_pos = pygame.draw.rect(win, (255, 255, 0), (50, 350, 50, 50), 1)
        self.back_pos1 = pygame.draw.rect(win, (255, 255, 0), (250, 40, 25, 25), 1)

    def draw(self):
        self.back_pos = pygame.draw.rect(win, (255, 255, 0), (50, 350, 50, 50), 1)
        win.blit(self.image, (0, 0))
        win.blit(self.image2, (250, 40))
        self.back_pos1 = pygame.draw.rect(win, (255, 255, 0), (250, 40, 25, 25), 1)


class FIGHT_MAP4(object):
    def __init__(self):
        self.image = pygame.image.load("set9.png")

    def draw(self):
        win.blit(self.image, (0, 0))


class poke(object):

    def __init__(self, x, y):
        self.p = [pygame.image.load("002.ico"), pygame.image.load("008.ico"), pygame.image.load("009.ico"),
                  pygame.image.load("010.ico"), pygame.image.load("048.ico"), pygame.image.load("019.ico"),
                  pygame.image.load("011.ico"), pygame.image.load("104.ico"), pygame.image.load("004.ico"),
                  pygame.image.load("019.ico"), pygame.image.load("092.ico"), pygame.image.load("027.ico")]
        self.image = self.p[random.randint(0, 7)]
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.lv = random.randint(1, 3)
        self.hp = random.randint(1, 3)
        self.dmg = random.randint(1, 3)
        self.speed = random.randint(1, 3)

    def draw(self):
        win.blit(self.image, (self.rect.left, self.rect.top))


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
        self.shut = False
        self.char_info = False
        self.char_pif = False
        self.hp = 2
        self.walkCount = 0
        self.hit_box = (self.x, self.y, 50, 80)
        self.w = pygame.draw.rect(win, (0, 0, 0), (self.x+9, self.y+2, 10, 26), 1)
        self.my_poke = []

    def draw(self):
        self.w = pygame.draw.rect(win, (0, 0, 0), (self.x+9, self.y+2, 10, 26), 1)
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


class jn_RL(object):
    def __init__(self, x, y, facing):
        self.image = pygame.image.load('jn1.ico')
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.speed = 3
        self.facing = facing

    def draw(self):
        if self.facing == -1:
            self.rect.left -= self.speed
            win.blit(self.image, (self.rect.left, self.rect.top))
            if self.rect.left <= 0:
                space.pop()
        if self.facing == 1:
            self.rect.left += self.speed
            win.blit(self.image, (self.rect.left, self.rect.top))
            if self.rect.left >= width:
                space.pop()
        if self.facing == 0:
            self.rect.top -= self.speed
            win.blit(self.image, (self.rect.left, self.rect.top))
            if self.rect.top <= 0:
                space.pop()
        if self.facing == 2:
            self.rect.top += self.speed
            win.blit(self.image, (self.rect.left, self.rect.top))
            if self.rect.top >= 400:
                space.pop()


class jn_UD(object):
    def __init__(self, x, y, UD):
        self.image = pygame.image.load('jn1.ico')
        self.image1 = pygame.image.load('jn1.ico')
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.speed = 3 * UD
        self.UD = UD

    def draw(self):
        if self.UD == -1:
            self.rect.top += self.speed
            win.blit(self.image, (self.rect.left, self.rect.top))
            if self.rect.top <= 0:
                spaceUD.pop()
        if self.UD == 1:
            self.rect.top += self.speed
            win.blit(self.image1, (self.rect.left, self.rect.top))
            if self.rect.top >= height:
                spaceUD.pop()


def ent():
    global map1
    text_SCORE = font.render('LV: ' + str(charLv), 1, (0, 0, 0))
    text_lvUP = font.render('EXP: ' + str(charEXP) + "/" + str(charEXPE), 1, (0, 0, 0))
    text_BALLNUB = font.render('ball: ' + str(ball_num), 1, (0, 0, 0))
    for i, j in L1:
        win.blit(i.image, j)
    bg.draw()
    char.draw()
    if len(poke1) <= 0:
        poke1.append(poke(random.randint(5, 350), random.randint(5, 350)))

    for wall in bg.hit:
        if pygame.Rect.colliderect(wall, char.w):
            if char.left:
                bg.x -= 1
            if char.right:
                bg.x += 1
            if char.up:
                bg.y -= 1
            if char.down:
                bg.y += 1
    if pygame.Rect.colliderect(bg.ent[0], char.w):
        map1 = 1
    if pygame.Rect.colliderect(bg.ent[1], char.w):
        map1 = 2
    if pygame.Rect.colliderect(bg.ent[2], char.w):
        map1 = 3
    if char.char_info:
        win.blit(info, (0, 0))
        win.blit(text_SCORE, (0, 0))
        win.blit(text_lvUP, (0, 40))
        win.blit(text_BALLNUB, (60, 0))
        for i, j in L1:
            win.blit(i.image, j)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_i]:
        char.char_info = True
    if keys[pygame.K_ESCAPE]:
        char.char_info = False
    if keys[pygame.K_LEFT]:
        bg.x += 1
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
        bg.x -= 1
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
        bg.y += 1
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
        bg.y -= 1
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


def ent1():
    global map1
    global charEXP
    global charLv
    global charEXPE
    global my_poke_x
    global ball_num
    text_SCORE = font.render('LV: ' + str(charLv), 1, (0, 0, 0))
    text_lvUP = font.render('HP: ' + str(charEXP) + "/" + str(charEXPE), 1, (0, 0, 0))
    text_BALLNUB = font.render('ball: ' + str(ball_num), 1, (0, 0, 0))
    charEXPE = charLv * 10
    door1.draw()
    for p in poke1:
        p.draw()
    char.draw()
    for lr in space:
        lr.draw()
        for p in poke1:
            if pygame.Rect.colliderect(p.rect, lr.rect):
                SM.play()
                my_poke_x += 30
                char.my_poke.append(poke1[poke1.index(p)])
                my_poke_posit.append(my_poke_y)
                poke1.pop(poke1.index(p))
                space.pop()
                charEXP += 1
                ball_num -= 1
    for j in spaceUD:
        j.draw()
        for p in poke1:
            if pygame.Rect.colliderect(p.rect, j.rect):
                SM.play()
                char.my_poke.append(poke1[poke1.index(p)])
                my_poke_x += 30
                my_poke_posit.append(my_poke_y)
                poke1.pop(poke1.index(p))
                spaceUD.pop()
                charEXP += 1
                ball_num -= 1
    if charEXP == charEXPE:
        charLv += 1
        charEXP = 0
    if pygame.Rect.colliderect(door1.back_pos, char.w):
        map1 = 0
    if char.char_info:
        win.blit(info, (0, 0))
        win.blit(text_SCORE, (0, 0))
        win.blit(text_lvUP, (0, 40))
        win.blit(text_BALLNUB, (60, 0))
        for i, j in L1:
            win.blit(i.image, j)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_i]:
        char.char_info = True
    if keys[pygame.K_ESCAPE]:
        char.char_info = False
    if keys[pygame.K_LEFT]:
        char.x -= 1
        if char.x <= 0:
            char.x = 0
        char.left = True
        char.right = False
        char.up = False
        char.down = False
    elif keys[pygame.K_RIGHT]:
        char.x += 1
        if char.x >= 500:
            char.x = 500
        char.right = True
        char.left = False
        char.up = False
        char.down = False
    elif keys[pygame.K_UP]:
        char.y -= 1
        if char.y <= 0:
            char.y = 0
        char.up = True
        char.left = False
        char.right = False
        char.down = False
    elif keys[pygame.K_DOWN]:
        char.y += 1
        if char.y >= 400:
            char.y = 400
        char.down = True
        char.left = False
        char.right = False
        char.up = False
    elif keys[pygame.K_SPACE]:
        if char.left:
            jn_RL.facing = -1
        if char.right:
            jn_RL.facing = 1
        if char.up:
            jn_RL.facing = 0
        if char.down:
            jn_RL.facing = 2
        if ball_num <= 0:
            space.clear()
        if ball_num >= 1:
            if len(space) <= 0:
                space.append(jn_RL(char.x, char.y, jn_RL.facing))
    else:
        char.walkCount = 0

    pygame.display.update()


def ent2():
    global charEXP
    global charLv
    global charEXPE
    global map1
    global ball_num
    text_SCORE = font.render('LV: ' + str(charLv), 1, (0, 0, 0))
    text_lvUP = font.render('HP: ' + str(charEXP) + "/" + str(charEXPE), 1, (0, 0, 0))
    text_BALLNUB = font.render('ball: ' + str(ball_num), 1, (0, 0, 0))
    charEXPE = charLv * 10
    door2.draw()
    char.draw()
    for get in my_sup:
        get.draw()
        if pygame.Rect.colliderect(get.rect, char.w):
            print(my_sup.pop(my_sup.index(get)))
            ball_num += 1
    if pygame.Rect.colliderect(door2.back_pos, char.w):
        map1 = 0
    if char.char_info:
        win.blit(info, (0, 0))
        win.blit(text_SCORE, (0, 0))
        win.blit(text_lvUP, (0, 40))
        win.blit(text_BALLNUB, (60, 0))
        for i, j in L1:
            win.blit(i.image, j)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_i]:
        char.char_info = True
    if keys[pygame.K_ESCAPE]:
        char.char_info = False
    if keys[pygame.K_LEFT]:
        char.x -= 1
        char.left = True
        char.right = False
        char.up = False
        char.down = False
    elif keys[pygame.K_RIGHT]:
        char.x += 1
        char.right = True
        char.left = False
        char.up = False
        char.down = False
    elif keys[pygame.K_UP]:
        char.y -= 1
        char.up = True
        char.left = False
        char.right = False
        char.down = False
    elif keys[pygame.K_DOWN]:
        char.y += 1
        char.down = True
        char.left = False
        char.right = False
        char.up = False
    else:
        char.walkCount = 0

    pygame.display.update()


def ent3():
    global charEXP
    global charLv
    global charEXPE
    global map1
    my = char.my_poke[nub]
    text_SCORE = font.render('LV: ' + str(charLv), 1, (0, 0, 0))
    text_lvUP = font.render('HP: ' + str(charEXP) + "/" + str(charEXPE), 1, (0, 0, 0))
    text_BALLNUB = font.render('ball: ' + str(ball_num), 1, (0, 0, 0))
    text_lv = font.render('LV: ' + str(my.lv), 1, (0, 0, 0))
    text_dmg = font.render('DMG: ' + str(my.dmg), 1, (0, 0, 0))
    text_speed = font.render('SPEED: ' + str(my.speed), 1, (0, 0, 0))
    text_hp = font.render('HP: ' + str(my.hp), 1, (0, 0, 0))
    charEXPE = charLv * 10
    door3.draw()
    char.draw()
    for p in poke1:
        p.draw()
        if pygame.Rect.colliderect(p.rect, char.w):
            map1 = 4

    if pygame.Rect.colliderect(door3.back_pos, char.w):
        map1 = 0

    if char.char_info:
        win.blit(info, (0, 0))
        win.blit(text_SCORE, (0, 0))
        win.blit(text_lvUP, (0, 40))
        win.blit(text_BALLNUB, (60, 0))

        for i, j in L1:
            win.blit(i.image, j)
    if char.char_pif:
        win.blit(info, (0, 0))
        win.blit(my.image, (0, 0))
        win.blit(text_dmg, (0, 90))
        win.blit(text_speed, (0, 70))
        win.blit(text_hp, (0, 50))
        win.blit(text_lv, (0, 25))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_p]:
        char.char_pif = True
    if keys[pygame.K_i]:
        char.char_info = True
    if keys[pygame.K_ESCAPE]:
        char.char_info = False
        char.char_pif = False
    if keys[pygame.K_LEFT]:
        char.x -= 1
        char.left = True
        char.right = False
        char.up = False
        char.down = False
    elif keys[pygame.K_RIGHT]:
        char.x += 1
        char.right = True
        char.left = False
        char.up = False
        char.down = False
    elif keys[pygame.K_UP]:
        char.y -= 1 
        char.up = True
        char.left = False
        char.right = False
        char.down = False
    elif keys[pygame.K_DOWN]:
        char.y += 1
        char.down = True
        char.left = False
        char.right = False
        char.up = False
    else:
        char.walkCount = 0

    pygame.display.update()


def enter4():
    global my_att
    global boss_att
    global map1
    global nub
    my = char.my_poke[nub]
    win.fill((0, 0, 0))
    win.blit(char.my_poke[nub].image, (250, 250))
    for i in poke1:
        i.draw()
        if i.speed >= my.speed:
            boss_att = 1
        else:
            my_att = 1
    if boss_att == 1:
        for i in poke1:
            my.hp = i.dmg - my.hp
            print("我方宠物小精灵受到伤害，剩余血量", my.hp)
            if my.hp <= 0:
                print("我方宠物小精灵死亡")
                map1 = 0
            boss_att = 0

    if my_att == 1:
        for i in poke1:
            i.hp = my.dmg - i.hp
            print("敌方宠物小精灵受到的伤害，剩余血量", i.hp)
            if i.hp <= 0:
                print("地方宠物小精灵死亡")
                my.hp += random.randint(0, 1)
                my.dmg += random.randint(0, 1)
                my.hp += random.randint(0, 1)
                my.speed += random.randint(0, 1)
                poke1.pop()
                map1 = 3
            my_att = 0

    if boss_att == 0:
        my_att = 1
    if my_att == 0:
        boss_att = 1
    pygame.display.update()


nub = 0
my_att = 0
boss_att = 0
ball_num = 0
map1 = 0
bg = BG(0, 0)
char = Player(50, 200)
clock = pygame.time.Clock()
door1 = FIGHT_MAP()
door2 = FIGHT_MAP2()
door3 = FIGHT_MAP3()
poke1 = []
space = []
spaceUD = []
my_sup = [ball(random.randint(1, 450), random.randint(1, 450)),
          ball(random.randint(1, 450), random.randint(1, 450)),
          ball(random.randint(1, 450), random.randint(1, 450)),
          ball(random.randint(1, 450), random.randint(1, 450))]
info = pygame.image.load("set7.png")
charLv = 1
charEXP = 0
charEXPE = charLv * 10
poke1.append(poke(random.randint(100, 350), random.randint(100, 350)))
font = pygame.font.SysFont('Arial', 30, True)
my_poke_x = 1
my_poke_posit = []
my_supp = []
while True:
    clock.tick(70)
    my_poke_y = (my_poke_x, 80)
    L1 = list(zip(char.my_poke, my_poke_posit))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if map1 == 0:
        ent()
    if map1 == 1:
        ent1()
    if map1 == 2:
        ent2()
    if map1 == 3:
        ent3()
    if map1 == 4:
        enter4()