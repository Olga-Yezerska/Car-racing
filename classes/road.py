import pygame
from classes.interfaces import IDrawable, IUpdatable
class Road(IUpdatable, IDrawable):
    """
    Клас дороги гри
    """
    def __init__(self, background_path: str, scroll_speed: int = 6, offset_y: int = 0):
        """
        Конструктор дороги
        Args: 
            background: фон / скін дороги
            scroll_speed: швидкість зміщення дороги / гравця
            offset_y: значення зміщення по у
        """
        self.background = pygame.image.load(background_path).convert()
        self.scroll_speed = scroll_speed
        self.offset_y = offset_y

    def update(self):
        """
        Метод оновлення позиції зміщення
        """
        self.offset_y += self.scroll_speed
        if self.offset_y >= self.background.get_height():
            self.offset_y -= self.background.get_height()

    def draw(self, screen: pygame.Surface):
        """
        Метод промалювання скіну дороги
        """
        screen.blit(self.background, (0, self.offset_y))
        screen.blit(self.background, (0, self.offset_y - self.background.get_height()))
        