from abc import ABC, abstractmethod
import pygame
class ICollidable(ABC):
    @abstractmethod
    def get_rect(self) -> pygame.Rect:
        pass
        
