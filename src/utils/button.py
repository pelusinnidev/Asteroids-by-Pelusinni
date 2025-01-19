import pygame
from src.utils.constants import *

class Button:
    def __init__(self, text, position, padding_x=40, padding_y=20):
        self.text = text
        self.position = position
        self.padding_x = padding_x
        self.padding_y = padding_y
        self.selected = False
        
        # Calculate button size based on text
        self.font = pygame.font.Font('src/assets/fonts/PressStart2P-Regular.ttf', 24)
        text_surface = self.font.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        
        # Adjust rectangle to text plus padding
        self.width = text_rect.width + (self.padding_x * 2)
        self.height = text_rect.height + (self.padding_y * 2)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.position
    
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and self.selected:
                print(f"Button '{self.text}' activated by ENTER key.")
                return True
        return False
    
    def draw(self, screen):
        # Draw selection rectangle if selected
        if self.selected:
            # Outer rectangle (border)
            pygame.draw.rect(screen, WHITE, self.rect, 2)
            
            # Inner rectangle (smaller for visual effect)
            inner_rect = self.rect.inflate(-4, -4)
            pygame.draw.rect(screen, WHITE, inner_rect, 1)
        
        # Render text
        text_surface = self.font.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
