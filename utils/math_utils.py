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

# проверяем уникальность email
def unique_email(emails):
    unique_email = set(emails)
    return len(emails) == len(set(emails))

# ищем общие товары в корзине
def common_products(cart1, cart2):
    set1 = set(cart1)
    set2 = set(cart2)
    return sorted(list(set1 & set2))

# ищем уникальные слова в тексте(отсортированы по алфавиту и в нижнем регистре)
def unique_words(text):
    words = text.split()
    lower_words = [word.lower() for word in words]
    unique_words = set(lower_words)
    return sorted(unique_words)

# ищем кто пропустил лекцию
def who_skipped(groups, present):
    set1 = set(groups)
    set2 = set(present)
    return  sorted(list(set1 - set2))

# dict() словарь
# получаем имена пользователей
def get_user_names(users):
    names = users.values()
    name_list = list(names)
    sorted_names = sorted(name_list)
    return sorted_names

# получаем список всех ключей пользователей
def keys_list(users):
    id = users.keys()
    id_list = list(id)
    sorted_id = sorted(id_list)
    return sorted_id

# получаем пары в виде "имя - id"
def name_id_pairs(users):
    result = []
    for key, value in users.items():
        pair = f"{value} - {key}"
        result.append(pair)
    return result

# получаем строки "ID: имя", сортируем по имени
def names_id(users):
    result = []
    for key, value in sorted(users.items(), key=lambda item: item[1]):
        keys_names = f"{key}:{value}"
        result.append(keys_names)
    return result

# ищем пользователей, у которых активность = True
def get_active_users(users):
    result = []
    for key,value in users.items():
        if value == True:
            result.append(key)
    return sorted(result)

# ищем неактивных пользователей = False
def get_inactive_users(users):
    result = []
    for key, value in users.items():
        if value == False:
            result.append(key)
    return sorted(result)

# ищем пользователей по роли
def find_admins(users):
    result = []
    for key, data in users.items():
        if data["role"] == "admin":
         result.append(key)
    return sorted(result)

# ищем активных пользователей с ролью "user"
def find_role_active(users):
    result = []
    for key, data in users.items():
        if data["role"] == "user" and data["active"] == True:
            result.append(key)
    return sorted(result)

# собираем строки "Имя (роль)"
def format_user_roles(users):
    result = []
    for key, data in users.items():
        user_info = f"{key}({data['role']})"
        result.append(user_info)
    return sorted(result)

# считаем количество пользователей по ролям
def count_roles(users):
    role_counts = {}
    for key, data in users.items():
       role = data["role"]
       if data["role"] in role_counts:
           role_counts[role] += 1
       else:
        role_counts[role] = 1
    return role_counts
        
# Ищем пользователей с определенной ролью и активностью
def find_users(users, role, only_active):
    result = []
    for key, data in users.items():
        if data["role"] == role and (data["active"]or not only_active):
            result.append(key)
    return sorted(result)

# ищем пользователей с определенным заказом еды (+ vegan)
def find_orders(orders, dish, only_vegan):
    result = []
    for key, data in orders.items():
        if data["dish"] == dish and (data["is_vegan"] or not only_vegan):
            result.append(key)
    return sorted(result)

# ищем псов и их имена
def find_pets(pets):
    result = []
    for key, data in pets.items():
        if data["type"] == "пёс":
            result.append(key)
    return sorted(result)

# Ищем учеников, которые учатся в обоих классах
def find_class(class_a, class_b):
    set1 = set(class_a)
    set2 = set(class_b)
    return(set1 & set2) 

# Ищем учеников, которые учатся ТОЛЬКО  в одном из 2х классов        
def find_only_class(class_a, class_b):
    set1 = set(class_a)
    set2 = set(class_b)
    return sorted(set1 ^ set2) 

# ищем имена, которые встречаются в списке больше 1 раза
def find_repeated_names(names):
    seen_once = set()  # множества имен, которые встречались 1 раз
    duplicates = set() # множества имен, кторые повторялись

    for name in names:
        if name in seen_once:
            duplicates.add(name)
        else:
            seen_once.add(name)
    return sorted(duplicates)

# ищем повторяющиеся роли пользователей
def find_repeated_roles(users):
    seen_only = set()
    duplicates = set()

    for key, data in users.items():
        role = data["role"]
        if data["role"] in seen_only:
            duplicates.add(role)
        else:
            seen_only.add(role)

    return sorted(duplicates)

# ищем роли, которые встречаются только 1 раз
def find_unique_roles(users):
    seen_once = set()
    duplicates = set()

    for key, data in users.items():
        role = data["role"]
        if data["role"] in seen_once:
            duplicates.add(role)
        else:
            seen_once.add(role)
    return sorted(seen_once - duplicates)

# ищем пользователей с уникальной ролью
def find_users_with_unique_roles(users):
    seen_once = set()
    duplicates = set()
    for key, data in users.items():
        role = data["role"]
        if role in seen_once:
            duplicates.add(role)
        else:
            seen_once.add(role)
        
    unique_roles = seen_once - duplicates
    result =[]
    for key, data in users.items():
        if data["role"] in unique_roles:
            result.append(key)
    return sorted(result)

# ищем блюда, заказанне только веганами 1 раз
def find_unique_vegan_dishes(orders):
    vegan_dishes = []
    for key, data in orders.items():  # ищеи блюда заказанные веганами
        if data["vegan"]:
            vegan_dishes.append(data["dish"])

    seen_once = set()
    duplicates = set()

    for dish in vegan_dishes: # тщем блюдо, которое встречалось только 1 раз
        if dish in seen_once:
            duplicates.add(dish)
        else:
            seen_once.add(dish)
    unique_dishes = seen_once - duplicates
    return sorted(unique_dishes)