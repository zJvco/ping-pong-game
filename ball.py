import pygame

class Ball:
    def __init__(self, x, y, color, size, ball_speed_x, ball_speed_y):
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.ball_speed_x = ball_speed_x
        self.ball_speed_y = ball_speed_y
        self.ball = None

    def ball_cfg(self):
        self.ball = pygame.Rect(self.x, self.y, self.size, self.size)

    def ball_animation(self, window_width, window_height, ai_bar_y, player_bar_y, bar_width, bar_height, bar_x):
        self.x += self.ball_speed_x
        self.y += self.ball_speed_y

        if self.x <= 0 or self.x >= window_width - self.size:
            self.ball_speed_x *= -1
        if self.y <= 0 or self.y >= window_height - self.size:
            self.ball_speed_y *= -1

        if self.x <= bar_width + self.size / 2 and self.y >= ai_bar_y and self.y <= ai_bar_y + bar_height:
            self.ball_speed_x *= -1
        if self.x >= window_width - self.size - bar_width - bar_x and self.y >= player_bar_y and self.y <= player_bar_y + bar_height:
            self.ball_speed_x *= -1

    def draw(self, window):
        pygame.draw.ellipse(window, self.color, self.ball)
