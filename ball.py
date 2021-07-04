import pygame
from math import sqrt

class Ball:
    def __init__(self, WIDTH, HEIGHT, color):
        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        self.color = color
        self.size = 20
        self.ball_speed_x = 7
        self.ball_speed_y = 7
        self.ball = None

    def ball_cfg(self):
        self.ball = pygame.Rect(self.x, self.y, self.size, self.size)

    def get_ball_cfg(self):
        return self.ball

    def detect_collision(self, player, ai, sound):
        if self.ball.colliderect(player) or self.ball.colliderect(ai):
            sound.play_ball_sound()
            self.ball_speed_x *= -1

    def ball_animation(self, window_width, window_height, sound):
        self.x += self.ball_speed_x
        self.y += self.ball_speed_y

        if self.x <= 0 or self.x >= window_width - self.size:
            sound.play_ball_sound()
            self.ball_speed_x *= -1
        if self.y <= 0 or self.y >= window_height - self.size:
            sound.play_ball_sound()
            self.ball_speed_y *= -1

    def draw(self, window):
        pygame.draw.ellipse(window, self.color, self.ball)
