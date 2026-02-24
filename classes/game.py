import pygame
from classes.input_handler import InputHandler
from classes.obstacle_manager import ObstacleManager
from classes.collision_system import CollisionSystem
from classes.score import Score
from classes.score_manager import ScoreManager
from classes.score_display import ScoreDisplay

class Game:
    def __init__(self, screen, settings):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.settings = settings

        self.player = self.settings.create_car()
        self.road = self.settings.create_road()  
        self.obstacle_manager = ObstacleManager(self.road.scroll_speed)
        self.collision_system = CollisionSystem(self.player, self.obstacle_manager)
        # Бали
        self.score = Score()
        self.score_manager = ScoreManager(self.score)
        self.score_display = ScoreDisplay(self.score_manager)
        self.road.on_cycle_complete = self.score_manager.cycle_complete

        self.running = True
        self.game_over = False

    def run_frame(self, input_data):
        # Вихід
        if input_data.get("quit"):
            return "menu"

        # Пауза
        if input_data.get("pause_toggle"):
            return "pause"

        # Оновлення
        self.player.update() 
        self.road.update()
        self.obstacle_manager.update()
        self.score_manager.update()

        if self.collision_system.check_collisions():
            self.game_over = True
            return "game_over"

        # Малювання кадру гри
        self.draw_only() 

        self.clock.tick(60)
        return None

    def draw_only(self):
        """Метод для малювання кадру гри без оновлення логіки"""
        self.road.draw(self.screen)
        self.player.draw(self.screen)
        for obs in self.obstacle_manager.obstacles:
            obs.draw(self.screen)
        self.score_display.draw(self.screen)