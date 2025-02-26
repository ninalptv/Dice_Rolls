from random import randint

class Die():
    """Класс, представляющий один кубик."""

    def __init__(self, num_sides=6):
        """Инициализация. По умолчанию шестигранный кубик"""
        self.num_sides = num_sides

    def roll(self):
        """Возвращает случайное число от1 до числа граней."""
        return randint(1, self.num_sides)