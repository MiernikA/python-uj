import pygame
import sys
import random

pygame.init()

width, height = 800, 600

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake")

# COLORS
light_green = (170, 215, 81)
pastel_blue = (69, 114, 231)
red = (231, 71, 29)
dark_green = (162, 209, 73)

# Set up

snake_size = 20
snake_speed = 10
snake = [(width // 2, height // 2)]
snake_direction = (1, 0)  # right

food_size = 20
food_position = (random.randrange(0, width - food_size, food_size),
                 random.randrange(0, height - food_size, food_size))

clock = pygame.time.Clock()

# Speed scaling
speed_increase_interval = 4000  # 4s
last_speed_increase_time = pygame.time.get_ticks()

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != (0, 1):
                snake_direction = (0, -1)
            elif event.key == pygame.K_DOWN and snake_direction != (0, -1):
                snake_direction = (0, 1)
            elif event.key == pygame.K_LEFT and snake_direction != (1, 0):
                snake_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                snake_direction = (1, 0)

    # Snake move
    x, y = snake[0]
    x += snake_direction[0] * snake_size
    y += snake_direction[1] * snake_size
    snake.insert(0, (x, y))

    # Collisions with borders
    if x < 0 or x >= width or y < 0 or y >= height:
        pygame.quit()
        sys.exit()

    # Collisions with itself
    if len(snake) > 1 and (x, y) in snake[1:]:
        pygame.quit()
        sys.exit()

    # Eating food
    if x == food_position[0] and y == food_position[1]:
        food_position = (random.randrange(0, width - food_size, food_size),
                         random.randrange(0, height - food_size, food_size))

        # Increase snake speed
        current_time = pygame.time.get_ticks()
        if current_time - last_speed_increase_time >= speed_increase_interval:
            snake_speed += 1
            last_speed_increase_time = current_time
    else:
        snake.pop()

    # DRAWING

    for row in range(0, width, 20):
        for col in range(0, height, 20):
            pygame.draw.rect(window, dark_green if (row // 20 + col // 20) % 2 == 0 else light_green,
                             (row, col, 20, 20))

    for segment in snake:
        pygame.draw.rect(window, pastel_blue, (segment[0], segment[1], snake_size, snake_size))

    pygame.draw.circle(window, red, (food_position[0] + food_size // 2, food_position[1] + food_size // 2),
                       food_size // 2)

    pygame.display.flip()
    clock.tick(snake_speed)
