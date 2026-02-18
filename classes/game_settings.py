import pygame

class GameSettings:
    def __init__(self):
        # --- Скіни ---
        self.available_cars = ["car_red.png", "car_blue.png"]
        self.available_roads = ["road_1.png", "road_2.png"]

        self.car_index = 0
        self.road_index = 0

        # --- Музика ---
        self.music_library = ["song1.mp3", "song2.mp3"]
        self.music_index = 0
        self.sound_volume = 0.5

    # -------- Factory methods --------
    def create_car(self):
        from classes.player_car import PlayerCar
        return PlayerCar(self.available_cars[self.car_index])

    def create_road(self):
        from classes.road import Road
        return Road(self.available_roads[self.road_index])
     
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
    
    
