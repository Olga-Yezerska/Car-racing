import pygame
from classes.interfaces import ICollidable, IUpdatable, IDrawable

class Obstacle(ICollidable, IUpdatable, IDrawable):
    def __init__(self, x: int, y: int = -50, speed: int = 6):
        self.x = x
        self.y = y
        self.speed = speed
        original = pygame.image.load("obstacle.png").convert_alpha()
        self.image = pygame.transform.scale(original, (60, 100))
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def update(self) -> None:
        self.y += self.speed
        self.rect.centery = self.y

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.image, self.rect)

    def get_rect(self) -> pygame.Rect:
        return self.rect