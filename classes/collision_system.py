import pygame
from classes.interfaces import ICollidable

class CollisionSystem:
    def __init__(self, player: ICollidable, obstacle_manager):
        """
        Initializes the collision system with the player and obstacle manager.
        
        :param player: The player's car object that implements ICollidable.
        :param obstacle_manager: The manager handling obstacles.
        """
        self.player = player
        self.obstacle_manager = obstacle_manager

    def check_collisions(self) -> bool:
        """
        Checks for collisions between the player and any obstacles.
        
        :return: True if a collision is detected, False otherwise.
        """
        for obstacle in self.obstacle_manager.obstacles:
            if self.player.get_rect().colliderect(obstacle.get_rect()):
                return True
        return False