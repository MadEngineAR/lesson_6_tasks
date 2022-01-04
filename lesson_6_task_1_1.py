from memory_profiler import profile
from pympler import asizeof
"""
Задание 2 к уроку 5 курса "Алгоритмы Python"
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
....
"""
""" Profile показал нулевой increment, пробовал  добавить заполнение списка sum_list, mult_list 
в цикле до 10000, но это не по условию задачи, и не дало результатов. Также пробовал использовать вместо num_16_list -
num_16_tuple, что на выделение памяти не повлияло. Пришлось замерить размер объекта класса asizeof и тут результат 
налицо 512 против 304"""

# Не профилированное решение.


class Number16:
    def __init__(self, num_16):
        self.num_16 = num_16
        self.num_16_list = list(num_16)

    @profile
    def __add__(self, other):
        sum_16 = "{:x}".format(int(self.num_16, 16) + int(other.num_16, 16)).upper()
        return f'Cумма числа {self.num_16_list} и числа {other.num_16_list} равна {list(sum_16)}'

    @profile
    def __mul__(self, other):
        mult_16 = "{:x}".format(int(self.num_16, 16) * int(other.num_16, 16)).upper()
        return f'Произведение числа {self.num_16_list} и числа {other.num_16_list} равна {list(mult_16)}'

    def __str__(self):
        return f''


# Профилированное решение.
class Number16slots:
    __slots__ = ['num_16_s', 'num_16_list_s', 'sum_list_s', 'mult_list_s']

    def __init__(self, num_16_s):
        self.num_16_s = num_16_s
        self.num_16_list_s = list(num_16_s)

    @profile
    def __add__(self, other):
        sum_16_s = "{:x}".format(int(self.num_16_s, 16) + int(other.num_16_s, 16)).upper()
        return f'Cумма числа {self.num_16_list_s} и числа {other.num_16_list_s} равна {list(sum_16_s)}'

    @profile
    def __mul__(self, other):
        mult_16_s = "{:x}".format(int(self.num_16_s, 16) * int(other.num_16_s, 16)).upper()
        return f'Произведение числа {self.num_16_list_s} и числа {other.num_16_list_s} равна {list(mult_16_s)}'

    def __str__(self):
        return f''


num_1 = Number16('A2')
print(f'Объект класса Number_16 занял {asizeof.asizeof(num_1)}')
num_2 = Number16('C4F')
num_3 = Number16slots('A2')
print(f'Объект класса Number_16slots занял {asizeof.asizeof(num_3)}')
num_4 = Number16slots('C4F')
x = num_1 + num_2
y = num_3 + num_4
z = num_1 * num_2
del x, y, num_1, num_2  # Удаление ненужных ссылок(хотя dc сам бы их убрал)
s = num_3 * num_4
