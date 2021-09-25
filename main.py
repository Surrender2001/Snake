import pygame
from random import randrange

# field
RES = 800
SIZE = 50

# start position
x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
# to prevent up-down and left-right movements
dirs = {'W': True, 'A': True, 'S': True, 'D': True}
# snake length
length = 1
# coordinates of each cell
snake = [(x, y)]
# direction
dx, dy = 0, 0
# refresh rate
fps = 5
# score
score = 0

pygame.init()
sc = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 26, bold=True)
font_end = pygame.font.SysFont('Arial', 66, bold=True)
# image background
img = pygame.image.load('1.jpg')
img = pygame.transform.scale(img, (RES, RES))
while True:
    sc.blit(img, (0, 0))

    # drawing snake
    [(pygame.draw.rect(sc, pygame.Color('green'),
                       (i, j, SIZE-2, SIZE-2))) for i, j in snake]
    pygame.draw.rect(sc, pygame.Color('red'), (*apple, SIZE, SIZE))

    # render score
    render_score = font_score.render(f'SCORE: {score}',
                                     1, pygame.Color('orange'))
    sc.blit(render_score, (5, 5))

    # snake movement
    x += dx * SIZE
    y += dy * SIZE
    snake.append((x, y))
    snake = snake[-length:]

    # eating apple
    if snake[-1] == apple:
        apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
        length += 1
        fps += 0.2
        score += 1

    # game over
    if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE\
            or len(snake) != len(set(snake)):
        while True:
            render_end = font_end.render('GAME OVER', 1,
                                         pygame.Color('orange'))
            sc.blit(render_end, (RES // 2 - 200, RES // 3))
            pygame.display.flip()
            # button exit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

    pygame.display.flip()
    clock.tick(fps)
    # button exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # control
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and dirs['W']:
        dx, dy = 0, -1
        dirs = {'W': True, 'A': True, 'S': False, 'D': True}
    if key[pygame.K_a] and dirs['A']:
        dx, dy = -1, 0
        dirs = {'W': True, 'A': True, 'S': True, 'D': False}
    if key[pygame.K_s] and dirs['S']:
        dx, dy = 0, 1
        dirs = {'W': False, 'A': True, 'S': True, 'D': True}
    if key[pygame.K_d] and dirs['D']:
        dx, dy = 1, 0
        dirs = {'W': True, 'A': False, 'S': True, 'D': True}
