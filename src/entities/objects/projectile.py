import pygame
from pygame.math import Vector2
import math
from src.entities.base_entity import BaseEntity
from src.utils.constants import *

class Projectile(BaseEntity):
    def __init__(self, position, angle):
        super().__init__(position)
        self.radius = 2
        self.lifetime = 60  # Duration in frames
        self.speed = PROJECTILE_SPEED
        
        # Load and play laser sound
        self.laser_sound = pygame.mixer.Sound('src/assets/sfx/laser.mp3')
        self.laser_sound.set_volume(0.3)  # Adjust volume (0.0 to 1.0)
        self.laser_sound.play()
        
        # Calculate direction based on angle
        self.velocity = Vector2(0, -self.speed).rotate(-angle)
        print(f"New projectile created: pos={position}, vel={self.velocity}")  # Debug
    
    def update(self):
        super().update()
        self.lifetime -= 1
        
        # Deactivate projectile when expired
        if self.lifetime <= 0:
            self.active = False
        
        print(f"Projectile updated: pos={self.position}")  # Debug
    
    def draw(self, screen):
        if not self.active:
            return
            
        # Draw projectile as a small line
        end_pos = self.position + self.velocity.normalize() * 4
        pygame.draw.line(screen, WHITE, self.position, end_pos, 2)
    
    def get_radius(self):
        return self.radius
