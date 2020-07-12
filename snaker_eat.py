import pygame
import sys
import random


def main():
    pygame.init()
    pygame.mixer.music.load("bg.wav")
    pygame.mixer.music.play(-1, 0)
    Width, Height = 420, 420
    window = pygame.display.set_mode((Width, Height))
    pygame.display.set_caption('snake game')
    direct = 'right'
    head_color = (255, 0, 0)
    head = [30, 15]
    snake_body = [[30, 15], [15, 15], [0, 15]]
    clock = pygame.time.Clock()

    food_POSITION = [random.randint(1, 27) * 15, random.randint(1, 27) * 15]
    food_pos = False
    _font = pygame.font.SysFont("arial", 60)
    _text = _font.render("Game Over", True, (255, 255, 255))
    font = pygame.font.SysFont("arial", 30)
    text = font.render("SPACE TO RESTART", 1, (255, 255, 255))
    while quit:
        clock.tick(10)
        snake_body.insert(0, list(head))
        if head[0] == food_POSITION[0] and head[1] == food_POSITION[1]:
            food_pos = True
            print(snake_body)

        else:
            snake_body.pop()
        if food_pos:

            food_POSITION = [random.randint(1, 27) * 15, random.randint(1, 27) * 15]
            if food_POSITION[0] == head[0] and food_POSITION[1] == head[1]:
                pass
            if food_POSITION[0] >= 0 or food_POSITION[0] <= [Width]:
                pass
            if food_POSITION[1] >= 0 or food_POSITION[1] <= [Height]:
                pass
            for snake in snake_body:
                if food_POSITION[0] == snake[0] and food_POSITION[1] == snake[1]:
                    pass
            else:
                food_pos = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main()
                if event.key == 273 or event.key == 119:
                    if direct == 'right' or direct == 'left':
                        direct = 'top'
                if event.key == 274 or event.key == 115:
                    if direct == 'left' or direct == 'right':
                        direct = 'bottom'
                if event.key == 276 or event.key == 97:
                    if direct == 'top' or direct == 'bottom':
                        direct = 'left'
                if event.key == 275 or event.key == 100:
                    if direct == 'bottom' or direct == 'top':
                        direct = 'right'
        if direct == "right":
            head[0] += 15
        if direct == 'left':
            head[0] -= 15
        if direct == 'top':
            head[1] -= 15
        if direct == 'bottom':
            head[1] += 15

        window.fill((0, 0, 0))
        for snake in snake_body:
            pygame.draw.rect(window, head_color, (snake[0], snake[1], 15, 15))

        pygame.draw.rect(window, head_color, (food_POSITION[0], food_POSITION[1], 15, 15))

        for snake in snake_body[1:]:
            if head[0] == snake[0] and head[1] == snake[1]:
                window.fill((0, 0, 0))
                window.blit(_text, (80, 180))
                window.blit(text, (90, 225))
        if head[0] < 0 or head[0] > Width or head[1] > Height or head[1] < 0:
            window.fill((0, 0, 0))
            window.blit(_text, (80, 160))
            window.blit(text, (90, 225))

        pygame.display.update()


main()