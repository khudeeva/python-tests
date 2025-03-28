# все функциоанльные функции с *args, **kwargs, фильтрацией по типам
from math import prod
# 🌟Работа с *args(сумма, произведение, статистика)
# произвольное количество аргументов  
def multiply_all(*args):
    return prod(args)
# суммируем все числа с *args
def sum_all(*args):
    result = 0
    for num in args:
        result = result + num
    return result
# ищем сумму всех переданных чисел
def total_sum(*args):
    return sum(args)
# возвращаем произведение всех переданных чисел
def multiply_all(*args):
    result = 1
    for x in args:
        result *= x
    return result
# вычисляем сумму, среднее, максимум и минимум
def calculate_stats(*numbers):
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)

    print(f"Сумма: {total}")
    print(f"Среднее значение: {average}")
    print(f"Максимальное значение: {maximum}")
    print(f"Минимальное значение: {minimum}")


calculate_stats(10, 20, 30, 40, 50)


# 🌟🌟Работа с **kwargs

# ключевые аргументы
def user_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

# именнованные аргументы **kwargs
def car_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")
car_info(brand="Toyota", year=2022, color="blue")

# возвращаем только строки 
def filter_strings(**kwargs):
    new_dict = {} #создаем словарь
    for key, value in kwargs.items(): # обращаемся к словам и значениям
        if isinstance(value, str):
            new_dict[key] = value
    return new_dict

# возвращаем только числовые параметры
def filter_numbers_kwargs(**kwargs):
    new_dict = {}
    for key, value in kwargs.items():
        if isinstance(value,(int, float)) and not isinstance(value, bool):
            new_dict[key] = value
    return new_dict

# считаем количество строк
def count_strings(**kwargs):
    count = 0
    for key, value in kwargs.items():
        if isinstance(value, str):
            count +=1
    return count

# Ищем ключи, значения которых булевые (True\False)
def find_booleans(**kwargs):
    booleans = []
    for key, value in kwargs.items():
        if isinstance (value, bool):
            booleans.append(key)
    return booleans

# считаем количество булевых значений
def count_booleans(**kwargs):
    count = 0
    for key, value in kwargs.items():
        if isinstance(value, bool):
            count += 1
    return count 

#🔗 Смешанное использование *args и **kwargs
# суммируем *args, а из **kwargs берем только строки
def summarize_and_collect_strings(*args, **kwargs):
    strings = [] # создаем список для kwargs
    for key, value in kwargs.items():
        if isinstance(value, str):
            strings.append(value) # добавляем строки в список
    return sum(args), strings

# объединяем * args, **kwargs
def person_details(name, *hobbies, **info):
    print(f"{name}")
    print(f"hobbies:", hobbies)
    print("Доплнительные параметры:")
    for key,value in info.items():
        print(f"{key} : {value}")

person_details("Ksenia", "Reading", "Travelling", age=25, city="Perm")
