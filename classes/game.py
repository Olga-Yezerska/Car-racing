import pygame
from classes.input_handler import InputHandler
from classes.obstacle_manager import ObstacleManager
from classes.collision_system import CollisionSystem
from classes.score import Score
from classes.score_manager import ScoreManager
from classes.score_display import ScoreDisplay

class Game:
    """
    Клас, що відповідає за основну логіку ігрового процесу (Gameplay).
    Керує оновленням стану об'єктів, обробкою зіткнень та підрахунком балів.
    """
    def __init__(self, screen, settings):
        """
        Конструктор ігрової сесії.
        
        :param screen: поверхня Pygame для малювання (pygame.Surface)
        :param settings: об'єкт з налаштуваннями гри
        """
        self.screen = screen
        self.clock = pygame.time.Clock()  # Контролер FPS
        self.settings = settings

        # Створення ігрових об'єктів через фабричні методи налаштувань
        self.player = self.settings.create_car()
        self.road = self.settings.create_road()  
        
        # Ініціалізація менеджерів систем
        self.obstacle_manager = ObstacleManager(self.road.scroll_speed)
        self.collision_system = CollisionSystem(self.player, self.obstacle_manager)
        
        # Налаштування системи нарахування балів
        self.score = Score()
        self.score_manager = ScoreManager(self.score)
        self.score_display = ScoreDisplay(self.score_manager)
        
        # Прив'язка події завершення циклу дороги до нарахування очок
        self.road.on_cycle_complete = self.score_manager.cycle_complete

        self.running = True
        self.game_over = False

    def run_frame(self, input_data: dict):
        """
        Метод обробки одного ігрового кадру (update + draw).
        
        :param input_data: словник з командами від InputHandler
        :return: рядок-ідентифікатор зміни стану гри (якщо потрібен перехід)
        """
        # Перевірка запиту на вихід у меню
        if input_data.get("quit"):
            return "menu"

        # Перевірка запиту на активацію паузи
        if input_data.get("pause_toggle"):
            return "pause"

        # --- БЛОК ОНОВЛЕННЯ ЛОГІКИ ---
        self.player.update() 
        self.road.update()
        self.obstacle_manager.update()
        self.score_manager.update()

        # Перевірка на зіткнення автомобіля з перешкодами
        if self.collision_system.check_collisions():
            self.game_over = True
            return "game_over"

        # --- БЛОК ВІЗУАЛІЗАЦІЇ ---
        self.draw_only() 

        # Обмеження частоти кадрів (60 FPS)
        self.clock.tick(60)
        return None

    def draw_only(self):
        """
        Метод для рендерингу всіх ігрових елементів на екран.
        Використовується окремо, коли гра на паузі або закінчена.
        """
        # 1. Малюємо дорогу (задній план)
        self.road.draw(self.screen)
        
        # 2. Малюємо гравця
        self.player.draw(self.screen)
        
        # 3. Малюємо всі активні перешкоди
        for obs in self.obstacle_manager.obstacles:
            obs.draw(self.screen)
            
        # 4. Малюємо інтерфейс користувача (рахунок) поверх усього
        self.score_display.draw(self.screen)