import random
from classes.obstacle import Obstacle
from classes.player_car import PlayerCar

class ObstacleManager:
    def __init__(self, scroll_speed: int, screen_height: int = 600):
        """
        Initializes the obstacle manager.
        
        :param scroll_speed: The speed at which the road scrolls (used for obstacle movement).
        :param screen_height: The height of the game screen (default 600).
        """
        self.scroll_speed = scroll_speed
        self.screen_height = screen_height
        self.obstacles = []

    def update(self) -> None:
        """
        Updates all obstacles, generates new ones randomly, and removes off-screen ones.
        """
        if random.random() < 0.025:
            x = random.randint(PlayerCar.LEFT_LIMIT + 30, PlayerCar.RIGHT_LIMIT - 30)
            
            # різні ймовірності для різних типів
            r = random.random()
            if r < 0.15:
                obs_type = "small"
            elif r < 0.25:
                obs_type = "large"
            elif r < 0.30:
                obs_type = "truck"
            else:
                obs_type = "normal"
                
            obs = Obstacle(x, obstacle_type=obs_type, speed=self.scroll_speed)
            self.obstacles.append(obs)

        # Update existing obstacles and remove those off-screen
        for obs in self.obstacles[:]:
            obs.update()
            if obs.y > self.screen_height + 50:
                self.obstacles.remove(obs)