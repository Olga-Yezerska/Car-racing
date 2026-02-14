import pygame
from classes.interfaces import IDrawable
from classes.game_settings import GameSettings

class Menu(IDrawable):
    def __init__(self, screen, settings: GameSettings):
        self.screen = screen
        self.settings = settings
        self.font = pygame.font.SysFont(None, 40)

        self.mode = "main"  # main / settings / pause
        self.font_big = pygame.font.SysFont(None, 72)
        self.font_small = pygame.font.SysFont(None, 40)

        self.resume_button = pygame.Rect(300, 260, 200, 50)
        self.menu_button = pygame.Rect(300, 330, 200, 50)


    def run(self, input_handler):
        while True:
            events = pygame.event.get()
            input_data = input_handler.handle_input(events)

            result = self.handle_input(input_data)

            if result:
               return result

            self.draw()
    
    def handle_input(self, input_data):
        if input_data.get("quit"):
            return "quit"

    # -------- MAIN MENU --------
        if self.mode == "main":

            if input_data.get("select_1"):
                return "start"

            if input_data.get("select_2"):
                self.mode = "settings"

            if input_data.get("escape"):
                return "quit"

    # -------- SETTINGS --------
        elif self.mode == "settings":

            if input_data.get("right"):
                self.settings.car_index = (
                  self.settings.car_index + 1
                ) % len(self.settings.available_cars)

            elif input_data.get("left"):
                self.settings.road_index = (
                    self.settings.road_index + 1
                ) % len(self.settings.available_roads)

            elif input_data.get("music"):
                self.settings.music_index = (
                    self.settings.music_index + 1
                ) % len(self.settings.music_library)

            elif input_data.get("up"):
                self.settings.sound_volume = min(
                    1.0, self.settings.sound_volume + 0.1)

            elif input_data.get("down"):
                self.settings.sound_volume = max(
                   0.0, self.settings.sound_volume - 0.1)

            elif input_data.get("escape"):
                self.mode = "main"

    # -------- PAUSE MENU --------
        elif self.mode == "pause":

            if input_data.get("select_1"):
                return "resume"
  
            if input_data.get("select_2"):
                return "menu"

            if input_data.get("escape"):
                return "resume"

        return None
    