import pytest
#  проверка четности числа
def is_even(number):
    return number % 2 == 0

# проверка, является ли число простым
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# возвращаем список только четных чисел
def filter_even(numbers):
    return [x for x in numbers if x % 2 == 0]

# возвращаем сумму всез четных чисел из списка
def sum_even(numbers):
    return sum(x for x in numbers if x % 2 == 0)


# возвращаем список, где каждое число возведено в квадрат
def square_all(numbers):
    return [x ** 2 for x in numbers]

# проверка на делимость на 5
def is_divisible_by_5(n):
    return n % 5 == 0

# возврат остатка от деления
def remainder(a, b):
    return a % b

# проверка кратности числа
def is_multiple_of(a, b): 
    if a % b == 0:
        return  True  # либо return a % b == 0
    else:
        return False

# проверяем находится ли число между low, high
def is_between(n, low, high):
    return low < n <  high

# проверяем четность числа + больше 10
def is_even_and_gt_10(n):
    return n % 2 == 0 and n > 10

# делим a/b, если b=0 - возвращаем ошибку, если после деления целое число - Int, иначе float
def safe_divide(a, b):
    if b == 0:
        return "Деление на ноль невозможно"
    else:
        result = a / b
        if result.is_integer():
                return int(result)
        else:
                return result
# вернуть строку четное или нечетное (+ тернарный оператор)
def check_even_or_odd(n):
    return "Чётное" if n % 2 == 0 else "Нечётное"

# если целое число - округляем его, иначе возвращаем int
def round_if_not_integer(n):
    return int(round(n)) if n.is_integer() else int(n)

# обрабатываем 2 числа и возвращаем строку
def check_even_odd_pair(a, b):
     if a % 2 == 0 and b % 2 == 0:
        return "Оба чётные"
     elif a % 2 == 1 and b % 2 == 1:
        return "Оба нечётные"
     else: 
        return "Разные" 

# ПАРАМЕТРИЗАЦИЯ ТЕСТОВ
# четное нечетное число
def even_or_odd(n):
    return "Чётное" if n % 2 == 0 else "Нечётное"

# определяем категорию температуры
def temperature_status(temp):
    if temp < 10:
        return "Холодно"
    elif 10 <= temp <= 25:
        return "Тепло"
    else:
        return "Жарко"

# определяем категорию по баллам
def grade_category(score):
    if  90 <= score <= 100:
        return "Отлично"
    elif 75 <= score <=  89:
        return "Хорошо"
    elif 60 <= score <= 74:
        return "Удовлетворительно"
    else:
        return "Неудовлетворительно"

# проверка длины пароля
def password_strength(password):
    if len(password) < 6:
        return "Слабый"
    elif 6 <= len(password) <= 10:
        return "Средний"
    else:
        return "Сильный"

# ФИКСТУРА
# фикстура для списка чисел
@pytest.fixture
def number_list():
    return [1, 2, 3, 4, 5, 6]

# фикстура для строк
@pytest.fixture
def word_list():
    return {"яблоко", "банан", "киви", "ананас"}

# фикструа словарь с пользователями
@pytest.fixture
def users():
    return {
        "Анна": {"age": 25, "active": True},
        "Иван": {"age": 30, "active": False},
        "Мария": {"age": 22, "active": True}
    }
# фикстура настройки пользователя
@pytest.fixture
def user_settings():
    return {
        "theme" : "dark",
        "notifications": True,
        "language": "ru"
    }

# фикстура числовой набор
@pytest.fixture
def number_data():
    return [12, 45, 33, 8, 21, 60]

# фикстура 2 числа
@pytest.fixture
def numbers():
    return (6, 3)

# ПОВТОРЕНИЕ
# проверка чётности числа
def is_even_practice(number):
   return number % 2 == 0

# проверка деления a/b без остатка
def is_divisible_practice(a, b):
    if b == 0:
        return False
    return a % b == 0
    
# ищем большее из 2-х чисел
def get_max(a, b):
    return max(a, b)

# ищем всю сумму чисел в списке
def sum_list(numbers):
    if not numbers:
        return 0
    return sum(numbers)

# ищем среднее значение чисел в списке
def average_practice(numbers):
    if not numbers:
        return 0
    return sum(numbers)/len(numbers)

# возвращаем произведение всех чисел в списке
def multiply_list_practice(numbers):
    result = 1
    for x in numbers:
        result *=x
    return result
    
# возвращаем кортеж из минимального и максимального значения списка
def find_min_max(numbers):
    if not numbers:
        return None
    return (min(numbers), max(numbers))

# ПОВТОРЕНИЕ
def divide(a, b):
    return a / b

def square(n):
    return n * n

def add(a, b):
    return a + b



def compare_number(a, b):
    if a > b:
        return "greater"
    elif a < b:
        return "less"
    else:
        return "equal"

def divide_with_raise(a, b):
    if b == 0:
        raise ValueError("Деление на ноль запрещено")
    return a / b

# Проверка исключений (with pytest.raises)
def safe_int(value):
    return int(value)
    
def safe_divide_zero(a, b):
    if b == 0:
        raise ZeroDivisionError("Деление на ноль запрещено")
    return a / b

def parse_int_list(lst):
    result = []
    for x in lst:
        try:
            result.append(int(x))
        except ValueError:
            raise ValueError("Невозможно преобразовать список в числа")
    return result

    
def divide_raise(a, b):
    return a/b
    
def double(x):
    return x ** 2

def is_even_example(num):
    return num % 2 == 0

def is_even_save(num):
    if not isinstance(num, int):
        raise TypeError("Input must be an integer")
    return num % 2 == 0

def divide_with_error(a, b):
    if b ==0:
        raise ZeroDivisionError("Деление на ноль невозможно")
    return a / b

def safe_divide_with_raise(a, b):
    if b == 0:
        raise ZeroDivisionError("Деление на 0 невозможно")
    if a < 0 or b < 0:
        raise ValueError("Числа должны быть положительными")
    return a / b

def is_prime_example(n):
    if n <=1:
        return False
    for i in range(2, int(n **0.5)+1):
        if n % i == 0:
            return False
    return True

def number_is_even(n):
    return n % 2 == 0