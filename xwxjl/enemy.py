import pygame


class enemy (object):
    run = [pygame.image.load("1.gif"), pygame.image.load("2.gif"), pygame.image.load("3.gif"),
           pygame.image.load("4.gif")]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 6
        self.end = end
        self.path = [self.x, self.end]
        self.runCount = 0
        self.hp = 10
        self.hit_box = (self.x, self.y, 32, 32)

    def draw_enemy(self, win):
        self.enemy_move(win)
        if self.runCount + 1 >= 16:
            self.runCount = 0
        if self.speed > 0:
            win.blit(self.run[self.runCount // 4], (self.x, self.y))
            self.runCount += 1
        else:
            win.blit(self.run[self.runCount // 4], (self.x, self.y))
            self.runCount += 1
        self.hit_box = (self.x, self.y, 32, 32)
        #pygame.draw.rect(win, (255, 0, 0), self.hit_box, 2)
        pygame.draw.rect(win, (255, 0, 0), (self.hit_box[0], self.hit_box[1] - 10, 30, 8))
        pygame.draw.rect(win, (0, 128, 0), (self.hit_box[0], self.hit_box[1] - 10, 30 - self.hp * 3, 8))


    def enemy_move(self, win):
        if self.speed > 0:
            if self.x + self.speed < self.path[1]:
                self.x += self.speed
            else:
                self.speed = self.speed*-1
                self.runCount = 0
        else:
            if self.x - self.speed > self.path[0]:
                self.x += self.speed
            else:
                self.speed = self.speed * -1
                self.runCount = 0

