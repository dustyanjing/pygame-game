import pygame
import sys
import random
import time


class mengh(pygame.sprite.Sprite):
    def __init__(self, image, position, speed, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.postiong = None
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = speed
        self.width, self.height = bg_size[0], bg_size[1]

    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.right < 0:
            self.rect.left = self.width
        elif self.rect.left > self.width:
            self.rect.right = 0
        elif self.rect.bottom < 0:
            self.rect.top = self.height
        elif self.rect.top > self.height:
            self.rect.bottom = 0


def main():
    start = time.time()
    pygame.init()

    mengh_image = "chatch.gif"

    pygame.mixer.music.load("BG.wav")
    pygame.mixer.music.play(-1, 0)
    HIT = pygame.mixer.Sound("hit.wav")
    run = True

    bg_size = width, height = 600, 600
    screen = pygame.display.set_mode(bg_size)
    pygame.display.set_caption("play ")
    menghs = []
    group = pygame.sprite.Group()
    R = 20
    font = pygame.font.SysFont('Arial', 30, True)
    for i in range(R):#make 5 mengh
        postiong = random.randint(0, width-300), random.randint(0, height-300)
        speed = [random.randint(-10, 10), random.randint(-10, 10)]
        Mengh = mengh(mengh_image, postiong, speed, bg_size)
        while pygame.sprite.spritecollide(Mengh, group, False):
            Mengh.rect.left, Mengh.rect.top = random.randint(0, width-100), random.randint(0,height-100)
        menghs.append(Mengh)
        group.add(Mengh)

    clock = pygame.time.Clock()

    while run:
        screen.fill((0, 0, 0))
        for each in menghs:
            each.move()
            screen.blit(each.image, each.rect)

        for each in group:
            group.remove(each)
            if pygame.sprite.spritecollide(each, group, False):
                each.speed[0] = -each.speed[0]
                each.speed[1] = -each.speed[1]
            group.add(each)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                catch = pygame.draw.rect(screen, (255, 0, 0), (event.pos[0], event.pos[1], 3, 3), 5)
                for each in menghs:
                    if pygame.Rect.colliderect(catch, each):
                        menghs.pop(menghs.index(each))
                        HIT.play()

        stop = time.time()
        U = stop - start
        text = font.render('TIME: ' + str('%-3.5s' % U), 1, (255, 0, 0))
        screen.blit(text, (0, 0))
        if len(menghs) == 0:
            final = time.time() - start
            text1 = font.render("game over:" + str('%-3.5s' % final), 1, (255, 255, 0))
            screen.blit(text1, (250, 250))
            pygame.display.update()
            time.sleep(6)
            sys.exit()
        pygame.display.update()
        clock.tick(30)


if __name__ == '__main__':
    main()
