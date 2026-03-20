import pytest
import pygame
from unittest.mock import MagicMock
from classes.menu import Menu


@pytest.fixture
def menu():
    """
    Фікстура для ініціалізації Меню
    """
    pygame.init()  # для ініціалізації шрифтів всередині меню
    screen = MagicMock()
    settings = MagicMock()
    menu = Menu(screen, settings)
    yield menu
    pygame.quit()


@pytest.mark.menu
def test_menu_navigate_down(menu):
    """
    Тест перевірки навігації з клавіатури - натиснення клавіші "вниз" спускає логіку на індекс 1
    """
    input_data = {"quit": False,
                  "enter": False,
                  "escape": False,
                  "up": False,
                  "down": True,
                  "left": False,
                  "right": False,
                  "pause_toggle": False}  # словник значень

    menu.handle_input(input_data)
    assert menu.selected_index == 1
