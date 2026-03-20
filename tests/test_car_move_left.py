import pytest

@pytest.mark.car_move_left
def test_move_left(car):
    """
    Тест на рух машини вліво - початкова координата наближена до краю
    """
    car.x = 140
    car.move_left()
    assert car.x == 140