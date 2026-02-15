import random
from classes.obstacle import Obstacle
from classes.player_car import PlayerCar

class ObstacleManager:
    def __init__(self, scroll_speed: int, screen_height: int = 600):
        self.scroll_speed = scroll_speed
        self.screen_height = screen_height
        self.obstacles = []

    def update(self) -> None:
        # Randomly generate a new obstacle with a small probability per frame
        if random.random() < 0.02:  # Adjust probability for desired spawn rate
            x = random.randint(PlayerCar.LEFT_LIMIT, PlayerCar.RIGHT_LIMIT)
            new_obstacle = Obstacle(x, y=-50, speed=self.scroll_speed)
            self.obstacles.append(new_obstacle)

        # Update existing obstacles and remove those off-screen
        for obs in self.obstacles[:]:
            obs.update()
            if obs.y > self.screen_height + 50:
                self.obstacles.remove(obs)