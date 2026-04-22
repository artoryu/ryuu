import pygame
import random

pygame.init()

# --- window settings ---
WIDTH, HEIGHT = 600, 600
CELL = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

# --- colors ---
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

# --- snake ---
snake = [(100, 100)]
dx, dy = CELL, 0

# --- food ---
def generate_food():
    while True:
        x = random.randrange(0, WIDTH, CELL)
        y = random.randrange(0, HEIGHT, CELL)
        if (x, y) not in snake:
            return (x, y)

food = generate_food()

# --- score & level ---
score = 0
level = 1
speed = 10

font = pygame.font.SysFont("Arial", 24)

running = True
while running:
    screen.fill(WHITE)

    # --- events ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- controls ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and dy == 0:
        dx, dy = 0, -CELL
    if keys[pygame.K_DOWN] and dy == 0:
        dx, dy = 0, CELL
    if keys[pygame.K_LEFT] and dx == 0:
        dx, dy = -CELL, 0
    if keys[pygame.K_RIGHT] and dx == 0:
        dx, dy = CELL, 0

    # --- move snake ---
    head = (snake[0][0] + dx, snake[0][1] + dy)

    # --- wall collision ---
    if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
        running = False

    # --- self collision ---
    if head in snake:
        running = False

    snake.insert(0, head)

    # --- eating food ---
    if head == food:
        score += 1
        food = generate_food()
    else:
        snake.pop()

    # --- level system ---
    if score % 4 == 0 and score != 0:
        level = score // 4 + 1
        speed = 10 + level * 2

    # --- draw snake ---
    for s in snake:
        pygame.draw.rect(screen, GREEN, (*s, CELL, CELL))

    # --- draw food ---
    pygame.draw.rect(screen, RED, (*food, CELL, CELL))

    # --- draw score ---
    text = font.render(f"Score: {score}  Level: {level}", True, BLACK)
    screen.blit(text, (10, 10))

    pygame.display.update()
    clock.tick(speed)

pygame.quit()