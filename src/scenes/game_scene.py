from pygame.math import Vector2
from src.entities.player.spaceship import Spaceship
from src.entities.objects.asteroid import Asteroid
from src.entities.objects.projectile import Projectile
from src.utils.constants import *
from src.core.managers.mongo_high_score_manager import MongoHighScoreManager


class GameScene:
    def __init__(self, high_score_manager: MongoHighScoreManager):
        self.player = Spaceship(Vector2(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.asteroids = []
        self.projectiles = []
        self.score = 0
        self.level = 1
        self.game_over = False
        self.new_highscore = False
        self.player_name = ""
        self.high_score_manager = high_score_manager
        
        self.high_score_manager.load_high_scores()
        self.highscores = self.high_score_manager.get_high_scores()
        self._spawn_asteroids()
        pygame.mixer.init()  # Initialize sound system
        print("Starting game. Current score: 0")
    
    def _spawn_asteroids(self):
        # Base number of asteroids increases with level
        num_asteroids = 3 + self.level

        # Calculate speed multiplier based on level (caps at 2x speed)
        speed_multiplier = min(1 + (self.level * 0.1), 2.0)
        
        print(f"Generating {num_asteroids} asteroids for round {self.level}.")
        print(f"Speed multiplier: {speed_multiplier}x")
        
        for _ in range(num_asteroids):
            # Create asteroid with modified speed based on level
            asteroid = Asteroid(size='large', speed_multiplier=speed_multiplier)
            self.asteroids.append(asteroid)
            print("Asteroid created.")
    
    def handle_input(self, event):
        if self.new_highscore:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    name = self.player_name.strip() or "AAA"
                    self.high_score_manager.add_high_score(name, self.score)
                    print(f"New high score added: {name} - {self.score}")
                    self.new_highscore = False
                    return "MENU"
                elif event.key == pygame.K_BACKSPACE:
                    self.player_name = self.player_name[:-1]
                    print(f"Deleting last character of name: {self.player_name}")
                else:
                    if len(self.player_name) < 3 and event.unicode.isalpha():
                        self.player_name += event.unicode.upper()
                        print(f"Current name input: {self.player_name}")
            return None

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not self.game_over:
                # Create projectile with sound
                self.projectiles.append(Projectile(self.player.position.copy(), self.player.angle))
                print("Projectile created and added to list.")
            elif event.key == pygame.K_LEFT:
                self.player.rotate(PLAYER_ROTATION_SPEED)
                print("Rotating ship left.")
            elif event.key == pygame.K_RIGHT:
                self.player.rotate(-PLAYER_ROTATION_SPEED)
                print("Rotating ship right.")
            elif event.key == pygame.K_UP:
                self.player.accelerate(forward=True)
                print("Ship accelerating forward.")
            elif event.key == pygame.K_DOWN:
                self.player.accelerate(forward=False)
                print("Ship accelerating backward.")
            elif event.key == KEY_FULLSCREEN:
                return "TOGGLE_FULLSCREEN"
        
        return None

    def update(self):
        if self.game_over:
            if not hasattr(self, 'game_over_music_played'):
                pygame.mixer.music.load('src/assets/music/game_over.mp3')
                pygame.mixer.music.play(0)  # Play once
                self.game_over_music_played = True
                print("Playing game over music.")
            
            if not pygame.mixer.music.get_busy():  # Check if music has finished
                if self.high_score_manager.is_high_score(self.score):
                    self.new_highscore = True
                    print("New high score achieved.")
                    return "NEW_HIGHSCORE"
                print("Game ending and returning to menu.")
                return "MENU"
            return None

        # Handle continuous key presses
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.rotate(PLAYER_ROTATION_SPEED)
            print("Rotating ship left.")
        if keys[pygame.K_RIGHT]:
            self.player.rotate(-PLAYER_ROTATION_SPEED)
            print("Rotating ship right.")
        if keys[pygame.K_UP]:
            self.player.accelerate(forward=True)
            print("Ship accelerating forward.")
        if keys[pygame.K_DOWN]:
            self.player.accelerate(forward=False)
            print("Ship accelerating backward.")

        # Update player
        self.player.update()
        print("Player updated.")
        
        # Update projectiles
        for projectile in self.projectiles[:]:  # Make a copy of the list to modify it
            projectile.update()
            if not projectile.active:
                self.projectiles.remove(projectile)
                print("Inactive projectile removed.")
        
        # Update asteroids
        for asteroid in self.asteroids:
            asteroid.update()
            print(f"Asteroid updated. Position: {asteroid.position}")
                
            if asteroid.collides_with(self.player):
                self.game_over = True
                print("Ship collided with an asteroid. Game Over.")
                return
        
        if not self.game_over:  # Only check collisions if not game over
            self._check_projectile_collisions()
        
        # Check if level is completed
        if len(self.asteroids) == 0:
            self.level += 1
            print(f"Level {self.level} completed.")
            self._spawn_asteroids()

    def _check_projectile_collisions(self):
        for projectile in self.projectiles[:]:
            for asteroid in self.asteroids[:]:
                if projectile.collides_with(asteroid):
                    self.score += asteroid.get_score()
                    print(f"Score increased. New total: {self.score}")
                    self.projectiles.remove(projectile)
                    print("Projectile removed after collision.")
                    self.asteroids.remove(asteroid)
                    print("Asteroid removed after collision.")
                    
                    # Create smaller asteroids if possible
                    new_asteroids = asteroid.split()
                    self.asteroids.extend(new_asteroids)
                    print(f"{len(new_asteroids)} smaller asteroid(s) created.")
                    break

    def draw(self, screen):
        screen.fill(BLACK)
        
        self.player.draw(screen)
        print("Ship drawn.")
        
        for projectile in self.projectiles:
            projectile.draw(screen)
            print("Projectile drawn.")
            
        for asteroid in self.asteroids:
            asteroid.draw(screen)
            print("Asteroid drawn.")
        
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score}", True, WHITE)
        round_text = font.render(f"Round: {self.level}", True, WHITE)
        screen.blit(score_text, (10, 10))
        screen.blit(round_text, (SCREEN_WIDTH - 150, 10))
        
        if self.game_over:
            # Draw game over text
            font = pygame.font.Font(None, 74)
            text = font.render('GAME OVER', True, RED)
            text_rect = text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 50))
            screen.blit(text, text_rect)
            
            if self.new_highscore:
                # Draw black rectangle behind name entry prompt
                prompt_font = pygame.font.Font(None, 36)
                prompt = prompt_font.render("New Highscore! Enter your name:", True, WHITE)
                prompt_rect = prompt.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 50))
                
                background_prompt = pygame.Surface((prompt_rect.width + 20, prompt_rect.height + 20))
                background_prompt.set_alpha(400)
                background_prompt.fill(BLACK)
                background_prompt_rect = background_prompt.get_rect(center=prompt_rect.center)
                
                screen.blit(background_prompt, background_prompt_rect)
                screen.blit(prompt, prompt_rect)
                
                # Show MongoDB status message
                status_message = self.high_score_manager.get_status_message()
                if status_message:
                    status_font = pygame.font.Font(None, 24)
                    status_text = status_font.render(status_message, True, YELLOW)
                    status_rect = status_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
                    screen.blit(status_text, status_rect)
                
                # Draw black rectangle behind player name
                name_font = pygame.font.Font(None, 48)
                name_surface = name_font.render(self.player_name, True, WHITE)
                name_rect = name_surface.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 100))
                
                background_name = pygame.Surface((name_rect.width + 20, name_rect.height + 20))
                background_name.set_alpha(400)
                background_name.fill(BLACK)
                background_name_rect = background_name.get_rect(center=name_rect.center)
                
                screen.blit(background_name, background_name_rect)
                screen.blit(name_surface, name_rect)
                print(f"Showing entered name: {self.player_name}")
