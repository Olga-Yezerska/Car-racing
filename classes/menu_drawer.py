import pygame
from .interfaces import IDrawable

class MenuDrawer(IDrawable):
    """
    Клас-рендерер, що відповідає за візуальне відображення інтерфейсу меню.
    Відокремлює логіку малювання від логіки керування (клас Menu).
    """
    def __init__(self, screen, settings):
        """
        Ініціалізація ресурсів для малювання меню.
        
        :param screen: поверхня Pygame для виводу зображення
        :param settings: об'єкт налаштувань для отримання шляхів до ресурсів
        """
        self.screen = screen
        self.settings = settings
        

        self.font_big = pygame.font.SysFont(None, 72)
        self.font_small = pygame.font.SysFont(None, 40)
        
  
        self.car_preview_pos = (480, 120)
        self.car_preview_size = (180, 360)
        

        self.car_images = {}
        self.background_images = {}
        

        self._preload_car_images()
        self._preload_background_images()

    def _preload_background_images(self):
        """Завантажує та оптимізує фонові зображення для різних режимів меню."""
        for mode, path in self.settings.menu_backgrounds.items():
            try:
                img = pygame.image.load(path).convert()
                # Масштабування під розмір екрана
                img = pygame.transform.scale(img, self.screen.get_size())
                self.background_images[mode] = img
            except Exception as e:
                print(f"Не вдалося завантажити фон {path}: {e}")
                # Створення заглушки у разі помилки
                surf = pygame.Surface(self.screen.get_size())
                surf.fill((20, 20, 20))
                self.background_images[mode] = surf

    def _preload_car_images(self):
        """Завантажує та масштабує зображення автомобілів для меню налаштувань."""
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
        """
        Головний метод рендерингу меню залежно від його поточного стану (режиму).
        
        :param menu: об'єкт класу Menu, що містить поточний стан та індекси
        """
      
        if menu.mode in self.background_images:
            self.screen.blit(self.background_images[menu.mode], (0, 0))
        elif menu.mode not in ["pause", "game_over"]:
            self.screen.fill((20, 20, 20))
        

        if menu.mode == "main":
            overlay = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 40))  
            self.screen.blit(overlay, (0, 0)) 

        if menu.mode == "settings":
            overlay = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 160))  
            self.screen.blit(overlay, (0, 0)) 

        if menu.mode == "main":
            screen_center_x = self.screen.get_width() // 2

            for i, item in enumerate(menu.main_items):
                selected = i == menu.selected_index
                text_color = (255, 255, 0) if selected else (255, 255, 255)
                text_surf = self.font_small.render(item, True, text_color)

                padding_x, padding_y = 30, 12
                rect_width = text_surf.get_width() + padding_x * 2
                rect_height = text_surf.get_height() + padding_y * 2
                x = screen_center_x - rect_width // 2
                y = 200 + i * 60

                rect_surf = pygame.Surface((rect_width, rect_height), pygame.SRCALPHA)
                rect_color = (0, 0, 0, 220) if selected else (0, 0, 0, 120)
                pygame.draw.rect(rect_surf, rect_color, rect_surf.get_rect(), border_radius=14)

                self.screen.blit(rect_surf, (x, y))
                self.screen.blit(text_surf, (x + padding_x, y + padding_y))

        elif menu.mode == "settings":
            values = [
                self.settings.available_cars[self.settings.car_index][0],
                self.settings.available_roads[self.settings.road_index][0],
                self.settings.get_music_name(),
                f"{int(self.settings.sound_volume * 100)}%"
            ]

            for i, (name, value) in enumerate(zip(menu.settings_items, values)):
                text = f"{name}: {value}"
                self._draw_text(text, 190 + i * 50, i == menu.selected_index)
            
            car_path = self.settings.available_cars[self.settings.car_index][1]
            car_img = self.car_images.get(car_path)
            if car_img:
                self.screen.blit(car_img, self.car_preview_pos)


        elif menu.mode == "pause":
            self._draw_overlay("PAUSE", menu.pause_items, menu.selected_index)

        elif menu.mode == "game_over":
            self._draw_overlay("GAME OVER", menu.game_over_items, menu.selected_index)

    def _draw_text(self, text, y, selected=False):
        """Допоміжний метод для малювання рядка тексту в налаштуваннях."""
        color = (255, 255, 0) if selected else (255, 255, 255)
        surf = self.font_small.render(text, True, color)
        self.screen.blit(surf, (100, y))

    def _draw_overlay(self, title_text, items, selected_index):
        """
        Малює повноцінне модальне вікно (для паузи або кінця гри).
        
        :param title_text: великий заголовок зверху
        :param items: список кнопок
        :param selected_index: індекс вибраної кнопки
        """
        screen_w, screen_h = self.screen.get_size()
        center_x = screen_w // 2

        overlay = pygame.Surface((screen_w, screen_h), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 200))
        self.screen.blit(overlay, (0, 0))

     
        title_surf = self.font_big.render(title_text, True, (255, 80, 80))
        self.screen.blit(title_surf, (center_x - title_surf.get_width() // 2, 140))


        for i, item in enumerate(items):
            selected = i == selected_index
            text_color = (255, 255, 0) if selected else (255, 255, 255)
            text_surf = self.font_small.render(item, True, text_color)

            padding_x, padding_y = 32, 14
            rect_w, rect_h = text_surf.get_width() + padding_x * 2, text_surf.get_height() + padding_y * 2
            x, y = center_x - rect_w // 2, 260 + i * 65

            rect_surf = pygame.Surface((rect_w, rect_h), pygame.SRCALPHA)
            rect_color = (0, 0, 0, 200) if selected else (0, 0, 0, 140)
            pygame.draw.rect(rect_surf, rect_color, rect_surf.get_rect(), border_radius=16)

            self.screen.blit(rect_surf, (x, y))
            self.screen.blit(text_surf, (x + padding_x, y + padding_y))