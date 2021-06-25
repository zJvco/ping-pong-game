import pygame, sys
from ball import Ball
from bar import Bar

pygame.font.init()

# COLOR
WHITE = (255, 255, 255)
ORANGE = (235, 152, 78)
DARK_BLUE = (44, 62, 80)

# DISPLAY
WIDTH, HEIGHT = 1000, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND_COLOR = pygame.color.Color(DARK_BLUE)
pygame.display.set_caption("Ping Pong")

def main():
    clock = pygame.time.Clock()

    # Ball Requirements
    ball_size = 10
    ball_x = WIDTH / 2
    ball_y = HEIGHT / 2
    ball_speed_x = 7
    ball_speed_y = 7

    # Bar Requirements
    bar_width = 10
    bar_height = 120
    bar_x = 10
    bar_y = (HEIGHT / 2) - (bar_height / 2)
    bar_speed = 7

    player_score = 0
    ai_score = 0
    font = pygame.font.SysFont("comicsans", 50)
    FPS = 60

    ball = Ball(ball_x, ball_y, ORANGE, ball_size)
    ai_bar = Bar(bar_x, bar_y, WHITE, bar_width, bar_height)
    player_bar = Bar(WIDTH - bar_width - bar_x, bar_y, WHITE, bar_width, bar_height)

    def redraw_window():
        # BACKGROUND
        WINDOW.fill(BACKGROUND_COLOR)

        # MIDDLE LINE
        pygame.draw.rect(WINDOW, WHITE, ((WIDTH - 5) / 2, 0, 5, HEIGHT))

        # BALL
        ball.draw(WINDOW)

        # AI
        ai_bar.draw(WINDOW)
        ai_bar.y = ball.y - bar_height / 2

        # PLAYER
        player_bar.draw(WINDOW)

        # DRAW TEXT
        player_score_label = font.render(f"{player_score}", 1, WHITE)
        ai_score_label = font.render(f"{ai_score}", 1, WHITE)

        WINDOW.blit(player_score_label, (WIDTH / 2 - player_score_label.get_width() + 50, 10))
        WINDOW.blit(ai_score_label, (WIDTH / 2 - 50, 10))

        pygame.display.update()

    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # PLAYER MOVIMENT
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and player_bar.y > 0 + 10:
            player_bar.y -= bar_speed
        if keys[pygame.K_DOWN] and player_bar.y < HEIGHT - bar_height - 10:
            player_bar.y += bar_speed

        # AI MOVIMENT VALIDATION
        if ai_bar.y <= 10:
            ai_bar.y = 10
        if ai_bar.y + bar_height >= HEIGHT - 10:
            ai_bar.y = HEIGHT - bar_height - 10

        # BALL MOVIMENT
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        if ball.x - ball_size <= 0 or ball.x >= WIDTH - ball_size:
            ball_speed_x *= -1
        if ball.y - ball_size <= 0 or ball.y >= HEIGHT - ball_size:
            ball_speed_y *= -1

        redraw_window()

if __name__ == "__main__":
    main()
