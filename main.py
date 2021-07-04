import pygame
import sys
from ball import Ball
from bar import Bar
from sound import Sound

# COLORS
WHITE = (255, 255, 255)
ORANGE = (235, 152, 78)
DARK_BLUE = (44, 62, 80)

class Main:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Ping Pong")

        self.WIDTH = 1000
        self.HEIGHT = 600
        self.WINDOW = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.player_score = 0
        self.ai_score = 0
        self.font = pygame.font.SysFont("comicsans", 50)
        self.FPS = 60
        self.BACKGROUND_COLOR = pygame.color.Color(DARK_BLUE)
        self.clock = pygame.time.Clock()

    def draw(self):
        player_score_label = self.font.render(f"{self.player_score}", 1, WHITE)
        ai_score_label = self.font.render(f"{self.ai_score}", 1, WHITE)

        self.WINDOW.blit(player_score_label, (self.WIDTH / 2 - player_score_label.get_width() + 50, 10))
        self.WINDOW.blit(ai_score_label, (self.WIDTH / 2 - 50, 10))

    def main_loop(self):
        sound = Sound()
        ball = Ball(self.WIDTH, self.HEIGHT, ORANGE)
        ai_bar = Bar(10, (self.HEIGHT / 2) - (120 / 2), WHITE)
        player_bar = Bar(self.WIDTH - 20, (self.HEIGHT / 2) - (120 / 2), WHITE)

        sound.player_background_music()
        sound.volume_control()

        while True:
            self.WINDOW.fill(self.BACKGROUND_COLOR)
            pygame.draw.rect(self.WINDOW, WHITE, ((self.WIDTH - 5) / 2, 0, 5, self.HEIGHT))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if ball.x <= 0:
                sound.play_point_match_sound()
                self.player_score += 1
                ball.x, ball.y = self.WIDTH / 2, self.HEIGHT / 2
            if ball.x >= self.WIDTH - ball.size:
                sound.play_point_match_sound()
                self.ai_score += 1
                ball.x, ball.y = self.WIDTH / 2, self.HEIGHT / 2

            player_bar.bar_cfg()
            player_bar.player_animation(self.HEIGHT)
            player_bar.draw(self.WINDOW)

            ai_bar.bar_cfg()
            ai_bar.ai_animation(self.HEIGHT, ball.y)
            ai_bar.draw(self.WINDOW)

            ball.ball_cfg()
            ball.detect_collision(player_bar.get_bar_cfg(), ai_bar.get_bar_cfg(), sound)
            ball.ball_animation(self.WIDTH, self.HEIGHT, sound)
            ball.draw(self.WINDOW)

            pygame.display.update()
            self.clock.tick(self.FPS)

if __name__ == "__main__":
    Main().main_loop()
