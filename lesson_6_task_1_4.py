"""4 к уроку 5 курса "Основы Python". Представлен список чисел. Необходимо вывести те его элементы, значения которых
больше предыдущего, например:
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [12, 44, 4, 10, 78, 123]"""

# В качестве оптимизации использования памяти использовал генератор вместо LC.
# В результате получил снижение использования памяти на 2 порядка.
from memory_profiler import memory_usage
from random import randint


def memory(func):
    def wrapper(*args):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        print(f"Выполнение заняло {mem_diff} Mib")
        return res

    return wrapper


# Не профилированное решение
@memory
def sort_list(lst):
    result = [num for n, num in enumerate(scr) if num > scr[n - 1] and n != 0]
    return result


# Профилированное решение
@memory
def sort_list_gen(lst):
    for n, num in enumerate(scr):
        if num > scr[n-1] and n != 0:
            yield num


# scr = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]   # ВАРИАНТ 2
scr = [randint(0, 100) for _ in range(100000)]
sort_list(scr)
scr_opt = list(sort_list_gen(scr))
