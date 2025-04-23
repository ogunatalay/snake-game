import pygame
import time
import random

# Pygame'i başlat
pygame.init()

# Oyun ekran boyutları
width = 600
height = 400

# Ekranı oluştur
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Yılan Oyunu')

# Renkler
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Yılan boyutu ve hızı
snake_block = 10
snake_speed = 15

# Saat
clock = pygame.time.Clock()

# Yazı fontu
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Skoru yazdırma fonksiyonu
def your_score(score):
    value = score_font.render("Skor: " + str(score), True, white)
    screen.blit(value, [0, 0])

# Yılanı çizme fonksiyonu
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])

# Mesaj yazma fonksiyonu
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])

# Gradient Arka Plan fonksiyonu
def draw_gradient_background():
    for i in range(height):
        color = (50, 153 + i // 5, 213 + i // 10)  # Renk geçişi
        pygame.draw.line(screen, color, (0, i), (width, i))

# Oyun döngüsü
def gameLoop():
    game_over = False
    game_close = False

    # Yılanın başlangıç pozisyonu
    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    # Yiyecek pozisyonu
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    score = 0  # Skor başlatma

    while not game_over:

        while game_close == True:
            screen.fill(blue)
            message("Kaybettin! Q-Quit veya C-Play Again", red)
            your_score(score)  # Skoru ekranda göster
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change

        # Gradient arka planı çiz
        draw_gradient_background()

        # Yiyeceği çiz
        pygame.draw.rect(screen, green, [foodx, foody, snake_block, snake_block])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        # Yılan uzunluğunu kontrol et
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # Yılanı çiz
        our_snake(snake_block, snake_List)

        # Skoru ekranda göster
        your_score(score)

        pygame.display.update()

        # Yılan yiyeceği yediğinde
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1  # Yılanın uzunluğunu artır
            score += 10  # Skoru artır

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Oyun başlat
gameLoop()
