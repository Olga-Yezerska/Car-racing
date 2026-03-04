import pygame
from classes.menu import Menu
from classes.game import Game
from classes.game_settings import GameSettings
from classes.input_handler import InputHandler


class GameApp:
    """
    Головний клас додатка, який керує життєвим циклом гри, 
    станами (меню, гра, пауза) та ініціалізацією Pygame
    """
    
    def __init__(self):
        """
        Конструктор класу: ініціалізує модулі Pygame, вікно гри,
        налаштування та обробник введення
        """
        pygame.init()
        pygame.mixer.init()

        # Налаштування графічного вікна
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Car Racing")

        # Ініціалізація допоміжних систем
        self.settings = GameSettings()
        self.input_handler = InputHandler()
        self.menu = Menu(self.screen, self.settings)
        self.game = None

        # Початковий стан програми
        self.state = "menu"
        self.running = True

    def run(self):
        """
        Головний цикл програми, який обробляє події, оновлює логіку 
        залежно від стану та рендерить зображення на екран.
        """
        while self.running:
            # Отримання списку подій від Pygame
            events = pygame.event.get()
            # Попередня обробка введення (клавіші, вихід)
            input_data = self.input_handler.handle_input(events)

            # Перевірка на закриття вікна
            if input_data.get("quit"):
                self.running = False

            # Машина станів (State Machine)
            if self.state == "menu":
                self.handle_menu(input_data)

            elif self.state == "game":
                self.handle_game(input_data)

            elif self.state == "pause":
                self.handle_pause(input_data)

            elif self.state == "game_over":
                self.handle_game_over(input_data)

            # Оновлення вмісту всього екрана
            pygame.display.flip()

        # Завершення роботи Pygame після виходу з циклу
        pygame.quit()

    # ---------------- ОБРОБНИКИ СТАНІВ (STATES) ----------------

    def handle_menu(self, input_data: dict):
        """
        Обробка логіки головного меню.
        
        :param input_data: словник з даними про натиснуті клавіші
        """
        result = self.menu.handle_input(input_data)
        self.menu.draw()

        # Перехід до гри при натисканні "Start"
        if result == "start":
            self.game = Game(self.screen, self.settings)
            self.input_handler.player = self.game.player
            self.settings.play_random_music()
            self.state = "game"

        # Вихід з програми
        elif result == "quit":
            self.running = False

    def handle_game(self, input_data: dict):
        """
        Обробка ігрового процесу (активна фаза гонки).
        
        :param input_data: словник з даними про натиснуті клавіші
        """
        result = self.game.run_frame(input_data)

        # Перевірка результату кадру (пауза або поразка)
        if result == "pause":
            self.menu.mode = "pause"
            self.menu.selected_index = 0
            self.input_handler.player = None  # Зупиняємо керування гравцем
            self.state = "pause"

        elif result == "game_over":
            self.menu.mode = "game_over"
            self.menu.selected_index = 0
            self.input_handler.player = None
            self.state = "game_over"

    def handle_pause(self, input_data: dict):
        """
        Обробка стану паузи (відображення меню поверх замороженої гри).
        
        :param input_data: словник з даними про натиснуті клавіші
        """
        self.game.draw_only()  # Малюємо фон гри без оновлення логіки
        result = self.menu.handle_input(input_data)
        self.menu.draw()

        # Повернення до гри
        if result == "resume":
            self.input_handler.player = self.game.player
            self.state = "game"

        # Повернення до головного меню
        elif result == "menu":
            self.menu.mode = "main"
            self.menu.selected_index = 0
            pygame.mixer.music.stop()
            self.state = "menu"

    def handle_game_over(self, input_data: dict):
        """
        Обробка екрана завершення гри.
        
        :param input_data: словник з даними про натиснуті клавіші
        """
        self.game.draw_only()
        result = self.menu.handle_input(input_data)
        self.menu.draw()

        # Почати гонку заново
        if result == "restart":
            self.game = Game(self.screen, self.settings)
            self.input_handler.player = self.game.player
            pygame.mixer.music.stop()
            self.settings.apply_music()
            self.state = "game"

        # Повернення до головного меню
        elif result == "menu":
            self.menu.mode = "main"
            self.menu.selected_index = 0
            pygame.mixer.music.stop()
            self.state = "menu"