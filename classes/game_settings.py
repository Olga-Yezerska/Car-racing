import pygame
import os
import random

class GameSettings:
    """
    Клас для керування налаштуваннями гри, ресурсами та звуковим супроводом.
    Використовує фабричні методи для створення об'єктів гравця та дороги.
    """
    def __init__(self):
        """
        Ініціалізація списків доступних ресурсів та початкових параметрів.
        """
        # --- Списки доступних скінів та трас (Назва, Шлях до файлу) ---
        self.available_cars = [
            ("Alpine",      "assets/Car/alpine.png"),
            ("Aston Martin","assets/Car/aston.png"),
            ("Audi",        "assets/Car/audi.png"),
            ("Ferrari",     "assets/Car/ferrari.png"),
            ("Haas",        "assets/Car/haas.png"),
            ("McLaren",     "assets/Car/mclaren.png"),
            ("Mercedes",    "assets/Car/mercedes.png"),
            ("Red Bull",    "assets/Car/red_bull.png"),
            ("VCARB",       "assets/Car/vcarb.png"),
            ("Williams",    "assets/Car/williams.png"),
        ]

        self.available_roads = [
            ("Monaco",     "assets/Road/monaco_track.jpg"),
            ("Baku",       "assets/Road/baku_track.png"),
            ("Singapore",  "assets/Road/singapore_track.jpg"),
            ("Spa",        "assets/Road/spa_track.png"),
            ("Las Vegas",  "assets/Road/vegas_track.jpg"),
        ]

        # Індекси поточного вибору користувача
        self.car_index = 0
        self.road_index = 0

        # --- Музична система ---
        self.music_folder = "assets/Music"
        self.music_library = self.load_music() # Автоматичне сканування папки
        self.music_index = 0
        self.sound_volume = 0.5
        self.music_was_selected = False # Прапорець, чи вибрав користувач трек вручну

        # --- Конфігурація фонів меню ---
        self.menu_backgrounds = {
            "main": "assets/Backgrounds/main_menu.jpg",
            "settings": "assets/Backgrounds/settings_menu.jpg"
        }

    # -------- Завантаження списку музики --------
    def load_music(self) -> list:
        """
        Сканує папку з музикою та повертає список шляхів до MP3 файлів.
        
        :return: список рядків (шляхів до файлів)
        """
        if not os.path.exists(self.music_folder):
            print(f"Попередження: Папку {self.music_folder} не знайдено.")
            return []
            
        return [
            os.path.join(self.music_folder, file)
            for file in os.listdir(self.music_folder)
            if file.endswith(".mp3")
        ]

    # -------- Фабричні методи (Factory Methods) --------
    def create_car(self):
        """
        Створює та повертає об'єкт PlayerCar з вибраним скіном.
        Імпорт виконується всередині методу, щоб уникнути циклічних імпортів.
        """
        from classes.player_car import PlayerCar
        car_path = self.available_cars[self.car_index][1]
        return PlayerCar(car_path)
    
    def create_road(self):
        """
        Створює та повертає об'єкт Road з вибраною текстурою траси.
        """
        from classes.road import Road
        road_path = self.available_roads[self.road_index][1]
        return Road(road_path)
     
    # -------- Керування відтворенням --------
    def apply_music(self):
        """Завантажує та запускає відтворення поточного вибраного треку."""
        if not self.music_library:
            return
            
        pygame.mixer.music.load(self.music_library[self.music_index])
        pygame.mixer.music.set_volume(self.sound_volume)
        pygame.mixer.music.play(-1) # -1 означає нескінченний повтор

    def play_random_music(self):
        """Грає випадковий трек, якщо користувач не вибрав конкретний у меню."""
        if not self.music_was_selected and self.music_library:
            self.music_index = random.randint(0, len(self.music_library) - 1)
        self.apply_music()

    # -------- Інформаційні методи --------
    def get_settings(self):
        """Повертає словник з поточними вибраними налаштуваннями."""
        return {
            "car": self.available_cars[self.car_index],
            "road": self.available_roads[self.road_index],
            "music": self.music_library[self.music_index] if self.music_library else None,
            "volume": self.sound_volume
        }

    def get_music_name(self):
        """Повертає назву файлу поточної музики без розширення."""
        if not self.music_library:
            return "No Music"
        filename = self.music_library[self.music_index]
        return os.path.splitext(os.path.basename(filename))[0]