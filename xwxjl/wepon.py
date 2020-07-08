import pygame


class wepon(object):
    bullet_1 = pygame.image.load('1.png')
    bullet_2= pygame.image.load('1.png')

    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing
        self.hit_box = (self.x+30, self.y+30, 55, 55)

    def draw(self, win):
        if self.facing == -1:
            win.blit(self.bullet_1, (self.x, self.y))
        else:
            win.blit(self.bullet_2, (self.x, self.y))
        self.hit_box = (self.x+30, self.y+30, 55, 55)
        #pygame.draw.rect(win, (255, 0, 0), self.hit_box, 2)