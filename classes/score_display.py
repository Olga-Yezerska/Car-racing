import pygame
from classes.interfaces import IDrawable
from classes.score_manager import ScoreManager


class ScoreDisplay(IDrawable):
    """
    Клас реалізації виведення балів
    """
    def __init__(self, score_manager: ScoreManager, font_size: int = 36):
        """
        Ініціалізація об'єкту класу

        :param score_manager: менеджер управління балами
        :type score_manager: ScoreManager
        :param font_size: розмір шрифту на інтерфейсі
        :type font_size: int
        """
        self.score_manager = score_manager
        self.font = pygame.font.SysFont("arial", font_size, bold=True)
        self.color = (255, 255, 255)

    def draw(self, screen: pygame.Surface) -> None:
        """
        Функція малювання на екрані

        :param screen: екран для відображення - фон дороги
        :type screen: pygame.Surface
        """
        text = f"SCORE: {self.score_manager.get_score():,}"
        surface = self.font.render(text, True, self.color)
        screen.blit(surface, (20, 20))
