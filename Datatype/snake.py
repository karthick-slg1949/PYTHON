#snake game
import pygame
import random
    
#initialize pygame
pygame.init()
#set up the game window
WINDOW_WITH = 800
WINDOW_HEIGHT = 600
game_window = pygame.display.set_mode((WINDOW_WITH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake Game")

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN =(0, 255, 0)
RED = (255, 0, 0)

#snake parameters
BLOCK_SIZE = 20
snake_speed = 15

#fonts
font = pygame.font.sysFont(None, 40)

#Function to display text on screen
def display_text(text, color, x, y):
    screen_text = font.render(text, True, color)
    game_window.blit(screen_text, x, y)

#function to draw the snake
def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(game_window, BLACK,[block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])
#Game loop
def game_loop():
    game_over = False
    game_close = False
    #snake initial position and direction
    snake_x = WINDOW_WITH / 2
    snake_y = WINDOW_HEIGHT / 2
    snake_x_change = 0
    snake_y_chamge = 0
    snake_list = []
    snake_length = 1
    #Food initial position
    food_x = round(random.randrange(0, WINDOW_WITH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    food_y = round(random.randrange(0, WINDOW_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
#Main game loop
    while not game_over:

     while game_close:
       game_window.fill(WHITE)
       display_text("you lost! press q to quit or c play again", RED, 100, 250)
       pygame.display.update()
       for event in pygame.event.get():
           if event.type == pygame.KEYDOWN:
              if event.key == pygame.k.q:
                 game_over ==True
                 game_close == False
              elif event.key ==pygame.k_c:
                   game_loop()

    for event in pygame.event.get():
       if event.type == pygame.QUIT:
          game_over = True
       if event.key == pygame.KEYDOWN:
          if event.key == pygame.k_LEFT:
             snake_x_change = -BLOCK_SIZE
             snake_y_chamge = 0
       elif event.key ==pygame.k_RIGHT:
             snake_x_change = BLOCK_SIZE
             snake_y_chamge = 0
       elif event.key == pygame.k_up:
             snake_y_chamge = -BLOCK_SIZE
             snake_x_change = 0
       elif event.key == pygame.k_down:   
             snake_y_chamge = BLOCK_SIZE
             snake_x_change = 0

    #update snake position
    snake_x += snake_x_change
    snake_y += snake_y_chamge

    #check if snake eats the food
    if snake_x ==food_x and snake_y == food_y:
        food_x = round(random.randrange(0, WINDOW_WITH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
        food_y = round(random.ranrange(0, WINDOW_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
        snake_length =+ 1
    #check if snake hits the boundaries
    if snake_x >= WINDOW_WITH or snake_x < 0 or snake_y >= WINDOW_HEIGHT or snake_y <0:
        game_close = True
    #uptate game window
    game_window.fill(WHITE)
    pygame.draw.rect(game_window, GREEN, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])

    snake_head = []
    snake_head.append(snake_x)
    snake_head.append(snake_y)
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]

    #check if snake hits itself
    for block in snake_list[:-1]:
        if block == snake_head:
            game_close = True

    draw_snake(snake_list)
    pygame.display.update()

    #set snake speed
    clock.tick(snake_speed)

pygame.quit()
quit()

#set up game clock
clock = pygame.time.clock()

#Start the game loop
game_loop()
