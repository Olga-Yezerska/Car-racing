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
    def draw_pause_menu(self):
    # Напівпрозорий фон
        overlay = pygame.Surface((800, 600))
        overlay.set_alpha(180)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))

        # Текст PAUSE
        pause_text = self.font_big.render("PAUSE", True, (255, 255, 255))
        self.screen.blit(pause_text, (310, 180))

        # Кнопка Продовжити
        pygame.draw.rect(self.screen, (50, 150, 50), self.resume_button)
        resume_text = self.font_small.render("Продовжити", True, (255, 255, 255))
        self.screen.blit(resume_text, (330, 270))

        # Кнопка Вийти
        pygame.draw.rect(self.screen, (150, 50, 50), self.menu_button)
        menu_text = self.font_small.render("Вийти", True, (255, 255, 255))
        self.screen.blit(menu_text, (360, 340))
  
    def draw(self):
    
        self.screen.fill((20, 20, 20))

        if self.mode == "main":
            self.draw_text("1 - Play", 200)
            self.draw_text("2 - Settings", 250)

        elif self.mode == "settings":
            self.draw_text(f"Car: {self.settings.available_cars[self.settings.car_index]}", 200)
            self.draw_text(f"Road: {self.settings.available_roads[self.settings.road_index]}", 240)
            self.draw_text(f"Music: {self.settings.music_library[self.settings.music_index]}", 280)
            self.draw_text(f"Volume: {round(self.settings.sound_volume,1)}", 320)
            self.draw_text("ESC - Back", 380)

        elif self.mode == "pause":
            self.draw_pause_overlay()

        pygame.display.flip()

    def draw_text(self, text, y):
        surface = self.font.render(text, True, (255, 255, 255))
        self.screen.blit(surface, (100, y))

    def draw_pause_overlay(self):
        overlay = pygame.Surface((800, 600))
        overlay.set_alpha(180)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))

        pause_text = self.font_big.render("PAUSE", True, (255, 255, 255))
        self.screen.blit(pause_text, (310, 180))

        pygame.draw.rect(self.screen, (50, 150, 50), self.resume_button)
        resume_text = self.font_small.render("Продовжити", True, (255, 255, 255))
        self.screen.blit(resume_text, (330, 270))

        pygame.draw.rect(self.screen, (150, 50, 50), self.menu_button)
        menu_text = self.font_small.render("Вийти", True, (255, 255, 255))
        self.screen.blit(menu_text, (360, 340))

