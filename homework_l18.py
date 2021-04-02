"""
Создать класс Дробное число со знаком (Fractions). Число должно быть представлено
двумя полями: целая часть - длинное целое со знаком, дробная часть - беззнаковое
короткое целое. Реализовать арифметические операции сложения, вычитания, умножения
и операции сравнения.
"""


class FractionNum:
    # внес в конструктор степень дробной части (нет в задании)
    # (для задания дробных частей с нулями перед значимыми цифрами)
    def __init__(self, decimal, fraction, power_of_fraction):
        self._decimal = decimal
        self._fraction = fraction
        self._power_of_fraction = power_of_fraction

    # преобразую раздельные части числа в число с плавающей запятой
    def _return_float(self):
        if self._decimal >= 0:
            return self._decimal + self._fraction * 10 ** self._power_of_fraction
        else:
            return self._decimal - self._fraction * 10 ** self._power_of_fraction

    # Реализую операции сложения, вычитания, умножения и операции сравнения
    def __add__(self, other):
        return self._return_float() + other._return_float()

    def __sub__(self, other):
        return self._return_float() - other._return_float()

    def __mul__(self, other):
        return self._return_float() * other._return_float()

    def __gt__(self, other):
        return self._return_float() > other._return_float()

    def __eq__(self, other):
        return self._return_float() == other._return_float()

    def __ge__(self, other):
        return self._return_float() >= other._return_float()

    def __str__(self):
        return str(self._return_float())


def main():
    fr_num_1 = FractionNum(-89, 1, -2)
    fr_num_2 = FractionNum(-9, 17, -3)
    print(f'Число 1: {fr_num_1}')
    print(f'Число 2: {fr_num_2}')
    print(f'Сумма чисел: {fr_num_1 + fr_num_2}')
    # Почему в данном случае разница дает 1 в -14 разряде?
    print(f'Разница чисел: {fr_num_1 - fr_num_2}')
    print(f'Произведение чисел: {fr_num_1 * fr_num_2}')
    print(f'Число 1 больше числа 2: {fr_num_1 > fr_num_2}')
    print(f'Число 1 равно числу 2: {fr_num_1 == fr_num_2}')
    print(f'Число 1 меньше или равно числу 2: {fr_num_1 <= fr_num_2}')


if __name__ == '__main__':
    main()
