from classes.interfaces import IUpdatable
from classes.score import Score


class ScoreManager(IUpdatable):
    """
    Клас управління балами
    """
    def __init__(self, score: Score, multiplier: float = 1.0):
        """
        Ініціалізація менеджера по управлінню балами

        :param score: бали
        :type score: Score
        :param multiplier: множник ітерацій
        :type multiplier: float
        """
        self.score = score
        self.multiplier = multiplier
        self.cycles = 0

    def cycle_complete(self) -> None:
        """
        Функція оновлення балів при закінченні одного циклу
        """
        points = int(1 * self.multiplier)
        self.score.increment(points)
        self.cycles += 1

    def update(self) -> None:
        """
        Функція оновлення
        *для майбутнього розширення
        """
        pass

    def reset(self) -> None:
        """
        Функція обнулення балів
        """
        self.score.reset()
        self.cycles = 0

    def get_score(self) -> int:
        """
        Метод отримання поточних балів

        :return: функція з класу балів
        :rtype: int
        """
        return self.score.get_score()
