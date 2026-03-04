import random
from classes.obstacle import Obstacle
from classes.player_car import PlayerCar

class ObstacleManager:
    def __init__(self, scroll_speed: int, screen_height: int = 600):
        """
        Ініціалізує менеджер перешкод.
        
        :param scroll_speed: Швидкість прокрутки дороги (використовується для переміщення перешкод).
        :param screen_height: Висота ігрового екрану (за замовчуванням 600).
        """
        self.scroll_speed = scroll_speed
        self.screen_height = screen_height
        self.obstacles = []
        
        # Визначаємо розмір "буферної зони" у пікселях (ширина, висота).
        # Це значення додається до розміру перешкоди для перевірки вільного місця.
        self.safe_margin = (130, 200)

    def update(self) -> None:
        """
        Оновлює всі перешкоди, випадково генерує нові та видаляє ті, що знаходяться поза екраном.
        """
        if random.random() < 0.025:
            x = random.randint(PlayerCar.LEFT_LIMIT + 30, PlayerCar.RIGHT_LIMIT - 30)
            
            # різні ймовірності для різних типів
            r = random.random()
            if r < 0.2:
                obs_type = "banana"
            elif r < 0.4:
                obs_type = "iguana"
            elif r < 0.6:
                obs_type = "paper_bag"
            elif r < 0.8:
                obs_type = "puddle"
            else:
                obs_type = "wheel"
                
            new_obs = Obstacle(x, obstacle_type=obs_type, speed=self.scroll_speed)
            safe_zone = new_obs.get_rect().inflate(self.safe_margin[0], self.safe_margin[1])
            
            safe_to_spawn = True
            for obs in self.obstacles:
                if safe_zone.colliderect(obs.get_rect()):
                    safe_to_spawn = False
                    break 
            
            if safe_to_spawn:
                self.obstacles.append(new_obs)

        for obs in self.obstacles[:]:
            obs.update()
            if obs.y > self.screen_height + 50:
                self.obstacles.remove(obs)