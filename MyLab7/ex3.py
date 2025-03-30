import pygame

# Инициализация
pygame.init()
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Параметры мяча
ball_radius = 25
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
speed = 20

running = True
while running:
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and ball_y - speed - ball_radius >= 0:
                ball_y -= speed
            elif event.key == pygame.K_DOWN and ball_y + speed + ball_radius <= HEIGHT:
                ball_y += speed
            elif event.key == pygame.K_LEFT and ball_x - speed - ball_radius >= 0:
                ball_x -= speed
            elif event.key == pygame.K_RIGHT and ball_x + speed + ball_radius <= WIDTH:
                ball_x += speed

pygame.quit()
