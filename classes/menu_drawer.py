import pygame
from classes.interfaces import IDrawable

class MenuDrawer(IDrawable):
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        
        # Шрифти тепер живуть тут
        self.font_big = pygame.font.SysFont(None, 72)
        self.font_small = pygame.font.SysFont(None, 40)
        
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

    def draw(self, menu):
        # Логіка малювання фону
        if menu.mode not in ["pause", "game_over"]:
            self.screen.fill((20, 20, 20))

        # Вибір режиму відображення
        if menu.mode == "main":
            for i, item in enumerate(menu.main_items):
                self._draw_text(item, 200 + i * 50, i == menu.selected_index)

        elif menu.mode == "settings":
            values = [
                self.settings.available_cars[self.settings.car_index][0],
                self.settings.available_roads[self.settings.road_index][0],
                self.settings.get_music_name(),
                f"{int(self.settings.sound_volume * 100)}%"
            ]
            for i, (name, value) in enumerate(zip(menu.settings_items, values)):
                text = f"{name}: {value}"
                self._draw_text(text, 200 + i * 50, i == menu.selected_index)

            # Прев’ю машини
            car_path = self.settings.available_cars[self.settings.car_index][1]
            car_img = self.car_images.get(car_path)
            if car_img:
                self.screen.blit(car_img, self.car_preview_pos)

        elif menu.mode == "pause":
            self._draw_overlay("PAUSE", menu.pause_items, menu.selected_index)

        elif menu.mode == "game_over":
            self._draw_overlay("GAME OVER", menu.game_over_items, menu.selected_index)

    def _draw_text(self, text, y, selected=False):
        color = (255, 255, 0) if selected else (255, 255, 255)
        surf = self.font_small.render(text, True, color)
        self.screen.blit(surf, (100, y))

    def _draw_overlay(self, title_text, items, selected_index):
        overlay = pygame.Surface((800, 600))
        overlay.set_alpha(200)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))

        title = self.font_big.render(title_text, True, (255, 80, 80))
        self.screen.blit(title, (250, 160))

        for i, item in enumerate(items):
            selected = i == selected_index
            color = (255, 255, 0) if selected else (255, 255, 255)
            surf = self.font_small.render(item, True, color)
            self.screen.blit(surf, (330, 260 + i * 60))