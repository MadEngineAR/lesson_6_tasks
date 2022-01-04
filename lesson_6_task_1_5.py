"""5 к уроку 5 курса "Основы Python". Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]"""

# В качестве оптимизации использования памяти использовал counter и генератор вместо LC.
# В результате получил снижение использования памяти на 1 порядок.
from memory_profiler import memory_usage
from collections import Counter
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
    unique_nums = set()
    repeated_num = set()
    for num in src:  # O(n)
        if num in repeated_num:  # O(1)
            continue
        if num in unique_nums:  # O(1)
            repeated_num.add(num)  # O(1)
            unique_nums.discard(num)  # O(1)
            continue
        unique_nums.add(num)  # O(1)
    unique_nums_list = [num for num in src if num in unique_nums]
    print(unique_nums_list)
    return unique_nums_list


# Профилированное решение
@memory
def sort_list_count_gen(lst):
    nums_count = Counter(lst)
    for k in nums_count:
        if nums_count.get(k) < 2:
            yield k


src = [randint(0, 100) for _ in range(500)]
sort_list(src)
print(list(sort_list_count_gen(src)))
