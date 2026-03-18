import pytest
from classes.obstacle_manager import ObstacleManager

@pytest.fixture
def obstacle_manager(obstacle):
    """
    Фікстура ініціалізації менеджера перешкод
    """
    om = ObstacleManager(scroll_speed=6)
    om.obstacles = [obstacle]
    yield om

@pytest.mark.obstacle_delete
def test_obstacle_update(obstacle_manager):
    """
    Тест видалення перешкод з масиву менеджера 
    """
    obstacle_manager.update()
    assert obstacle_manager.obstacles == []