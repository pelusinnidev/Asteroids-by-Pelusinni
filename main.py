import sys
import os

# Añadir el directorio src al PYTHONPATH
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from src.scenes.menu_scene import MenuScene
from src.scenes.game_scene import GameScene
from src.scenes.pause_scene import PauseScene
from src.scenes.intro_scene import IntroScene
from src.utils.constants import *
from src.core.managers.mongo_high_score_manager import MongoHighScoreManager
import pygame

# Inicializar Pygame
pygame.init()
pygame.mixer.init()  # Asegúrate de que el mixer está inicializado

# Función para cargar música con gestión de errores
def load_music(path):
    try:
        pygame.mixer.music.load(path)
    except pygame.error as e:
        pass

# Crear instancia de MongoHighScoreManager
high_score_manager = MongoHighScoreManager()

class Game:
    def __init__(self):
        # Inicializar en modo ventana
        self.screen = pygame.display.set_mode((DEFAULT_WIDTH, DEFAULT_HEIGHT))
        pygame.display.set_caption("Asteroids")
        self.clock = pygame.time.Clock()
        
        # Guardar el estado de la pantalla
        self.is_fullscreen = False
        
        self.menu_scene = MenuScene(high_score_manager)
        self.game_scene = None
        self.pause_scene = PauseScene()
        self.intro_scene = IntroScene()
        self.current_scene = "INTRO"
        
        # Flags para carga de música
        self.menu_music_loaded = False
        self.game_music_loaded = False
    
    def toggle_fullscreen(self):
        self.is_fullscreen = not self.is_fullscreen
        if self.is_fullscreen:
            info = pygame.display.Info()
            self.screen = pygame.display.set_mode((info.current_w, info.current_h), FULLSCREEN_MODE)
        else:
            self.screen = pygame.display.set_mode((DEFAULT_WIDTH, DEFAULT_HEIGHT), WINDOW_MODE)
    
    def run(self):
        try:
            while True:
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE and self.current_scene == "GAME":
                            pygame.mixer.music.pause()
                            self.current_scene = "PAUSE"

                if self.current_scene == "INTRO":
                    self._handle_intro(events)
                elif self.current_scene == "MENU":
                    self._handle_menu(events)
                elif self.current_scene == "GAME":
                    self._handle_game(events)
                elif self.current_scene == "PAUSE":
                    self._handle_pause(events)
                elif self.current_scene == "NEW_HIGHSCORE":
                    self._handle_new_highscore(events)

                pygame.display.flip()
                self.clock.tick(FPS)
        except KeyboardInterrupt:
            pygame.quit()
            sys.exit()

    def _handle_intro(self, events):
        if not self.game_music_loaded:
            load_music('src/assets/music/game_music.mp3')
            pygame.mixer.music.play(-1)
            self.game_music_loaded = True
        
        result = self.intro_scene.update()
        if result == "MENU":
            self.current_scene = "MENU"
            self.game_music_loaded = False
        
        self.intro_scene.draw(self.screen)
    
    def _handle_menu(self, events):
        if not self.menu_music_loaded:
            pygame.mixer.music.stop()
            load_music('src/assets/music/menu_music.mp3')
            pygame.mixer.music.play(-1)
            self.menu_music_loaded = True
            self.game_music_loaded = False
        
        for event in events:
            result = self.menu_scene.handle_input(event)
            if result == "PLAY":
                pygame.mixer.music.stop()
                self.game_scene = GameScene(high_score_manager)
                self.current_scene = "GAME"
                self.menu_music_loaded = False
            elif result == "QUIT":
                pygame.quit()
                sys.exit()
        
        self.menu_scene.draw(self.screen)
    
    def _handle_game(self, events):
        update_result = self.game_scene.update()
        if update_result == "MENU":
            pygame.mixer.music.stop()
            self.current_scene = "MENU"
            self.menu_music_loaded = False
            self.game_music_loaded = False
            self.game_scene = None
            return
        elif update_result == "NEW_HIGHSCORE":
            self.current_scene = "NEW_HIGHSCORE"
            return

        if not self.game_music_loaded:
            pygame.mixer.music.stop()
            load_music('src/assets/music/game_music.mp3')
            pygame.mixer.music.play(-1)
            self.game_music_loaded = True
            self.menu_music_loaded = False

        for event in events:
            result = self.game_scene.handle_input(event)
            if result == "QUIT":
                pygame.quit()
                sys.exit()
            elif result == "MENU":
                self.current_scene = "MENU"
            elif result == "NEW_HIGHSCORE":
                self.current_scene = "NEW_HIGHSCORE"
            elif result == "TOGGLE_FULLSCREEN":
                self.toggle_fullscreen()

        self.game_scene.draw(self.screen)

    def _handle_pause(self, events):
        for event in events:
            result = self.pause_scene.handle_input(event)
            if result == "RESUME":
                pygame.mixer.music.unpause()
                self.current_scene = "GAME"
            elif result == "MENU":
                pygame.mixer.music.stop()
                self.current_scene = "MENU"
        self.pause_scene.draw(self.screen)
    
    def _handle_new_highscore(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if self.game_scene:
                    if event.key == pygame.K_RETURN:
                        name = self.game_scene.player_name.strip() or "AAA"
                        high_score_manager.add_high_score(name, self.game_scene.score)
                        self.current_scene = "MENU"
                        self.game_scene = None
                    elif event.key == pygame.K_BACKSPACE:
                        self.game_scene.player_name = self.game_scene.player_name[:-1]
                    else:
                        if len(self.game_scene.player_name) < 3 and event.unicode.isalpha():
                            self.game_scene.player_name += event.unicode.upper()
        
        if self.game_scene:
            self.game_scene.draw(self.screen)

if __name__ == "__main__":
    game = Game()
    game.run()