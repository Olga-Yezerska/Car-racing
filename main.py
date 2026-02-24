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

state = "menu"
running = True
game = None      # ← зберігаємо гру
menu = Menu(screen, settings)

while running:

    if state == "menu":
        menu.mode = "main"
        menu.selected_index = 0
        result = menu.run(input_handler)

        if result == "start":
            game = Game(screen, settings)
            state = "game"

        elif result == "quit":
            running = False

    elif state == "game":
        result = game.run()

        if result == "pause":
            menu.mode = "pause"
            menu.selected_index = 0
            state = "pause"

        elif result == "game_over":
            menu.mode = "game_over"
            menu.selected_index = 0
            state = "menu"

    elif state == "pause":
        result = menu.run(input_handler)

        if result == "resume":
            state = "game"

        elif result == "menu":
            state = "menu"

pygame.quit()