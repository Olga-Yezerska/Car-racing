class Score():
    """
    Клас балів гравця
    """
    def __init__(self, initial_score=0):
        """
        Ініціалізує об'єкт балів
        
        :param initial_score: початкове значення балів
        """
        self.score = initial_score

    def increment(self, points=1):
        """
        Функція збільшення кількості балів
        
        :param points: на скільки збільшується при ітерації
        """
        self.score += points

    def reset(self):
        """
        Функція обнулення
        """
        self.score = 0

    def get_score(self) -> int:
        """
        Функція для повернення поточної кількості балів
        
        :return: поточна кількість балів
        :rtype: int
        """
        return self.score
