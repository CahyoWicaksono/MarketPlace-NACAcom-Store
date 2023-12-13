import pygame
import random

# Initialize PyGame
pygame.init()

# Game Screen
screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

# Colors
white = (255, 255, 255)

# Paddle
paddle_width = 100
paddle_height = 20
paddle = pygame.Rect(600, 700, paddle_width, paddle_height)

# Ball
ball_radius = 15
ball = pygame.Rect(600, 600, ball_radius*2, ball_radius*2)
ball_speed_x = 7
ball_speed_y = 7

# Bricks
brick_rows = 5
brick_columns = 15
brick_width = 80
brick_height = 20
brick_offset_x = 100
brick_offset_y = 100
bricks = []
for i in range(brick_rows):
    for j in range(brick_columns):
        brick = pygame.Rect(brick_offset_x + j * (brick_width + 10),
                            brick_offset_y + i * (brick_height + 5),
                            brick_width, brick_height)
        bricks.append(brick)

# Game Loop
running = True
while running:
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle.x -= 500
            if event.key == pygame.K_RIGHT:
                paddle.x += 500

    # Draw paddle
    pygame.draw.rect(screen, (0, 0, 255), paddle)

    # Draw ball
    pygame.draw.ellipse(screen, (255, 0, 0), ball)

    # Update ball position
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Check for collisions with walls
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y = -ball_speed_y
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x = -ball_speed_x

    # Check for collisions with paddle
    if ball.colliderect(paddle):
        ball_speed_y = -ball_speed_y
        ball_speed_x = ball_speed_x if random.random() > 0.5 else -ball_speed_x

    # Check for collisions with bricks
    for brick in bricks:
        if ball.colliderect(brick):
            bricks.remove(brick)
            ball_speed_y = -ball_speed_y
            ball_speed_x = ball_speed_x if random.random() > 0.5 else -ball_speed_x
            break

    # Draw bricks
    for brick in bricks:
        pygame.draw.rect(screen, (255, 0, 0), brick)

    # Update display
    pygame.display.flip()

pygame.quit()