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
    
    def run(self):
        while self.running:

            events = pygame.event.get()
            input_data = self.input_handler.handle_input(events)

            # вихід
            if input_data.get("quit"):
                return "menu"

            # пауза
            if input_data.get("pause_toggle"):
                return "pause"

            self.update()
            self.render()
            self.clock.tick(60)

        return "menu"

    
    def handle_input(self):
        """
        Викликає InputHandler для обробки клавіш.
        Обробляє паузу та вихід з гри.
        """
        events = pygame.event.get()
        input_data = self.input_handler.handle_input(events)

        # Вихід із гри
        if input_data.get('quit'):
            self.running = False

        # Пауза
        if input_data.get('pause_toggle'):
            self.paused = not self.paused

    def update(self):
        # Оновлюємо гравця та дорогу
        self.player.update()
        self.road.update()
        #self.obstacle_manager.update()
        #self.check_collisions()

    def render(self):
        # Малюємо дорогу та гравця
        self.road.draw(self.screen)
        self.player.draw(self.screen)

        #for obstacle in self.obstacle_manager.obstacles:
        #    obstacle.draw(self.screen)

        pygame.display.flip()

    def check_collisions(self):
        # Тимчасово ігноруємо
        pass
