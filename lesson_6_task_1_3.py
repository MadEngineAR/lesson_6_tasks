"""2 к уроку 4 курса "Основы Python". Написать функцию currency_rates(), принимающую в качестве аргумента код валюты
(например, USD, EUR, GBP, ...)
и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests. В качестве API можно
использовать http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API в обычном
браузере, посмотреть содержимое ответа. Можно ли, используя только методы класса str, решить поставленную задачу?
Функция должна возвращать результат числового типа, например float. Подумайте: есть ли смысл для работы с денежными
величинами использовать вместо float тип Decimal? Сильно ли усложняется код функции при этом?
Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
В качестве примера выведите курсы доллара и евро.
3. * (вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату, которая передаётся
в ответе сервера. Дата должна быть в виде объекта date. Подумайте, как извлечь дату из ответа, какой тип данных лучше
использовать в ответе функции?"""

# В качестве оптимизации использования памяти использовал recordclass вместо dict. Удалил ссылку после использования.
# В результате получил снижение использования памяти от 2 до 5 раз(разные значения при запусках).
from memory_profiler import memory_usage
import datetime
from requests import get
from recordclass import recordclass


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
def currency_exchange_rate(key):
    values = []
    currencies = []
    for elem in content.split('<Value>')[1:]:
        value = elem.split('</')[0].replace(",", ".")
        values.append(value)
    for elem in content.split('<CharCode>')[1:]:
        currency = elem.split('</')[0]
        currencies.append(currency)
    values_float = list(map(float, values))
    currency_value = dict(zip(currencies, values_float))
    print(currency_value)
    currency_value.update({k.lower(): v for k, v in currency_value.items()})
    print(f'Курс {key} = {currency_value.get(key)} руб. на {date}')
    return currency_value


# Профилированное решение
@memory
def currency_exchange_rc(key):
    values = []
    currencies = []
    currency_rc = recordclass('currency', 'name value')  # использование recordclass
    for elem in content.split('<Value>')[1:]:
        value = elem.split('</')[0].replace(",", ".")
        values.append(value)
    values_float = list(map(float, values))
    for i, elem in enumerate(content.split('<CharCode>')[1:]):
        name = elem.split('</')[0]
        currency = currency_rc(name, values_float[i])
        currencies.append(currency)
        del currency                                    # Удаление ссылки
    currency_rate = [currency.value for currency in currencies if currency.name == key]
    print(f'Курс {key} = {currency_rate[0]} руб. на {date}')
    return currency_rate


response = get('http://www.cbr.ru/scripts/XML_daily.asp')
content = response.content.decode(encoding=response.encoding)
for el in content.split('<ValCurs Date="')[1:]:
    date_list = list(map(int,  (el.split('"')[0]).split('.')))
    date = datetime.date(year=date_list[2], month=date_list[1], day=date_list[0])

# currency_exchange_rate('EUR')
currency_exchange_rate('USD')
currency_exchange_rc('USD')
