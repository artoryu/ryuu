import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

clock = pygame.time.Clock()

# --- colors ---
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

current_color = BLACK

# --- modes ---
mode = "draw"   # draw / rect / circle / eraser

start_pos = None

screen.fill(WHITE)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # --- mouse pressed ---
        if event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = event.pos

        # --- mouse released ---
        if event.type == pygame.MOUSEBUTTONUP:
            end_pos = event.pos

            if mode == "rect":
                rect = pygame.Rect(start_pos, (end_pos[0]-start_pos[0], end_pos[1]-start_pos[1]))
                pygame.draw.rect(screen, current_color, rect, 2)

            if mode == "circle":
                radius = int(((end_pos[0]-start_pos[0])**2 + (end_pos[1]-start_pos[1])**2) ** 0.5)
                pygame.draw.circle(screen, current_color, start_pos, radius, 2)

        # --- keyboard controls ---
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = "rect"
            if event.key == pygame.K_c:
                mode = "circle"
            if event.key == pygame.K_e:
                mode = "eraser"
            if event.key == pygame.K_d:
                mode = "draw"

            # colors
            if event.key == pygame.K_1:
                current_color = BLACK
            if event.key == pygame.K_2:
                current_color = RED
            if event.key == pygame.K_3:
                current_color = BLUE

    # --- drawing with mouse ---
    if pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()

        if mode == "draw":
            pygame.draw.circle(screen, current_color, pos, 5)

        if mode == "eraser":
            pygame.draw.circle(screen, WHITE, pos, 10)

    pygame.display.update()
    clock.tick(60)

pygame.quit()