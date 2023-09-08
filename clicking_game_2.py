import pygame
import sys
import random
import math

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

# Load images for different levels and backgrounds
level_images = {
    1: pygame.image.load("level1.png"),
    2: pygame.image.load("level2.png"),
    # Add more levels and images here
}

background_images = {
    "background1": pygame.image.load("forest.jpg"),
    "background2": pygame.image.load("forest2.jpg"),
    # Add more backgrounds here
}

# Initialize game variables
score = 0
level = 1
threshold = 10  # Score required to level up
current_image_index = 1  # Start with level 1 image
current_background = "background1"  # Start with background 1

font = pygame.font.Font(None, 36)


# Function to change the level and update the image
def change_level():
    global level, threshold, current_image_index
    level += 1
    threshold *= 2  # Increase the threshold when changing level
    current_image_index = level if level in level_images else max(level_images.keys())


# Function to handle enemy appearance
def handle_enemy_appearance():
    # Implement logic for enemy appearance here
    pass


def main():
    global score, level

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                image = level_images.get(level, level_images[max(level_images.keys())])
                image_rect = image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
                if image_rect.collidepoint(x, y):
                    score += level
                    if score >= threshold:
                        change_level()
                        handle_enemy_appearance()

        # Clear the screen and draw the background
        screen.fill(WHITE)
        screen.blit(background_images[current_background], (0, 0))

        # Draw the current image
        image = level_images.get(level, level_images[max(level_images.keys())])
        screen.blit(
            image,
            (
                WIDTH // 2 - image.get_width() // 2,
                HEIGHT // 2 - image.get_height() // 2,
            ),
        )

        # Draw the score and level
        text = font.render(f"Score: {score} | Level: {level}", True, BLACK)
        screen.blit(text, (20, 20))

        # Update the screen
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)


if __name__ == "__main__":
    main()
