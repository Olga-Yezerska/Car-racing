import pygame
from classes.interfaces import ICollidable, IUpdatable, IDrawable

class Obstacle(ICollidable, IUpdatable, IDrawable):
    def __init__(self, x: int, obstacle_type: str = "normal", y: int = -50, speed: int = 6):
        """
        Ініціалізує об'єкт перешкоди.

        :param x: Початкове горизонтальне положення.
        :param x: Початкове горизонтальне положення.
        :param obstacle_type: Тип перешкоди.
        :param y: Початкове вертикальне положення (починається над екраном).
        :param speed: Швидкість, з якою перешкода рухається вниз по екрану.
        """
        self.x = x
        self.y = y
        self.speed = speed
        self.obstacle_type = obstacle_type
        
        if obstacle_type == "small":
            size = (50, 80)
            img_path = "obstacle.png"   # заглушки для різних типів
        elif obstacle_type == "large":
            size = (90, 140)
            img_path = "obstacle.png"
        elif obstacle_type == "truck":
            size = (80, 160)
            img_path = "obstacle.png"
        else:  # normal / default
            size = (65, 105)
            img_path = "obstacle.png"
        
        original = pygame.image.load(img_path).convert_alpha()
        self.image = pygame.transform.scale(original, size)
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def update(self) -> None:
        """
        Updates the obstacle's position by moving it down.
        """
        self.y += self.speed
        self.rect.centery = self.y

    def draw(self, screen: pygame.Surface) -> None:
        """
        Draws the obstacle on the screen.
        
        :param screen: The Pygame surface to draw on.
        """
        screen.blit(self.image, self.rect)

    def get_rect(self) -> pygame.Rect:
        """
        Returns the rectangle for collision detection.
        
        :return: The obstacle's Rect.
        """
        return self.rect