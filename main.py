import pygame
import sys
import os
from pygame import mixer
from ball import Ball
from bar import Bar

pygame.init()

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
    ball_size = 20
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

    # BACKGROUND MUSIC
    mixer.music.load(os.path.join("assets", "happynes.wav"))
    mixer.music.play(-1)
    mixer.music.set_volume(0.1)

    # BALL SOUND
    ball_sound = mixer.Sound(os.path.join("assets", "sound_bouncing.wav"))

    # POINT MATCH
    point_match_sound = mixer.Sound(os.path.join("assets", "sound_correct.wav"))
    point_match_sound.set_volume(0.1)

    # INSTANCE
    ball = Ball(ball_x, ball_y, ORANGE, ball_size, ball_speed_x, ball_speed_y, ball_sound)
    ai_bar = Bar(bar_x, bar_y, WHITE, bar_width, bar_height, bar_speed)
    player_bar = Bar(WIDTH - bar_width - bar_x, bar_y, WHITE, bar_width, bar_height, bar_speed)

    def redraw_window():
        # BACKGROUND
        WINDOW.fill(BACKGROUND_COLOR)

        # MIDDLE LINE
        pygame.draw.rect(WINDOW, WHITE, ((WIDTH - 5) / 2, 0, 5, HEIGHT))

        # BALL
        ball.ball_cfg()
        ball.ball_animation(WIDTH, HEIGHT, ai_bar.y, player_bar.y, bar_width, bar_height, bar_x)
        ball.draw(WINDOW)

        # AI
        ai_bar.bar_cfg()
        ai_bar.ai_animation(HEIGHT, ball.y)
        ai_bar.draw(WINDOW)

        # PLAYER
        player_bar.bar_cfg()
        player_bar.player_animation(HEIGHT)
        player_bar.draw(WINDOW)

        # DRAW TEXT
        player_score_label = font.render(f"{player_score}", 1, WHITE)
        ai_score_label = font.render(f"{ai_score}", 1, WHITE)

        WINDOW.blit(player_score_label, (WIDTH / 2 - player_score_label.get_width() + 50, 10))
        WINDOW.blit(ai_score_label, (WIDTH / 2 - 50, 10))

        # UPDATE WINDOW
        pygame.display.update()
        clock.tick(FPS)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if ball.x <= 0:
            point_match_sound.play()
            player_score += 1
            ball.x, ball.y = ball_x, ball_y
        if ball.x >= WIDTH - ball_size:
            point_match_sound.play()
            ai_score += 1
            ball.x, ball.y = ball_x, ball_y

        redraw_window()


if __name__ == "__main__":
    main()
