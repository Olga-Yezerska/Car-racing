from classes.collision_system import CollisionSystem
import pytest
from unittest.mock import MagicMock

@pytest.fixture
def obstacle_manager(obstacle):
    """
    фікстура для ініціалізації менеджера перешкод 
    """
    obstacle_manager = MagicMock()
    obstacle_manager.obstacles = [obstacle] #у масив перешкод передається одна з фікстур 
    yield obstacle_manager

@pytest.mark.collision
def test_collision(car, obstacle_manager):
    """
    Тест перевірки зіткнення гравця з перешкодою
    """
    collision_system = CollisionSystem(car, obstacle_manager)
    assert collision_system.check_collisions() == True