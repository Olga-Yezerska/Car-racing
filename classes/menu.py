import pygame
from classes.interfaces import IDrawable
from classes.game_settings import GameSettings

class Menu(IDrawable):
    def __init__(self, screen, settings: GameSettings):
        self.screen = screen
        self.settings = settings

        # Шрифти
        self.font_big = pygame.font.SysFont(None, 72)
        self.font_small = pygame.font.SysFont(None, 40)

        # Пункти меню
        self.main_items = ["Play", "Settings", "Exit"]
        self.settings_items = ["Car", "Road", "Music", "Volume"]
        self.pause_items = ["Resume", "Main Menu"]
        self.game_over_items = ["Restart", "Main Menu"]

        self.selected_index = 0
        self.mode = "main"  # main / settings / pause / game_over

        # Прев’ю машини
        self.car_preview_pos = (480, 220)
        self.car_preview_size = (180, 360)
        self.car_images = {}
        self._preload_car_images()

    def _preload_car_images(self):
        for name, path in self.settings.available_cars:
            try:
                img = pygame.image.load(path).convert_alpha()
                scaled = pygame.transform.scale(img, self.car_preview_size)
                self.car_images[path] = scaled
            except Exception as e:
                print(f"Не вдалося завантажити {path}: {e}")
                surf = pygame.Surface(self.car_preview_size)
                surf.fill((60, 60, 80))
                self.car_images[path] = surf

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
            self.settings.sound_volume = min(1.0, max(0.0, self.settings.sound_volume + 0.1 * direction))

    def draw(self):
        # Фон тільки для меню та налаштувань (гра залишається видимою за оверлеєм у паузі)
        if self.mode not in ["pause", "game_over"]:
            self.screen.fill((20, 20, 20))

        if self.mode == "main":
            for i, item in enumerate(self.main_items):
                self._draw_text(item, 200 + i * 50, i == self.selected_index)

        elif self.mode == "settings":
            values = [
                self.settings.available_cars[self.settings.car_index][0],
                self.settings.available_roads[self.settings.road_index][0],
                self.settings.get_music_name(),
                f"{int(self.settings.sound_volume * 100)}%"
            ]
            for i, (name, value) in enumerate(zip(self.settings_items, values)):
                text = f"{name}: {value}"
                self._draw_text(text, 200 + i * 50, i == self.selected_index)

            # Прев’ю машини
            car_path = self.settings.available_cars[self.settings.car_index][1]
            car_img = self.car_images.get(car_path)
            if car_img:
                self.screen.blit(car_img, self.car_preview_pos)

        elif self.mode == "pause":
            self._draw_overlay("PAUSE", self.pause_items)

        elif self.mode == "game_over":
            self._draw_overlay("GAME OVER", self.game_over_items)


    def _draw_text(self, text, y, selected=False):
        color = (255, 255, 0) if selected else (255, 255, 255)
        surf = self.font_small.render(text, True, color)
        self.screen.blit(surf, (100, y))

    def _draw_overlay(self, title_text, items):
        overlay = pygame.Surface((800, 600))
        overlay.set_alpha(200)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))

        title = self.font_big.render(title_text, True, (255, 80, 80))
        self.screen.blit(title, (250, 160))

        for i, item in enumerate(items):
            selected = i == self.selected_index
            color = (255, 255, 0) if selected else (255, 255, 255)
            surf = self.font_small.render(item, True, color)
            self.screen.blit(surf, (330, 260 + i * 60))