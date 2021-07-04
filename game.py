import pygame, sys
from ball import Ball
from bar import Bar

class Game:
    def __init__(self, WIDTH, HEIGHT, clock, FPS, font, sound):
        self.WHITE = (255, 255, 255)
        self.ORANGE = (235, 152, 78)
        self.DARK_BLUE = (44, 62, 80)
        self.GREEN = (26, 188, 156)
        self.BLACK = (0, 0, 0)
        self.player = Bar(WIDTH - 20, (HEIGHT / 2) - (120 / 2), self.WHITE)
        self.ai = Bar(10, (HEIGHT / 2) - (120 / 2), self.WHITE)
        self.ball = Ball(WIDTH, HEIGHT, self.ORANGE)
        self.clock = clock
        self.FPS = FPS
        self.font = font
        self.player_score = 0
        self.ai_score = 0
        self.score_timer = None
        self.BACKGROUND_COLOR = pygame.color.Color(self.DARK_BLUE)
        self.sound = sound

    def draw(self, WINDOW, WIDTH, HEIGHT):
        player_score_label = self.font.render(f"{self.player_score}", 1, self.WHITE)
        ai_score_label = self.font.render(f"{self.ai_score}", 1, self.WHITE)

        WINDOW.blit(player_score_label, (WIDTH / 2 - player_score_label.get_width() + 50, 10))
        WINDOW.blit(ai_score_label, (WIDTH / 2 - 50, 10))

        pygame.draw.rect(WINDOW, self.WHITE, ((WIDTH - 5) / 2, 0, 5, HEIGHT))

    def update(self, WINDOW, WIDTH, HEIGHT):
        self.player.bar_cfg()
        self.player.player_animation(HEIGHT)
        self.player.draw(WINDOW)

        self.ai.bar_cfg()
        self.ai.ai_animation(HEIGHT, self.ball.y)
        self.ai.draw(WINDOW)

        self.ball.ball_cfg()
        self.ball.detect_collision(self.player.get_bar_cfg(), self.ai.get_bar_cfg(), self.sound)
        self.ball.ball_animation(WIDTH, HEIGHT, self.sound)
        self.ball.draw(WINDOW)

    def check_game_point(self, WIDTH):
        if self.ball.x <= 0:
            self.sound.play_point_match_sound()
            self.player_score += 1
            self.score_timer = pygame.time.get_ticks()

        if self.ball.x >= WIDTH - self.ball.size:
            self.sound.play_point_match_sound()
            self.ai_score += 1
            self.score_timer = pygame.time.get_ticks()

    def draw_score_timer(self, WINDOW, WIDTH, HEIGHT):
        if self.score_timer:
            current_time = pygame.time.get_ticks()
            self.ball.x, self.ball.y = WIDTH / 2 - self.ball.size / 2, HEIGHT / 2 - self.ball.size / 2

            if current_time - self.score_timer < 700:
                three_timer_label = self.font.render("3", 0, self.GREEN)
                WINDOW.blit(three_timer_label, (WIDTH / 2 - three_timer_label.get_width() / 2, HEIGHT / 2 + 20))
            elif current_time - self.score_timer < 1400:
                two_timer_label = self.font.render("2", 0, self.GREEN)
                WINDOW.blit(two_timer_label, (WIDTH / 2 - two_timer_label.get_width() / 2, HEIGHT / 2 + 20))
            else:
                one_timer_label = self.font.render("1", 0, self.GREEN)
                WINDOW.blit(one_timer_label, (WIDTH / 2 - one_timer_label.get_width() / 2, HEIGHT / 2 + 20))

            if not (current_time - self.score_timer < 2100):
                self.score_timer = None

    def game_loop(self, WINDOW, WIDTH, HEIGHT):
        run = True

        while run:
            WINDOW.fill(self.BACKGROUND_COLOR)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.check_game_point(WIDTH)
            self.draw(WINDOW, WIDTH, HEIGHT)
            self.update(WINDOW, WIDTH, HEIGHT)
            self.draw_score_timer(WINDOW, WIDTH, HEIGHT)

            pygame.display.update()
            self.clock.tick(self.FPS)
