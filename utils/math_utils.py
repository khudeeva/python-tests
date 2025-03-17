from math import prod
import math

def multiply (a, b):
    return a * b

def greet(name="Гость"):
    return(f"Добро пожаловать, {name}!")

# произвольное количество аргументов  
def multiply_all(*args):
    return prod(args)

# ключевые аргументы
def user_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

# передача функции как аргумента + лябда-функции
def apply_operation(func, a, b):
    return func(a,b)

# применение нескольких операций
def apply_multiple_operations(operations, a, b):
    return [func(a,b) for func in operations] # проходим по списку Ф и применяем каждую

# фильтрация чисел
def filter_numbers(numbers, condition):
    return[num for num in numbers if condition(num)]

# сортируем список с кастомным ключом
def sort_by_key(data, key_func):
    return sorted(data, key=key_func) # используем key_func для сортировки

# фильтрация строк по длине и наличию букв (lambda)
def filtered_words(words, condition):
    return[word for word in words if condition(word)]

# применение нескольких математических опрераций
def apply_operations(operations, a, b):
    return[func(a,b) for func in operations]

# Сортируем слова по последней букве
def sort_by_last_letter(words):
    return sorted(words, key=lambda word: word[-1]) #сортируем по последнему символу слова

# Ищем самое длинное слово в списке
def longest_word(words):
    return max(words, key=len) # слово с мах длиной

# фильтруем слова по начальной букве
def filter_by_first_letter(words, letter):
    return[word for word in words if word.startswith(letter)]

# сумма квадратов чисел
def sum_of_squares(numbers):
    return sum(x ** 2 for x in numbers) 

# проверка палиндрома
def is_palindrome(word):
    word = word.lower().replace(" ", "") # делаем буквы маленькими, удаляем пробелы между ними
    return word == word[::-1] # сравниваем слово с его перевернутой версией

# подсчет количества гласных в строке
def count_vowels(text):
    text = text.lower() # переводим текст в нижний регистр
    vowels = "аеёиоуыэюя"
    return sum(1 for letter in text if letter in vowels) # подсчитываем количество гласных

# ищем среднее арифметическое
def average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

# ищем самое короткое слово
def shortest_word(words):
    return min(words, key=len)

# ищем слово с длиной ближе к среднему значению
def closest_to_average(words):
    avg_length = sum(len(word) for word in words) / len(words)
    return min(words, key=lambda word: abs(len(word) - avg_length))

# удвоение числа
def double(x):
    return (x * 2)

# параметр по умолчанию
def power(x, y=2):
    return(x ** y)

# суммируем все числа с *args
def sum_all(*args):
    result = 0
    for num in args:
        result = result + num
    return result

# именнованные аргументы **kwargs
def car_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

car_info(brand="Toyota", year=2022, color="blue")

# объединяем * args, **kwargs
def person_details(name, *hobbies, **info):
    print(f"{name}")
    print(f"hobbies:", hobbies)
    print("Доплнительные параметры:")
    for key,value in info.items():
        print(f"{key} : {value}")

person_details("Ksenia", "Reading", "Travelling", age=25, city="Perm")

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

# находим медиану - центральное число в отсортированном списке
def find_median(*numbers):
    numbers = sorted(numbers) # сортируем список
    n = len(numbers) # считаем количество чисел
    middle = n // 2 # находим индекс середины
    if n % 2 == 1: # если нечетное число - возвращаем средний элемент
        return numbers[middle]
    else: # если четное - берем среднее 2х центральных чисел
        return(numbers[middle -1] + numbers[middle]) / 2


print(find_median(10, 20, 30, 40, 50))
print(find_median(1, 3, 5, 7))
print(find_median(2, 8, 10, 12, 14))
print(find_median(4, 6, 8, 10))

# ищем сумму всех четных чисел
def sum_even_all(numbers):
    return sum(x for x in numbers if x % 2 == 0)

# ищем произведение всех нечетных чисел:
def multiply_odd_all(numbers):
    return prod(x for x in numbers if x % 2 == 1)

# ищем максимальную разницу между числами
def max_difference(numbers):
    maximum = max(numbers)
    minimum = min(numbers)
    return max(numbers) - min(numbers)

# ищем среднее арифметическое
def average_arifmetic(numbers):
    return sum(numbers) / len(numbers)

# ищем среднеквадратичное отклонение чисел
def average_square(numbers):
    average = sum(numbers) / len(numbers) # ищем среднее арифметическое
    squared_differences = [(x - average) ** 2 for x in numbers] #квадрат разницы каждого числа
    variance = sum(squared_differences) / len(numbers) # среднее этих квадратов
    return math.sqrt(variance) # извлекаем корень 

# фильтрация строк по количеству гласных
def filter_by_vowels_count(words, min_vowels):
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    return [word for word in words if sum(1 for letter in word if letter in vowels) >=min_vowels]

# удаление дубликатов в списке
def remove_duplicates(lst):
    unique_items = []
    for item in lst:
        if item not in unique_items:
            unique_items.append(item)
    return unique_items

# удаление из списка элементов, которые встречаются больше 1 раза
def remove_repeated(lst):
    return [ item for item in lst if lst.count(item) == 1]

# фильтрация строк, содержащихся гласные буквы
def filter_vowel_words(words):
    vowels = "аеёиоуыэюя"
    return [word for word in words if any( letter in vowels for letter in word)] 