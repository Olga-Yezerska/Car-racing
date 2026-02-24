import pygame
from classes.interfaces import IDrawable
from classes.game_settings import GameSettings

class Menu(IDrawable):
    def __init__(self, screen, settings: GameSettings):
        self.screen = screen
        self.settings = settings
        self.font = pygame.font.SysFont(None, 40)
        self.main_items = ["Play", "Settings", "Exit"]
        self.settings_items = ["Car", "Road", "Music", "Volume"]
        self.pause_items = ["Resume", "Main Menu"]
        
        self.selected_index = 0

        self.mode = "main"  # main / settings / pause
        self.font_big = pygame.font.SysFont(None, 72)
        self.font_small = pygame.font.SysFont(None, 40)

        self.resume_button = pygame.Rect(300, 260, 200, 50)
        self.menu_button = pygame.Rect(300, 330, 200, 50)

        # ── Прев’ю машини в налаштуваннях ───────────────
        self.car_preview_pos = (480, 220)           # де малювати машину
        self.car_preview_size = (180, 360)          # розмір прев’ю 
        self.car_images = {}                        # кеш зображень

        # завантажуємо всі машини один раз
        self._preload_car_images()

    def _preload_car_images(self):
        for name, path in self.settings.available_cars:     # розпаковуємо кортеж
            try:
                img = pygame.image.load(path).convert_alpha()
                scaled = pygame.transform.scale(img, self.car_preview_size)
                self.car_images[path] = scaled   # ключем залишаємо шлях
            except Exception as e:
                print(f"Не вдалося завантажити {path}: {e}")
                surf = pygame.Surface(self.car_preview_size)
                surf.fill((60, 60, 80))
                self.car_images[path] = surf


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
           

            if input_data.get("up"):
                self.selected_index = (self.selected_index - 1) % len(self.main_items)
            
            elif input_data.get("down"):
                self.selected_index = (self.selected_index + 1) % len(self.main_items)

            elif input_data.get("enter"):
                choice = self.main_items[self.selected_index]

                if choice == "Play":
                    return "start"

                if choice == "Settings":
                    self.mode = "settings"
                    self.selected_index = 0

                if choice == "Exit":
                    return "quit"

    # -------- SETTINGS --------
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

    # -------- PAUSE MENU --------
        elif self.mode == "pause":

            if input_data.get("up"):
                self.selected_index = (self.selected_index - 1) % len(self.pause_items)

            elif input_data.get("down"):
                self.selected_index = (self.selected_index + 1) % len(self.pause_items)

            elif input_data.get("enter"):
                choice = self.pause_items[self.selected_index]

                if choice == "Resume":
                    return "resume"

                if choice == "Main Menu":
                    return "menu"

            elif input_data.get("escape"):
                return "resume"
            
    def _change_setting(self, direction):
        item = self.settings_items[self.selected_index]

        if item == "Car":
            self.settings.car_index = (
                self.settings.car_index + direction
            ) % len(self.settings.available_cars)

        elif item == "Road":
            self.settings.road_index = (
                self.settings.road_index + direction
            ) % len(self.settings.available_roads)

        elif item == "Music":
            self.settings.music_index = (
                self.settings.music_index + direction
            ) % len(self.settings.music_library)
            self.settings.apply_music()

        elif item == "Volume":
            self.settings.sound_volume = min(
                1.0, max(0.0, self.settings.sound_volume + 0.1 * direction)
                  )
            
    def draw_pause_overlay(self):
        overlay = pygame.Surface((800, 600))
        overlay.set_alpha(180)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))

        pause_text = self.font_big.render("PAUSE", True, (255, 255, 255))
        self.screen.blit(pause_text, (310, 160))

        for i, item in enumerate(self.pause_items):
            selected = i == self.selected_index
            color = (255, 255, 0) if selected else (255, 255, 255)

            text = self.font_small.render(item, True, color)
            self.screen.blit(text, (330, 260 + i * 60))
  
    def draw(self):
    
        self.screen.fill((20, 20, 20))

        if self.mode == "main":
            for i, item in enumerate(self.main_items):
               self.draw_text(item, 200 + i * 50, i == self.selected_index)

        elif self.mode == "settings":
           values = [
                self.settings.available_cars[self.settings.car_index][0],
                self.settings.available_roads[self.settings.road_index][0],
                self.settings.get_music_name(),
            f"{int(self.settings.sound_volume * 100)}%"]
           
           for i, (name, value) in enumerate(zip(self.settings_items, values)):
                text = f"{name}: {value}"
                self.draw_text(text, 200 + i * 50, i == self.selected_index)



        elif self.mode == "pause":
                self.draw_pause_overlay()

        pygame.display.flip()

    def draw_text(self, text, y, selected=False):
        color = (255, 255, 0) if selected else (255, 255, 255)
        surface = self.font.render(text, True, color)
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

