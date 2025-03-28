# только функции, связанные с числами(чётность, суммы, простые числа)
from math import prod
import math
# 📌Арифметика и базовые операции
# умножение
def multiply (a, b):
    return a * b

# удвоение числа
def double(x):
    return (x * 2)

# параметр по умолчанию
def power(x, y=2):
    return(x ** y)

# функция для суммы цифр числа
def sum_of_digits(num):
    return  sum(int(digit) for digit in str(num))

#  проверка четности числа
def is_even(number):
    return number % 2 == 0


# 🔁Работа с коллекциями чисел(сумма, фильтрация, анализ)
# сумма квадратов чисел
def sum_of_squares(numbers):
    return sum(x ** 2 for x in numbers) 
# ищем сумму всех четных чисел
def sum_even_all(numbers):
    return sum(x for x in numbers if x % 2 == 0)

# ищем произведение всех нечетных чисел:
def multiply_odd_all(numbers):
    return prod(x for x in numbers if x % 2 == 1)
# ищем среднее арифметическое
def average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

# ищем среднее арифметическое
def average_arifmetic(numbers):
    return sum(numbers) / len(numbers)

# ищем среднеквадратичное отклонение чисел
def average_square(numbers):
    average = sum(numbers) / len(numbers) # ищем среднее арифметическое
    squared_differences = [(x - average) ** 2 for x in numbers] #квадрат разницы каждого числа
    variance = sum(squared_differences) / len(numbers) # среднее этих квадратов
    return math.sqrt(variance) # извлекаем корень 
# ищем максимальную разницу между числами
def max_difference(numbers):
    maximum = max(numbers)
    minimum = min(numbers)
    return max(numbers) - min(numbers)
# фильтрация чисел по сумме цифр
def filter_by_digits_sum(numbers, min_sum):
    return [num for num in numbers if sum(int(digit) for digit in str(num)) > min_sum]
# фильтрация чисел
def filter_numbers(numbers, condition):
    return[num for num in numbers if condition(num)]


#  🧠Применение функций и лямбда
# передача функции как аргумента + лябда-функции
def apply_operation(func, a, b):
    return func(a,b)

# применение нескольких операций
def apply_multiple_operations(operations, a, b):
    return [func(a,b) for func in operations] # проходим по списку Ф и применяем каждую
# применение нескольких математических опрераций
def apply_operations(operations, a, b):
    return[func(a,b) for func in operations]

# 🔢Работа с сортировкой и кастомными ключами
# сортируем список с кастомным ключом
def sort_by_key(data, key_func):
    return sorted(data, key=key_func) # используем key_func для сортировки

# 🧮Статистика
# находим медиану - центральное число в отсортированном списке
def find_median(*numbers):
    numbers = sorted(numbers) # сортируем список
    n = len(numbers) # считаем количество чисел
    middle = n // 2 # находим индекс середины
    if n % 2 == 1: # если нечетное число - возвращаем средний элемент
        return numbers[middle]
    else: # если четное - берем среднее 2х центральных чисел
        return(numbers[middle -1] + numbers[middle]) / 2



#✅ Проверка (булевые функции)


# проверка, что число больше 10 и делится на 3
def is_big_and_divisible(number):
    return number > 10 and number % 3 == 0


# Разное 
def greet(name="Гость"):
    return(f"Добро пожаловать, {name}!")
