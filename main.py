import pygame
from classes.menu import Menu
from classes.game import Game
from classes.game_settings import GameSettings
from classes.input_handler import InputHandler

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Car Racing")

settings = GameSettings()

input_handler = InputHandler()

menu = Menu(screen, settings)
game = None

state = "menu"
running = True

while running:
    events = pygame.event.get()
    input_data = input_handler.handle_input(events)

    # Завжди можна закрити
    if input_data.get("quit"):
        running = False

    # ---------------- MAIN MENU ----------------
    if state == "menu":
        result = menu.handle_input(input_data)
        menu.draw()

        if result == "start":
            game = Game(screen, settings)
            input_handler.player = game.player
            settings.play_random_music()

            state = "game"

        elif result == "quit":
            running = False

    # ---------------- GAME ----------------
    elif state == "game":
        result = game.run_frame(input_data)

        if result == "pause":
            menu.mode = "pause"
            menu.selected_index = 0
            input_handler.player = None
            state = "pause"


        elif result == "game_over":
            menu.mode = "game_over"
            menu.selected_index = 0
            input_handler.player = None
            state = "game_over"

    # ---------------- PAUSE ----------------
    elif state == "pause":
        game.draw_only()  # малюємо гру під оверлеєм
        result = menu.handle_input(input_data)
        menu.draw()

        if result == "resume":
            input_handler.player = game.player
            state = "game"

        elif result == "menu":
            menu.mode = "main"
            menu.selected_index = 0
            state = "menu"
            pygame.mixer.music.stop()

    # ---------------- GAME OVER ----------------
    elif state == "game_over":
        game.draw_only()
        result = menu.handle_input(input_data)
        menu.draw()

        if result == "restart":
            game = Game(screen, settings)
            input_handler.player = game.player
            pygame.mixer.music.stop()
            settings.apply_music()
            #input_handler.player = None
            state = "game"

        elif result == "menu":
            menu.mode = "main"
            menu.selected_index = 0
            state = "menu"
            pygame.mixer.music.stop()

    pygame.display.flip()

pygame.quit()
