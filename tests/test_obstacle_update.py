import pytest

@pytest.mark.obstacle
def test_obstacle_update(obstacle):
    """
    Тест оновлення позиції перешкоди на екрані
    """
    obstacle.update()
    assert obstacle.y == 706