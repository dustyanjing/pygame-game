import time
import random
import pygame
from pygame.locals import *



pygame.init()
SCREEN_RECT = pygame.Rect(0, 0, 1000, 750)
OFFSET = 10
fps_clock = pygame.time.Clock()
screen = pygame.display.set_mode(SCREEN_RECT.size)
pygame.display.set_caption("贪吃蛇")
gameover_font = pygame.font.SysFont("arial", 100)
gameover_text = gameover_font.render("Game Over", True, (150, 150, 150))
gameover_rect = gameover_text.get_rect()
gameover_rect.center = SCREEN_RECT.center
snake_position = [100, 100]
snake_segments = [[100, 100], [100 - OFFSET, 100], [100 - 2 * OFFSET, 100]]
target_position = [300, 300]
flag = 0
direction = 'right'
temp_direction = direction
while True:
    fps_clock.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[K_RIGHT]:
        temp_direction = 'right'
    if keys_pressed[K_LEFT]:
        temp_direction = 'left'
    if keys_pressed[K_UP]:
        temp_direction = 'up'
    if keys_pressed[K_DOWN]:
        temp_direction = 'down'
    if (((temp_direction == 'right') and (direction != 'left'))
            or ((temp_direction == 'left') and (direction != 'right'))
            or ((temp_direction == 'up') and (direction != 'down'))
            or (temp_direction == 'down') and (direction != 'up')):
        direction = temp_direction
    if direction == 'right':
        snake_position[0] += OFFSET
    if direction == 'left':
        snake_position[0] -= OFFSET
    if direction == 'up':
        snake_position[1] -= OFFSET
    if direction == 'down':
        snake_position[1] += OFFSET
    snake_segments.insert(0, list(snake_position))
    print(snake_segments)
    if (snake_position[0] == target_position[0]) and (snake_position[1] == target_position[1]):
        flag = 1
    else:
        snake_segments.pop()
    if flag:
        x = random.randrange(1, SCREEN_RECT.width // OFFSET)
        y = random.randint(1, SCREEN_RECT.height // OFFSET)
        target_position = [int(x * OFFSET), int(y * OFFSET)]
        flag = 0
    screen.fill((0, 0, 0))
    for each in snake_segments:
        pygame.draw.rect(screen, (255, 255, 255), Rect(each[0], each[1], OFFSET, OFFSET))
    pygame.draw.rect(screen, (255, 0, 0), Rect(target_position[0], target_position[1], OFFSET, OFFSET))
    pygame.display.update()
    if ((snake_position[0] < 0)
            or (snake_position[0] > SCREEN_RECT.width - OFFSET)
            or (snake_position[1] < 0)
            or (snake_position[1] > SCREEN_RECT.height - OFFSET)):
        screen.blit(gameover_text, gameover_rect)
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        exit()
    for each in snake_segments[1:]:
        if (snake_segments[0] == each[0]) and (snake_segments[1] == each[1]):
            screen.blit(gameover_text, gameover_rect)
            pygame.display.update()
            time.sleep(2)
            pygame.quit()
            exit()