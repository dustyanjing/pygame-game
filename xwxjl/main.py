import pygame
from PLAYER import *
from wepon import *
from enemy import *
import sys
pygame.init()

size = Width, Height = 480, 783

win = pygame.display.set_mode((size))
pygame.display.set_caption("First Game")

bg = pygame.image.load("_2.jpg")
winmusic=pygame.mixer.Sound("WIN.wav")
Losemusic=pygame.mixer.Sound("lose.wav")
hitmusic=pygame.mixer.Sound("jn1.wav")
bgmusic=pygame.mixer.music.load("bg.wav")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1,0)

def collision_check(bullet, little_enemy):
    temp1 = (bullet.hit_box[0] <= little_enemy.hit_box[0] + little_enemy.hit_box[2] <= bullet.hit_box[0]
             + bullet.hit_box[2])
    temp2 = (bullet.hit_box[1] <= little_enemy.hit_box[1] + little_enemy.hit_box[3] <= bullet.hit_box[1]
             + bullet.hit_box[3])
    return temp1 and temp2


def collision_check1(hero, little_enemy):
    temp1 = (hero.hit_box[0] <= little_enemy.hit_box[0] + little_enemy.hit_box[2] <= hero.hit_box[0] +
             hero.hit_box[2])
    temp2 = (hero.hit_box[1] <= little_enemy.hit_box[1] + little_enemy.hit_box[3] <= hero.hit_box[1] +
             hero.hit_box[3])
    return temp1 and temp2


def show_Window():
    win.blit(bg, (0, 0))
    text = font.render('Score: ' + str(score), 1, (0, 0, 0))
    text1 = font.render("HP:" + str(hero.hp), 1, (0, 0, 0))
    you_win = font.render('YOU WIN! ', 1, (0, 0, 255))
    you_lost = font.render('YOU LOST! ', 1, (255, 0, 0))
    if little_enemy.hp <0:
        Losemusic.play()
        win.blit(you_win, (200, 230))
        pygame.display.update()
        return
    if hero.hp <= 0:
        winmusic.play()
        win.blit(you_lost, (200, 230))
        pygame.display.update()
        return

    win.blit(text, (370, 10))
    win.blit(text1, (20, 10))
    hero.draw(win)
    little_enemy.draw_enemy(win)
    for BULLET in bullets:
        BULLET.draw(win)

    pygame.display.update()


font = pygame.font.SysFont('Arial', 30, True)
score = 0

shootLoop = 0
little_enemy = enemy(50, 401, 32, 32,450)
hero = Player(400, 400, 40, 60,)
clock = pygame.time.Clock()
bullets = []
while True:
    clock.tick(27)
    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0
    if collision_check1(hero, little_enemy) or collision_check1(little_enemy, hero):
        hero.hp -= 1
        hero.isJump = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    for bullet in bullets:
        if collision_check(bullet, little_enemy) or collision_check(little_enemy, bullet):
            score += 1
            little_enemy.hp -= 1
            bullets.pop(bullets.index(bullet))

        if Width > bullet.x > 0:
            bullet.x = bullet.x + bullet.vel
        else:
            b = bullets.index(bullet)
            bullets.pop(b)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and hero.x > hero.vel:
        hero.x -= hero.vel
        hero.left = True
        hero.right = False

    elif keys[pygame.K_RIGHT] and hero.x < 480 - hero.vel - hero.width:
        hero.x += hero.vel
        hero.left = False
        hero.right = True

    elif keys[pygame.K_SPACE] and shootLoop == 0:
        hitmusic.play()
        if hero.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 3:
            bullets.append(wepon(round(hero.x), round(hero.y), 6, (0, 0, 0), facing))
        shootLoop = 1
    else:
        hero.walkCount = 0

    if not hero.isJump:
        if keys[pygame.K_UP]:
            hero.isJump = True
            hero.walkCount = 0
    else:
        if hero.jumpCount >= -10:
            hero.y -= (hero.jumpCount * abs(hero.jumpCount)) * 0.5
            hero.jumpCount -= 1
        else:
            hero.jumpCount = 10
            hero.isJump = False

    show_Window()
