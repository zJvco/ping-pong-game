import pygame

class Ball:
    def __init__(self, x, y, color, size):
        self.x = x
        self.y = y
        self.color = color
        self.size = size

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.size)