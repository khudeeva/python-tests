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

# ПОВТОРЕНИЕ
def add_all(*numbers):
    return sum(numbers)

def multiply_all(*numbers):
    return prod(numbers)

def max_from_args(*numbers):
    if not numbers:
        return None
    return max(numbers)

def count_positives(*numbers):
    return sum(1 for number in numbers if number > 0)

def greet_user_kwargs(**kwargs):
    if "name" in kwargs and "age" in kwargs:
        return f"Привет, {kwargs['name']}! Тебе {kwargs['age']} лет."
    else:
        return "Недостаточно данных"
    
def describe_person(**kwargs):
    if "name" in kwargs and "age" in kwargs and "role" in kwargs:
        return f"Имя: {kwargs['name']}, Возраст: {kwargs['age']}, Роль: {kwargs['role']}"
   
def is_qa_user(**kwargs):
    if "is_qa" in kwargs and kwargs['is_qa'] == True:
        return "Пользователь - QA"
    else:
        return" Не QA"
   
def describe_user(**kwargs):
    if "name" in kwargs and "city" in kwargs and "is_active" in kwargs:
        return f"Пользователь {kwargs['name']} из {kwargs['city']}. Активен: {kwargs['is_active']}"
    else:
        return "Недостаточно информации"
    
def user_summary(name, *skills, **info):
    skill_str = ",".join(skills) if skills else "ничего"
    city = info.get("city", "неизвестно")
    experience = info.get("experience", "не указано")
    return f"Пользователь {name} знает: {skill_str}. Дополнительно: город - {city}, опыт -  {experience} года"

def summarize_person(name, *skills, **details):
    skill = ",".join(skills) if skills else "ничего"
    city = details.get("city", "неизвестно")
    age = details.get("age", "неизвестно")
    is_active = details.get("is_active", "неизвестно")
    return f"Имя: {name}. Навыки: {skill}. Детали: город - {city}, возраст - {age}, активен - {is_active}"

def profile_summary(name, *interests, **meta):
    interest = ",".join(interests) if interests else "не указано"
    country = meta.get("country", "не указано")
    verified = meta.get("verified", "не указано")
    return f"Имя: {name}. Интересы: {interest}. Детали: страна -  {country}, верифицирован - {verified}"