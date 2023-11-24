import random
import time
import pygame


def snake(snake_list: list[tuple[int, int]], color: tuple):
    for x in snake_list:
        pygame.draw.rect(display, color, [x[0], x[1], 10, 10])


def set_food():
    x = round(random.randrange(20, 800 - 20) / 10) * 10
    y = round(random.randrange(20, 600 - 20) / 10) * 10
    return x, y


def first_lost():
    global snake_list1, x1, y1, x1_change, y1_change, score1
    snake_list1 = []
    x1 = 200
    y1 = 450
    x1_change = 0
    y1_change = 0
    score1 = 1


def second_lost():
    global snake_list2, x2, y2, x2_change, y2_change, score2
    snake_list2 = []
    x2 = 600
    y2 = 150
    x2_change = 0
    y2_change = 0
    score2 = 1


GREEN = (0, 255, 0)
BACKGROUND = (165, 50, 120)
CYAN = (0, 255, 255)
BROWN = (244, 164, 96)
RED = (255, 0, 0)

pygame.init()

clock = pygame.time.Clock()
display = pygame.display.set_mode((800, 600))

game_closed = False

while not game_closed:
    first_lost()
    second_lost()

    food_x, food_y = set_food()

    game_over = False

    won = 0

    while not game_over:
        display.fill(BACKGROUND)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and x1_change != 10:
                    x1_change = -10
                    y1_change = 0
                if event.key == pygame.K_d and x1_change != -10:
                    x1_change = 10
                    y1_change = 0
                if event.key == pygame.K_w and y1_change != 10:
                    x1_change = 0
                    y1_change = -10
                if event.key == pygame.K_s and y1_change != -10:
                    x1_change = 0
                    y1_change = 10

                if event.key == pygame.K_LEFT and x2_change != 10:
                    x2_change = -10
                    y2_change = 0
                if event.key == pygame.K_RIGHT and x2_change != -10:
                    x2_change = 10
                    y2_change = 0
                if event.key == pygame.K_UP and y2_change != 10:
                    x2_change = 0
                    y2_change = -10
                if event.key == pygame.K_DOWN and y2_change != -10:
                    x2_change = 0
                    y2_change = 10

        x1 += x1_change
        y1 += y1_change
        x2 += x2_change
        y2 += y2_change

        if x1 == food_x and y1 == food_y:
            score1 += 1
            food_x, food_y = set_food()
        if x2 == food_x and y2 == food_y:
            score2 += 1
            food_x, food_y = set_food()

        if x1 in (800, -10) or y1 in (600, -10):
            first_lost()
        if x2 in (800, -10) or y2 in (600, -10):
            second_lost()

        if (x1, y1) == (x2, y2):
            first_lost()
            second_lost()

        if (x1, y1) in snake_list1[1:-2] or (x1, y1) in snake_list2:
            first_lost()
        if (x2, y2) in snake_list2[1:-2] or (x2, y2) in snake_list1:
            second_lost()

        snake_list1.append((x1, y1))
        snake_list2.append((x2, y2))

        if len(snake_list1) > score1:
            del snake_list1[0]
        if len(snake_list2) > score2:
            del snake_list2[0]

        if score1 == 21:
            won = 1
            game_over = True
        if score2 == 21:
            won = 2
            game_over = True

        snake(snake_list1, CYAN)
        snake(snake_list2, BROWN)

        pygame.draw.rect(display, GREEN, [food_x, food_y, 10, 10])

        pygame.display.update()

        clock.tick(25)

    if won == 1:
        display.blit(pygame.font.SysFont('loss notification', 50).render('Pink won', True, RED), [300, 250])
    elif won == 2:
        display.blit(pygame.font.SysFont('loss notification', 50).render('Red won!', True, RED), [300, 250])

    pygame.display.update()
    time.sleep(3)
    pygame.display.update()
    display.blit(pygame.font.SysFont('loss notification', 50).render('Press space to restart', True, GREEN), [300, 350])
    pygame.display.update()
    time.sleep(2)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                continue
            else:
                game_closed = True
                break

pygame.quit()
exit()
