import pygame, sys
from sound import Sound
from game import Game

class Main:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Ping Pong")

        self.WIDTH = 1000
        self.HEIGHT = 600
        self.WINDOW = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.BLACK = (0, 0, 0)
        self.font = pygame.font.SysFont("comicsans", 50)
        self.FPS = 60
        self.clock = pygame.time.Clock()
        self.sound = Sound()

    def main_loop(self):
        run = True

        self.sound.volume_control(0.1)
        game = Game(self.WIDTH, self.HEIGHT, self.clock, self.FPS, self.font, self.sound)

        while run:
            self.WINDOW.fill(self.BLACK)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            game.game_loop(self.WINDOW, self.WIDTH, self.HEIGHT)

            pygame.display.update()
            self.clock.tick(self.FPS)

if __name__ == "__main__":
    Main().main_loop()
