import pygame
import sys
from game import Game

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

# Create a screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Passive Mouse-Clicking Game")

font = pygame.font.Font(None, 36)


def main():
    clock = pygame.time.Clock()
    game = Game(screen, font)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        game.handle_events()
        game.update()
        game.render()

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
