from math import prod
import math
import re

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

# фильтрация слов, которые начинаются и заканчиваются на согласную букву
def filter_consonant_words(words):
    vowels = "аеёиоуыэюя"
    return [word for word in words if word[0] not in vowels and word[-1] not in vowels]

   # фильтруем слова, кторые содержат  больше/= 2 гласных 
def filter_two_vowels(words):
    vowels = "аеёиоуыэюя"
    return [word for word in words if sum(1 for letter in word if letter in vowels) >= 2]

# фильтруем слова, которые содержат четное количество букв в слове
def filter_even_length(words):
    return [word for word in words if len(word) % 2 == 0]

# фильтрация слов, где первая и последняя буквы одинаковые
def filter_same_first_last(words):
    return [word for word in words if  word[0] == word[-1]]

# фильтрация слов, которые содержат только уникальные буквы
def filter_unique_letters(words):
    return[word for word in words if len(set(word)) == len(word)]

# фильтрация слов с повторяющимися буквами
def filter_repeated_letters(words):
    return[word for word in words if len(set(word)) < len(word)]

# фильтрация чисел по сумме цифр
def filter_by_digits_sum(numbers, min_sum):
    return [num for num in numbers if sum(int(digit) for digit in str(num)) > min_sum]


# фильтрация слов по количеству уникальных букв
def filter_by_unique_letters(words, max_unique):
    return[word for word in words if len(set(word)) <= max_unique]

# функция для суммы цифр числа
def sum_of_digits(num):
    return  sum(int(digit) for digit in str(num))

# подсчет количества слов в строке
def count_words(text):
    if not isinstance(text, str):
        return "Ошибка: не строка"
    words = text.split()
    return len(words)

# ищем самое длинное слово в строке
def longest_word(text):
    if not isinstance(text, str):
        return "Ошибка: не строка"
    words = text.split()
    return max(words, key=len)

# проверка на палиндром
def is_palindrome(word):
    if not isinstance(word, str):
        return "Ошибка: не строка"
    clean_word = word.lower().replace(" ", "")
    return clean_word == clean_word[::-1]

# ищем самое короткое слово в тексте
def shortest_word(text):
    if not isinstance(text, str):
        return "Ошибка: не строка"
    words = text.split()
    return min(words, key=len)

# ищем слово с максимальным количеством гласных
def most_vowels_word(text):
    if not isinstance(text, str):
        return "Ошибка: не строка"
    
    vowels = "аеёиоуыэюя"
    words = text.split()

    return max(words, key=lambda word: sum(1 for letter in word if letter in vowels))

# замена букв в тексте
def replace_letters(text, old, new):
    if not isinstance(text, str):
        return "Ошибка: не строка"
    return text.replace(old, new)

# считаем количество букв  в каждом слове
def word_lengths(text):
    if not isinstance(text, str):
        return "Ошибка: не строка"
    words = text.split()
    return [len(word) for word in words] 

# выбираем самое частое слово в тексте
def most_frequent_word(text):
    if not isinstance(text, str):
        return "Ошибка: не строка"
    words = text.split()
    return max(words, key=words.count)

# ищем самое редкое слово в тексте
def least_frequent_word(text):
    if not isinstance(text, str):
        return "Ошибка: не строка"
    words = text.split()
    return min(words, key=words.count)

# считаем количество предложений в тексте
def count_sentences(text):
    if not isinstance(text, str):
        return "Ошибка: не строка"
    sentences = re.split(r'[.!?]', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    return len(sentences)

# замена всех цифр в тексте на *
def replace_digits(text):
    if not isinstance(text, str):
        return "Ошибка: не строка"
    return re.sub(r'\d','*', text)

# делим текст по ,.!
def divided_sentences(text):
    if not isinstance(text, str):
        return "Ошибка: не строка"
    sentences = re.split(r'[,.!]', text) # разделяем текст по знакам препинания
    sentences = [s.strip() for s in sentences if s.strip()] # убираем пустые строки
    return(sentences)

# замена всех букв "а" и "о" на * в тексте
def replace_words(text):
    if not isinstance(text, str):
        return "Ошибка: не строка"
    return re.sub(r'[ао]', '*', text) # несколько букв заключи в []

# извлекаем из строки только числа
def extract_numbers(text):
    if not isinstance(text, str):
        return "Ошибка: не строка"
    return re.findall(r'\d+', text) # находим все группы цифр

# оставляем в тексте слова длиной от 4 до 6 символов
def filtered_words_len(text):
    if not isinstance(text, str):
        return "Ошибка: не строка"
    words = text.split()
    return [word for word in words if 4 <= len(word) <= 6]

# ищем слова с длиной от 4 до 6 букв
def find_words(text):
    if not isinstance(text, str):
        return "Ошибка: не строка"
    return re.findall(r'\b\w{4,6}\b', text)

# ищем все даты в формате ДД.ММ.ГГГГ
def find_dates(text):
    if not isinstance(text, str):
        return "Ошибка: не строка"
    return re.findall(r'\b\d{2}\.\d{2}\.\d{4}\b', text)

# проверяем как функция возвращает кортеж
def get_user_info(name, age, city):
    return(name, age, city)

# фильтруем уникальные числа из списка
def filter_unique(numbers):
    return list(set(numbers))

# добавляем ключ в словарь
def update_dict(user_data):
    if not isinstance(user_data, dict):
        return "Ошибка: не словарь"
    user_data["status"] = "active"
    return user_data

# ищем только уникальные слова(без повторений, в нижнем регистре)
def find_unique_words(text):
    if not isinstance(text, str):
        return "Ошибка: не строка"
    words = re.findall(r'\b\w+\b', text.lower())
    return list(set(words))

# SET
# ищем множество уникальных значений
def unique_numbers(numbers):
    unique_numbers = set(numbers)
    return(unique_numbers)

# ищем количество уникальных чисел в списке
def count_unique(numbers):
    unique = set(numbers)
    return len(unique)

# ищем только те числа, которые есть одновременно в двух списках
def common_numbers(list1, list2):
   set1 = set(list1)
   set2 = set(list2)
   return list(set1 & set2)

# ищем элементы из первого списка, которых нет во втором 
def unique_from_first(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1 - set2)

# ищем числа которе есть ТОЛЬКО в одном из двух списков
def unique_numbers_from_both(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1 ^ set2)

# ищем пересечение, если в списках есть хотя бы 1 общий элемент
def has_common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return len(set1 & set2) > 0 # return bool(set1 & set2)

# ищем подмножество
def is_subset(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1 <= set2

# проверяем не имеют ли два списка общие элементы
def is_disjoint(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return len(set1 & set2) == 0

# проверка на дубликаты
def has_duplicates(lts):
    return len(lts) != len(set(lts)) 

# подсчет уникальных посещенных страниц
def count_unique_pages(visited_pages):
    unique_pages = set(visited_pages)
    return len(unique_pages)

# ищем уникальные имена, отсортированные по алфавиту
def unique_users(users):
    unique_users = set(users)
    sorted_users = sorted(unique_users) # сортируем по алфавиту
    return sorted_users

# ищем кто не сдал работу, отсортируем по алфавиту
def who_didnt_submit(all_students, submitted):
    set1 = set(all_students)
    set2 = set(submitted)
    return sorted(list(set1 - set2))
