import pytest
from classes.score import Score
from classes.score_manager import ScoreManager


@pytest.fixture
def manager():
    """
    Фікстура для ініціалізації менеджер абалів
    """
    return ScoreManager(Score())


@pytest.mark.cycle_complete
def test_cycle_complete(manager):
    """
    Тест на проходження циклу дороги - 3 рази виклик у відповідності кількості очок за ці цикли
    """
    manager.cycle_complete()
    manager.cycle_complete()
    manager.cycle_complete()
    assert manager.get_score() == 3
