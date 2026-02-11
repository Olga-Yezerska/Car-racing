import pygame
from classes.interfaces import ICollidable, IUpdatable, IDrawable
class PlayerCar(ICollidable, IUpdatable, IDrawable):
    LEFT_LIMIT = 140
    RIGHT_LIMIT = 660
    def __init__(self, car_skin: str, x: int = 400, y: int = 500, speed: int = 5):
        """
        Конструктор машини гравця
        Args:
            x: початкова горизонтальна позиція 
            y: вертикальна позиція 
            speed: швидкість руху
            car_skin: шлях до файлу зображення машини
        """
        self.x = x
        self.y = y
        self.speed = speed
        self.image = pygame.image.load(car_skin).convert_alpha() #скін машини
        self.rect = self.image.get_rect(center=(self.x, self.y)) #

    def move_left(self):
        """
        Метод руху вліво
        """
        self.x -= self.speed
        if self.x < PlayerCar.LEFT_LIMIT:
            self.x = PlayerCar.LEFT_LIMIT 
        self.rect.centerx = self.x

    def move_left(self):
        """
        Метод руху вправо
        """
        self.x += self.speed
        if self.x > PlayerCar.LEFT_LIMIT:
            self.x = PlayerCar.LEFT_LIMIT 
        self.rect.centerx = self.x

