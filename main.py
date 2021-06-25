import pygame, sys
from ball import Ball
from bar import Bar

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
    ball_vel = 1

    # Bar Requirements
    bar_x = 10
    bar_y = 0
    bar_vel = 1
    bar_width = 10
    bar_height = 120

    FPS = 60

    ball = Ball(ball_x, ball_y, ORANGE, ball_size)
    ai_bar = Bar(bar_x, (HEIGHT / 2) - (bar_height / 2), WHITE, bar_width, bar_height)
    player_bar = Bar(WIDTH - bar_width - bar_x, (HEIGHT / 2) - (bar_height / 2), WHITE, bar_width, bar_height)

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

        pygame.display.flip()
        pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and player_bar.y > 0 + 10:
            player_bar.y -= bar_vel
        if keys[pygame.K_DOWN] and player_bar.y < HEIGHT - bar_height - 10:
            player_bar.y += bar_vel

        ball.x -= ball_vel
        ball.y -= ball_vel

        redraw_window()

    clock.tick(FPS)

if __name__ == "__main__":
    main()
