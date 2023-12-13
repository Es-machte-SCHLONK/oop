import pygame
import random

# Initialize Pygame
pygame.init()

# Set the width and height of the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Set the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set the game window size
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Tower Defense Game")

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Create a class for the player's tower
class Tower(pygame.sprite.Sprite):
    """
    Class to represent the player's tower.

    Attributes:
    - image: pygame.Surface
        The image of the tower.
    - rect: pygame.Rect
        The rectangle that defines the position and size of the tower.
    """

    def __init__(self):
        """
        Constructor to initialize the Tower class.

        Initializes the image and rect attributes.
        """

        super().__init__()

        # Load the tower image
        self.image = pygame.image.load("tower.png").convert_alpha()

        # Set the initial position of the tower
        self.rect = self.image.get_rect()
        self.rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT - 50)

    def update(self):
        """
        Update the tower's position.

        The tower follows the mouse cursor.
        """

        # Get the current position of the mouse cursor
        mouse_pos = pygame.mouse.get_pos()

        # Update the position of the tower to the current mouse position
        self.rect.center = mouse_pos

    def draw(self):
        """
        Draw the tower on the game window.
        """

        game_window.blit(self.image, self.rect)

# Create a class for the enemy
class Enemy(pygame.sprite.Sprite):
    """
    Class to represent the enemy.

    Attributes:
    - image: pygame.Surface
        The image of the enemy.
    - rect: pygame.Rect
        The rectangle that defines the position and size of the enemy.
    - speed: int
        The speed at which the enemy moves.
    """

    def __init__(self):
        """
        Constructor to initialize the Enemy class.

        Initializes the image, rect, and speed attributes.
        """

        super().__init__()

        # Load the enemy image
        self.image = pygame.image.load("enemy.png").convert_alpha()

        # Set the initial position of the enemy
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, WINDOW_WIDTH - 50), 50)

        # Set the speed of the enemy
        self.speed = random.randint(1, 3)

    def update(self):
        """
        Update the enemy's position.

        The enemy moves downwards at a constant speed.
        """

        # Move the enemy downwards
        self.rect.y += self.speed

    def draw(self):
        """
        Draw the enemy on the game window.
        """

        game_window.blit(self.image, self.rect)

# Create a group to hold all the sprites
all_sprites = pygame.sprite.Group()

# Create the player's tower
tower = Tower()
all_sprites.add(tower)

# Create a group to hold the enemies
enemies = pygame.sprite.Group()

# Create a variable to control the spawning of enemies
spawn_counter = 0
spawn_rate = 60  # Spawn a new enemy every 60 frames

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the tower
    tower.update()

    # Spawn enemies
    spawn_counter += 1
    if spawn_counter >= spawn_rate:
        enemy = Enemy()
        enemies.add(enemy)
        all_sprites.add(enemy)
        spawn_counter = 0

    # Update the enemies
    enemies.update()

    # Clear the game window
    game_window.fill(BLACK)

    # Draw all the sprites
    all_sprites.draw(game_window)

    # Update the game window
    pygame.display.update()

    # Set the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()