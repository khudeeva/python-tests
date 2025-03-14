from math import prod

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
