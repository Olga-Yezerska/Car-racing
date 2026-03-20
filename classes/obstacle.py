import pygame
from classes.interfaces import ICollidable, IUpdatable, IDrawable


class Obstacle(ICollidable, IUpdatable, IDrawable):
    def __init__(self, x: int, obstacle_type: str = "normal", y: int = -50, speed: int = 6):
        """
        Ініціалізує об'єкт перешкоди.

        :param x: Початкове горизонтальне положення.
        :param obstacle_type: Тип перешкоди.
        :param y: Початкове вертикальне положення (починається над екраном).
        :param speed: Швидкість, з якою перешкода рухається вниз по екрану.
        """
        self.x = x
        self.y = y
        self.speed = speed
        self.obstacle_type = obstacle_type

        if obstacle_type == "wheel":
            size = (80, 80)
            img_path = "assets\\Obstacles\\wheel.png"
        elif obstacle_type == "banana":
            size = (70, 70)
            img_path = "assets\\Obstacles\\banana.png"
        elif obstacle_type == "puddle":
            size = (90, 90)
            img_path = "assets\\Obstacles\\puddle.png"
        elif obstacle_type == "paper_bag":
            size = (80, 80)
            img_path = "assets\\Obstacles\\paper_bag.png"
        else:
            size = (90, 90)
            img_path = "assets\\Obstacles\\iguana.png"

        original = pygame.image.load(img_path).convert_alpha()
        self.image = pygame.transform.scale(original, size)
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def update(self) -> None:
        """
        Оновлює положення перешкоди, переміщуючи її вниз.
        """
        self.y += self.speed
        self.rect.centery = self.y

    def draw(self, screen: pygame.Surface) -> None:
        """
        Малює перешкоду на екрані.

        :param screen: Поверхня Pygame, на якій буде малюватись.
        """
        screen.blit(self.image, self.rect)

    def get_rect(self) -> pygame.Rect:
        """
        Повертає прямокутник для виявлення зіткнення.

        :return: Прямокутник перешкоди.
        """
        return self.rect
