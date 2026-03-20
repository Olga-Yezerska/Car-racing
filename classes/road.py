import pygame
from classes.interfaces import IDrawable, IUpdatable


class Road(IUpdatable, IDrawable):
    """
    Клас дороги гри
    """
    def __init__(self, background_path: str, scroll_speed: int = 6, offset_y: int = 0):
        """
        Ініціалізація об'єкту дорога

        :param background_path: шлях до зображення
        :type background_path: str
        :param scroll_speed: швидкість зміщення
        :type scroll_speed: int
        :param offset_y: на скільки зміщення по у
        :type offset_y: int
        """
        original_bg = pygame.image.load(background_path).convert()
        screen_width = pygame.display.get_surface().get_width()

        self.background = pygame.transform.scale(original_bg, (screen_width, original_bg.get_height()))
        self.scroll_speed = scroll_speed
        self.offset_y = offset_y
        self.on_cycle_complete = None

    def update(self):
        """
        Метод оновлення позиції зміщення
        """
        self.offset_y += self.scroll_speed
        if self.offset_y >= self.background.get_height():
            self.offset_y -= self.background.get_height()

            if self.on_cycle_complete is not None:
                self.on_cycle_complete()

    def draw(self, screen: pygame.Surface):
        """
        Метод промалювання скіну дороги

        :param screen: зображення дороги
        :type screen: pygame.Surface
        """
        screen.blit(self.background, (0, self.offset_y))
        screen.blit(self.background, (0, self.offset_y - self.background.get_height()))
