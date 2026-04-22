import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

clock = pygame.time.Clock()

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# player
player_x = 400
player_y = 500
player_speed = 5

# coins
coin_size = 30
coins = []
score = 0

font = pygame.font.SysFont("Arial", 30)


def spawn_coin():
    x = random.randint(50, WIDTH - 50)
    y = random.randint(-600, -50)
    coins.append([x, y])


# spawn initial coins
for _ in range(5):
    spawn_coin()


running = True
while running:
    screen.fill(WHITE)

    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # draw player
    pygame.draw.rect(screen, BLACK, (player_x, player_y, 50, 50))

    # coins logic
    for coin in coins:
        coin[1] += 4  # fall speed

        pygame.draw.circle(screen, (255, 215, 0), coin, 10)

        # collision
        if player_x < coin[0] < player_x + 50 and player_y < coin[1] < player_y + 50:
            coins.remove(coin)
            score += 1
            spawn_coin()

    # score
    text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(text, (650, 20))

    pygame.display.update()
    clock.tick(60)

pygame.quit()