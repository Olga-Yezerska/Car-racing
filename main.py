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

while running:

    if state == "menu":
        menu = Menu(screen, settings)
        result = menu.run(input_handler)

        if result == "start":
            state = "game"

        elif result == "quit":
            running = False

    elif state == "game":
        game = Game(screen, settings)
        result = game.run()
        state = result
    

pygame.quit()
