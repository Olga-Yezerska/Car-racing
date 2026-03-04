import pygame
from classes.menu_drawer import MenuDrawer
from classes.interfaces import IDrawable
from classes.game_settings import GameSettings

class Menu(IDrawable):
    """
    Клас для керування ігровим меню.
    Відповідає за навігацію між пунктами, вибір налаштувань та перемикання режимів
    (головне меню, налаштування, пауза, кінець гри).
    """

    def __init__(self, screen, settings):
        """
        Ініціалізація меню та описів його пунктів.
        
        :param screen: поверхня для малювання
        :param settings: об'єкт GameSettings для доступу до параметрів гри
        """
        self.settings = settings
        
        # Списки пунктів для різних режимів меню
        self.main_items = ["Play", "Settings", "Exit"]
        self.settings_items = ["Car", "Road", "Music", "Volume"]
        self.pause_items = ["Resume", "Main Menu"]
        self.game_over_items = ["Restart", "Main Menu"]

        self.selected_index = 0  # Індекс поточного вибраного пункту
        self.mode = "main"       # Поточний режим меню (main, settings, pause, game_over)

        # Об'єкт, що відповідає за візуальне відображення меню
        self.drawer = MenuDrawer(screen, settings)

    def draw(self):
        """Викликає метод малювання через спеціалізований рендерер."""
        self.drawer.draw(self)

    def handle_input(self, input_data: dict) -> str:
        """
        Обробляє введення користувача для навігації по меню.
        
        :param input_data: словник з командами (up, down, enter, etc.)
        :return: рядок-команда для GameApp або None
        """
        if input_data.get("quit"):
            return "quit"

        # --- ГОЛОВНЕ МЕНЮ ---
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

        # --- НАЛАШТУВАННЯ ---
        elif self.mode == "settings":
            if input_data.get("up"):
                self.selected_index = (self.selected_index - 1) % len(self.settings_items)
            elif input_data.get("down"):
                self.selected_index = (self.selected_index + 1) % len(self.settings_items)
            elif input_data.get("left"):
                self._change_setting(-1)
            elif input_data.get("right"):
                self._change_setting(1)
            elif input_data.get("escape"):
                self.mode = "main"
                self.selected_index = 0

        # --- ПАУЗА ---
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

        # --- КІНЕЦЬ ГРИ ---
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

    def _change_setting(self, direction: int):
        """
        Приватний метод для зміни значень налаштувань (автомобіль, дорога, гучність).
        
        :param direction: напрямок зміни (-1 або 1)
        """
        item = self.settings_items[self.selected_index]
        
        if item == "Car":
            # Циклічний перебір доступних авто
            self.settings.car_index = (self.settings.car_index + direction) % len(self.settings.available_cars)
        
        elif item == "Road":
            # Циклічний перебір доступних трас
            self.settings.road_index = (self.settings.road_index + direction) % len(self.settings.available_roads)
        
        elif item == "Music":
            # Вибір треку та миттєве застосування
            self.settings.music_index = (self.settings.music_index + direction) % len(self.settings.music_library)
            self.settings.music_was_selected = True
            self.settings.apply_music()
        
        elif item == "Volume":            
            # Робота з гучністю (від 0.0 до 1.0)
            new_volume = self.settings.sound_volume + 0.1 * direction
            self.settings.sound_volume = min(1.0, max(0.0, new_volume))           
            self.settings.sound_volume = round(self.settings.sound_volume, 1)
            pygame.mixer.music.set_volume(self.settings.sound_volume)