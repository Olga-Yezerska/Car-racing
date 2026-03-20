import pytest
from classes.score import Score


@pytest.fixture
def score():
    """
    Фікстура для ініціалізації Score
    """
    return Score()


@pytest.mark.increment_score
def test_increment(score):
    """
    Тест на збільшення очок
    """
    score.increment(5)
    assert score.get_score() == 5


@pytest.mark.parametrize("points, expected", [
    (1, 1),
    (5, 5),
    (100, 100),
])  # параметризація для того ж тесту
@pytest.mark.increment_score
def test_increment_parametrized(score, points, expected):
    """
    Тест на збільшення очок з параметрами
    """
    score.increment(points)
    assert score.get_score() == expected


@pytest.mark.reset_score
def test_reset(score):
    """
    Тест на скидання очок - додавання 5 і скидання до нуля
    """
    score.increment(10)
    score.reset()
    assert score.get_score() == 0


@pytest.mark.parametrize("initial", [1, 5, 50, 999])  # параметризація початкової кілкьості очок для тесту скидання
@pytest.mark.reset_score
def test_reset_parametrized(initial):
    """
    Тест на скидання очок - ініціалізація з параметру і скидання до нуля
    """
    s = Score(initial_score=initial)
    s.reset()
    assert s.get_score() == 0
