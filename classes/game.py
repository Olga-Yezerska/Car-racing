import pygame
from classes.input_handler import InputHandler
from classes.menu import Menu
# Заглушки для перешкод і колізій
# from classes.obstacle_manager import ObstacleManager
# from classes.collision_system import CollisionSystem

class Game:
    def __init__(self, screen, settings):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.settings = settings

        self.player = self.settings.create_car()
        self.road = self.settings.create_road()

        self.settings.apply_music()

        #self.obstacle_manager = ObstacleManager()
        #self.collision_system = CollisionSystem()
        # InputHandler тепер управляє гравцем
        self.input_handler = InputHandler(player=self.player, game=self)

        self.running = True
        self.paused = False
    
    