import pygame
from classes.menu_drawer import MenuDrawer
from classes.interfaces import IDrawable
from classes.game_settings import GameSettings

class Menu(IDrawable):

    def __init__(self, screen, settings):
        self.settings = settings
        self.main_items = ["Play", "Settings", "Exit"]
        self.settings_items = ["Car", "Road", "Music", "Volume"]
        self.pause_items = ["Resume", "Main Menu"]
        self.game_over_items = ["Restart", "Main Menu"]

        self.selected_index = 0
        self.mode = "main"

        # Створюємо рендерер
        self.drawer = MenuDrawer(screen, settings)

    def draw(self):
        self.drawer.draw(self)

    def handle_input(self, input_data):
        if input_data.get("quit"):
            return "quit"

    # --- MAIN MENU ---
        if self.mode == "main":
            if input_data.get("up"):
                self.selected_index = (self.selected_index - 1) % len(self.main_items)
            elif input_data.get("down"):
                self.selected_index = (self.selected_index + 1) % len(self.main_items)
            elif input_data.get("enter"):
                choice = self.main_items[self.selected_index]
                if choice == "Play":
                    return "start"
                elif choice == "Settings":
                    self.mode = "settings"
                    self.selected_index = 0
                elif choice == "Exit":
                    return "quit"

    # --- SETTINGS ---
        elif self.mode == "settings":
            if input_data.get("up"):
                self.selected_index = (self.selected_index - 1) % len(self.settings_items)
            elif input_data.get("down"):
                self.selected_index = (self.selected_index + 1) % len(self.settings_items)
            elif input_data.get("left"):
                self._change_setting(-1)
            elif input_data.get("right"):
                self._change_setting(1)
            elif input_data.get("enter"):
            # Enter у налаштуваннях не виходить з меню, просто залишаємо
                pass
            elif input_data.get("escape"):
                self.mode = "main"
                self.selected_index = 0

         # --- PAUSE ---
        elif self.mode == "pause":
            if input_data.get("up"):
                self.selected_index = (self.selected_index - 1) % len(self.pause_items)
            elif input_data.get("down"):
                self.selected_index = (self.selected_index + 1) % len(self.pause_items)
            if input_data.get("enter"):
                choice = self.pause_items[self.selected_index]
                if choice == "Resume":
                    return "resume"
                elif choice == "Main Menu":
                    return "menu"

    # --- GAME OVER ---
        elif self.mode == "game_over":
            if input_data.get("up"):
                self.selected_index = (self.selected_index - 1) % len(self.game_over_items)
            elif input_data.get("down"):
                self.selected_index = (self.selected_index + 1) % len(self.game_over_items)
            if input_data.get("enter"):
                choice = self.game_over_items[self.selected_index]
                if choice == "Restart":
                    return "restart"
                elif choice == "Main Menu":
                    return "menu"

        return None

    def _change_setting(self, direction):
        '''Змінює налаштування в залежності від вибраного пункту та напрямку (вліво/вправо)'''
        item = self.settings_items[self.selected_index]
        if item == "Car":
            self.settings.car_index = (self.settings.car_index + direction) % len(self.settings.available_cars)
        elif item == "Road":
            self.settings.road_index = (self.settings.road_index + direction) % len(self.settings.available_roads)
        elif item == "Music":
            self.settings.music_index = (self.settings.music_index + direction) % len(self.settings.music_library)
            self.settings.music_was_selected = True
            self.settings.apply_music()
        elif item == "Volume":            
            new_volume = self.settings.sound_volume + 0.1 * direction
            self.settings.sound_volume = min(1.0, max(0.0, new_volume))           
            self.settings.sound_volume = round(self.settings.sound_volume, 1)
            pygame.mixer.music.set_volume(self.settings.sound_volume) 

    