import pygame

# Game version
GAME_VERSION = "v2.2.4"

# Screen dimensions (default)
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Game configuration
FPS = 60
PLAYER_ACCELERATION = 0.15
PLAYER_MAX_SPEED = 4
PLAYER_ROTATION_SPEED = 5
PLAYER_FRICTION = 0.98

# Projectile configuration
PROJECTILE_SPEED = 12

# Asteroid configuration
ASTEROID_SPEEDS = {
    'large': 1,
    'medium': 2,
    'small': 3
}

ASTEROID_SCORES = {
    'large': 20,
    'medium': 50,
    'small': 100
}

# Control keys
KEY_FULLSCREEN = pygame.K_F11
KEY_EXIT_FULLSCREEN = pygame.K_ESCAPE

# Add these constants
WINDOW_MODE = 0  # Window mode
FULLSCREEN_MODE = pygame.FULLSCREEN
DEFAULT_WIDTH = 1280
DEFAULT_HEIGHT = 720
