import pygame

class Bar:
    def __init__(self, x, y, color, width, height, bar_speed):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
        self.bar_speed = bar_speed
        self.bar = None

    def bar_cfg(self):
        self.bar = pygame.Rect(self.x, self.y, self.width, self.height)

    def player_animation(self, window_height):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.y > 0 + 10:
            self.y -= self.bar_speed
        if keys[pygame.K_DOWN] and self.y < window_height - self.height - 10:
            self.y += self.bar_speed

    def ai_animation(self, window_height, ball_y):
        self.y = ball_y - self.height / 2

        if self.y <= 10:
            self.y = 10
        if self.y + self.height >= window_height - 10:
            self.y = window_height - self.height - 10

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.bar)
