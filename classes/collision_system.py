import pygame
from classes.interfaces import ICollidable

class CollisionSystem:
    def __init__(self, player: ICollidable, obstacle_manager):
        self.player = player
        self.obstacle_manager = obstacle_manager

    def check_collisions(self) -> bool:
        for obstacle in self.obstacle_manager.obstacles:
            if self.player.get_rect().colliderect(obstacle.get_rect()):
                return True
        return False