"""
Задание 1 к уроку 4 курса "Алгоритмы Python"
Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива.
Сделайте замеры времени выполнения кода с помощью модуля timeit.
Попробуйте оптимизировать код, чтобы снизить время выполнения,
проведите повторные замеры
ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""


# В данной задаче при профилировании применил array из numpy, генератор. Применение данных подходов позволило сократить
# объем выделяемой памяти в случае с array в два раза, а с генератором на порядок"""
from timeit import timeit
from memory_profiler import profile, memory_usage
from numpy import array
# Не профилированное решение


@profile
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# Вариант 2 - LC Не профилированное решение
@profile
def test_lst_comp(nums):
    return [i for i in range(0, len(nums), 2)]


# Вариант 1 Профилированное решение
@profile
def array_numpy(nums):
    new_arr = array([i for i in range(0, len(nums), 2)])
    return new_arr


# Вариант 2 Профилированное решение- Использование генератора
def memory(func):
    def wrapper(*args):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        print(f"Выполнение заняло {mem_diff} Mib")
        return res

    return wrapper


@memory
def test_gen_comp(nums):
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            yield i


nums_list = [num for num in range(50000)]
func_1(nums_list)
test_lst_comp(nums_list)
array_numpy(nums_list)
my_list = list(test_gen_comp(nums_list))


print(f'Время выполнение func_1(nums) - {timeit("func_1", globals=globals())}')
print(f'Время выполнение test_lst_comp(nums) - {timeit("test_lst_comp", globals=globals())}')
print(f'Время выполнение array_numpy(nums) - {timeit("array_numpy", globals=globals())}')
print(f'Время выполнение my_list - {timeit("my_list", globals=globals())}')
