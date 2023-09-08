import pygame
import random

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60


class Game:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.level = 1
        self.score = 0
        self.threshold = 10
        self.current_image = None
        self.enemy_appeared = False
        self.load_images()

    def load_images(self):
        # Load images for different levels
        self.level_images = {
            1: pygame.image.load("level1.png"),
            2: pygame.image.load("level2.png"),
            # Add more levels and images here
        }

        # Load background images
        self.background_images = {
            "background1": pygame.image.load("forest.jpg"),
            "background2": pygame.image.load("forest2.jpg"),
            # Add more backgrounds here
        }

        # Load enemy images
        self.enemy_images = [
            pygame.image.load("enemy1.png"),
            pygame.image.load("enemy2.png"),
            # Add more enemy images here
        ]

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                image = self.level_images.get(
                    self.level, self.level_images[max(self.level_images.keys())]
                )
                image_rect = image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
                if image_rect.collidepoint(x, y):
                    self.score += self.level
                    if self.score >= self.threshold:
                        self.change_level()
                        self.handle_enemy_appearance()

    def change_level(self):
        self.level += 1
        self.threshold *= 2
        self.current_image = self.level_images.get(
            self.level, self.level_images[max(self.level_images.keys())]
        )

    def handle_enemy_appearance(self):
        # Implement logic for enemy appearance here
        self.enemy_appeared = True

    def update(self):
        # Implement game logic here
        pass

    def render(self):
        # Clear the screen and draw the background
        self.screen.fill(WHITE)
        self.screen.blit(
            self.background_images.get(
                "background1", self.background_images["background1"]
            ),
            (0, 0),
        )

        # Draw the current image
        self.screen.blit(
            self.current_image,
            (
                WIDTH // 2 - self.current_image.get_width() // 2,
                HEIGHT // 2 - self.current_image.get_height() // 2,
            ),
        )

        # Draw the score and level
        text = self.font.render(
            f"Score: {self.score} | Level: {self.level}", True, BLACK
        )
        self.screen.blit(text, (20, 20))

        # Draw the enemy if it appeared
        if self.enemy_appeared:
            enemy_image = random.choice(self.enemy_images)
            self.screen.blit(
                enemy_image,
                (
                    random.randint(0, WIDTH - enemy_image.get_width()),
                    random.randint(0, HEIGHT - enemy_image.get_height()),
                ),
            )
