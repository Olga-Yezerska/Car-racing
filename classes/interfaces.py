from abc import ABC, abstractmethod
import pygame
class ICollidable(ABC):
    """Інтерфейс для об'єктів, які беруть участь у перевірці колізій"""
    @abstractmethod
    def get_rect(self) -> pygame.Rect:
        """Повертає прямокутник об'єкта для перевірки зіткнень"""
        pass
        
class IDrawable(ABC):
    """Інтерфейс для об'єктів, які потрібно намалювати"""
    @abstractmethod
    def draw(self, screen: pygame.Surface) -> None:
        """Малює об'єкт на екрані"""
        pass

class IUpdatable(ABC):
    """Інтерфейс для об'єктів, позиції / відображення яких потрібно оновлювати"""
    @abstractmethod
    def update(self) -> None:
        """Оновлює стан об'єкта (позицію, анімацію)"""
        pass