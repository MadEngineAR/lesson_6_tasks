"""
Задание 2.
Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.
Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.
Опишите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение.
"""
# Проблема замеров в том, что при каждом рекурсивном вызове функции profile делает отдельный замер объема выделяемой
# памяти. Ее можно решить, профилируя функцию total, которая возвращает результат nums_reverse. Таким образом, profile
# сделает один замер выделяемой памяти на работу nums_reverse.
from memory_profiler import profile


@profile
def total(func):
    return nums_reverse


def nums_reverse(num):
    if num < 10:
        return f'{num}'
    elif num % 10 == 0 and num > 10 ** (len(str(n))-1):
        digit = num % 10
        num = num // 10
        return nums_reverse(num) + str(digit)
    else:
        digit = num % 10
        num = num // 10
        return str(digit) + nums_reverse(num)


try:
    print(f'Введите число')
    n = int(input())
except ValueError:
    print(f'Введите число')
    n = int(input())

print(f'Перевернутое {n}  - {total(nums_reverse(n))}')
