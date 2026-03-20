import pytest
import pygame
from unittest.mock import MagicMock, patch
from classes.player_car import PlayerCar
from classes.obstacle import Obstacle


# Оголошення маркерів тестів
def pytest_configure(config):
    config.addinivalue_line("markers", "collision: тести зіткнень гравця з перешкодою")
    config.addinivalue_line("markers", "obstacle: тести перешкоди (оновлення)")
    config.addinivalue_line("markers", "obstacle_delete: тести видалення перешкоди")
    config.addinivalue_line("markers", "menu: тести меню")
    config.addinivalue_line("markers", "car_move_left: тести руху гравця вліво")
    config.addinivalue_line("markers", "cycle_complete: тести проходження циклу на збільшення очків")
    config.addinivalue_line("markers", "increment_score: тести збільшення очків")
    config.addinivalue_line("markers", "reset_score: тести оновлення очків")


# Спільні фіксутри тестів
@pytest.fixture
def car():
    """
    Фікстура для ініціалізації машини гравця
    """
    # patch для щоб замінити pygame.image.load та pygame.transform.scale фіктивними об'єктами
    with patch("classes.player_car.pygame.image.load"), \
         patch("classes.player_car.pygame.transform.scale") as mock_scale:
        fake_surf = MagicMock()
        fake_surf.get_rect.return_value = pygame.Rect(365, 425, 70, 150)
        mock_scale.return_value = fake_surf
        yield PlayerCar("fake.png", x=400)


@pytest.fixture
def obstacle():
    """
    Фікстура для ініціалізації перешкоди
    """
    with patch("classes.obstacle.pygame.image.load"), \
         patch("classes.obstacle.pygame.transform.scale") as mock_scale:
        fake_surf = MagicMock()
        fake_surf.get_rect.return_value = pygame.Rect(365, 425, 70, 150)
        mock_scale.return_value = fake_surf
        yield Obstacle(x=100, y=700)
