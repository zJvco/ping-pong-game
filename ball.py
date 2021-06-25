import pygame

class Ball:
    def __init__(self, x, y, color, size):
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.ball = None

    def ball_cfg(self):
        self.ball = pygame.Rect(self.x, self.y, self.size, self.size)

    def draw(self, window):
        pygame.draw.ellipse(window, self.color, self.ball)