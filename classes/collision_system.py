from classes.interfaces import ICollidable


class CollisionSystem:
    def __init__(self, player: ICollidable, obstacle_manager):
        """
        Ініціалізує систему зіткнень з гравцем і менеджером перешкод.
       
        :param player: Об'єкт автомобіля гравця, що реалізує ICollidable.
        :param obstacle_manager: Менеджер, що обробляє перешкоди.
        """
        self.player = player
        self.obstacle_manager = obstacle_manager

    def check_collisions(self) -> bool:
        """
        Перевіряє наявність зіткнень між гравцем і будь-якими перешкодами.
        
        :return: True, якщо виявлено зіткнення, False в іншому випадку.
        """
        for obstacle in self.obstacle_manager.obstacles:
            if self.player.get_rect().colliderect(obstacle.get_rect()):
                return True
        return False
