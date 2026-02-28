import pygame
import os
import random

class GameSettings:
    def __init__(self):
        # --- Скіни ---
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

        self.car_index = 0
        self.road_index = 0

           # --- Музика ---
        self.music_folder = "assets/Music"
        self.music_library = self.load_music()
        self.music_index = 0
        self.sound_volume = 0.5
        self.music_was_selected = False

        # --- Фони меню ---
        self.menu_backgrounds = {
        "main": "assets/Backgrounds/main_menu.jpg",
        "settings": "assets/Backgrounds/settings_menu.jpg"}


    # -------- Load music from folder --------
    def load_music(self):
        return [
            os.path.join(self.music_folder, file)
            for file in os.listdir(self.music_folder)
            if file.endswith(".mp3")
        ]

    # -------- Factory methods --------
    def create_car(self):
        from classes.player_car import PlayerCar
        car_path = self.available_cars[self.car_index][1]
        return PlayerCar(car_path)
    

    def create_road(self):
        from classes.road import Road
        road_path = self.available_roads[self.road_index][1]    # [1] — це шлях
        return Road(road_path)
     
    # -------- Music --------
    def apply_music(self):
        pygame.mixer.music.load(self.music_library[self.music_index])
        pygame.mixer.music.set_volume(self.sound_volume)
        pygame.mixer.music.play(-1)

    # -------- Settings dictionary --------
    def get_settings(self):
        return {
            "car": self.available_cars[self.car_index],
            "road": self.available_roads[self.road_index],
            "music": self.music_library[self.music_index],
            "volume": self.sound_volume
        }
    def get_music_name(self):
        filename = self.music_library[self.music_index]
        return os.path.splitext(os.path.basename(filename))[0]
    def play_random_music(self):
        if not self.music_was_selected:
            self.music_index = random.randint(0, len(self.music_library) - 1)
        self.apply_music()

