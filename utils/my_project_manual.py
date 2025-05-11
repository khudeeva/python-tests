from text_utils import (count_vowels, is_title_and_multiple_words,filtered_words, is_long_word, sort_by_last_letter, longest_word,
    filter_by_first_letter, shortest_word, closest_to_average,
    filter_by_vowels_count, filter_vowel_words, filter_consonant_words,
    filter_two_vowels, filter_even_length, filter_same_first_last,
    filter_unique_letters, filter_repeated_letters, count_words,
    most_frequent_word, least_frequent_word, count_sentences,
    replace_letters, word_lengths, replace_digits, divided_sentences,
    replace_words, extract_numbers, filtered_words_len, find_words,
    find_dates, find_unique_words, filter_by_unique_letters,
    get_user_info, most_vowels_word, is_alpha_only, is_palindrome, greet_user, count_vowels_practice
)

# 🔢 Импортируем функции, связанные с числами
from math_utils import(
    multiply, greet, apply_operation, apply_multiple_operations,
    filter_numbers, sort_by_key, apply_operations, sum_of_squares,
    average, double, power, find_median, sum_even_all, multiply_odd_all,
    max_difference, average_arifmetic, average_square,
    filter_by_digits_sum, sum_of_digits, is_big_and_divisible, is_even
)

# 📚 Импортируем функции, связанные со списками
from list_utils import (
    remove_even, clean_names, find_duplicates, find_unique_names,
    find_longest_word, find_shortest_word, filter_long_words,
    remove_words_with_a, words_starting_with_m, same_first_last_letter,
    difficult_filtered_words, average_num, more_that_5,
    transform_m_words, capitalize_long_words, remove_even_length,
    word_lengths, filter_by_allowed_lengths, filter_by_lengths_and_start,
    remove_duplicates, remove_repeated, filter_unique
)

# 🧩 Импортируем функции, связанные с множествами
from set_utils import (
    unique_numbers, count_unique, common_numbers, unique_from_first,
    unique_numbers_from_both, has_common_elements, is_subset,
    is_disjoint, has_duplicates, count_unique_pages, unique_users,
    who_didnt_submit, unique_email, common_products, unique_words,
    who_skipped
)

# 🧠 Импортируем функции, связанные со словарями
from dict_utils import (
    get_user_names, keys_list, name_id_pairs, names_id, get_active_users,
    get_inactive_users, find_admins, find_role_active, format_user_roles,
    count_roles, find_users, find_orders, find_pets, find_class,
    find_only_class, find_repeated_names, find_repeated_roles,
    find_unique_roles, find_users_with_unique_roles,
    find_unique_vegan_dishes, find_all_keys, find_inactive_users,
    find_unique_role_today, update_dict, dict_summary, get_skills, get_task_count, knows_python, top_user, all_skills, has_tasks
)

# ✨ Импортируем функции с *args, **kwargs, фильтрацией по типам
from flex_utils import (
    multiply_all, user_profile, sum_all, car_info, total_sum,
    filter_strings, filter_numbers_kwargs, count_strings,
    summarize_and_collect_strings, find_booleans, count_booleans,
    person_details, calculate_stats, add_all, max_from_args, count_positives, greet_user_kwargs, is_qa_user, describe_user, user_summary, summarize_person, profile_summary
)

print(multiply(3, 7))  # 21

print(greet()) # Добро пожаловать, Гость!
print(greet("Анна")) # Добро пожаловать, Анна!
    
print(multiply_all(1, 2, 3)) # 6
print(multiply_all(2, 4, 6)) # 48

user_profile(name="Ksenia", age=25, city="Perm")

# Использую apply_operation() с лямбда-функциями
print(apply_operation(lambda x, y: x+ y, 10, 5)) # 15
print(apply_operation(lambda x, y: x - y, 10, 5)) #5
print(apply_operation(lambda x, y: x / y, 10, 5)) # 2

# передаем список операций
operations = [
    lambda x, y: x + y,
    lambda x, y: x * y,
    lambda x, y: x - y
]
print(apply_multiple_operations(operations, 5, 3))

# фильтрация числен по условию
numbers = [10, 15, 20, 25, 30, 35]

# фильтруем только чётные числа
even_numbers = filter_numbers(numbers, lambda x: x % 2 == 0)
print(even_numbers)

# фильтруем числа, которые больше 20
greater_than_20 = filter_numbers(numbers, lambda x: x > 20)
print(greater_than_20)

# сортируем людей по ключу
people = [
    {"name": "Анна", "age": 25},
    {"name": "Иван", "age": 30},
    {"name": "Мария", "age": 22}
]

# Сортируем по возрасту
sorted_by_age = sort_by_key(people, lambda person: person["age"])
print(sorted_by_age)

# фильтруем слова, с lambda: длина больше 5 символов, содержат "а"
words = ["яблоко", "груша", "арбуз", "апельсин", "персик", "слива"]
filtered = filtered_words(words, lambda word: len(word) > 5 and "а" in word)
print(filtered)

# применяем несколько математических опреаций 
operations = [
lambda x, y: x + y,
lambda x, y: x * y,
lambda x, y: x ** y
]
print(apply_operations(operations, 2, 3))

# Сортируем слова по последней букве
words = [ "кот", "собака", "питон", "ананас", "ёжик"]
sorted_words = sort_by_last_letter(words)
print(sorted_words)

# Ищем самое длинное слово в списке
words = ["кот", "собака", "слон", "медведь", "ёжик"]
print(longest_word(words))

# фильтруем слова по начальной букве
words = ["ананас", "апельсин", "арбуз", "банан", "абрикос"]
print(filter_by_first_letter(words, "а"))

# вычисляем сумму квадратов числа:
numbers = [1, 2, 3, 4]
print(sum_of_squares(numbers))

# проверка палиндрома
print(is_palindrome("топот"))
print(is_palindrome("шорох"))
print(is_palindrome("радар"))
print(is_palindrome("А роза упала на лапу Азора"))

# подсчет количества гласных
print(count_vowels("привет"))
print(count_vowels("обучение"))
print(count_vowels("ТеТрАдь"))
print(count_vowels("самообразование"))
 
 # ищем среднее арифметическое
print(average([1, 2, 3, 4, 5]))  # 3.0
print(average([10, 20, 30]))  # 20.0
print(average([7, 14, 21, 28]))  # 17.5
print(average([])) # 0

# ищем самое короткое слово
words = ["машина", "телевизор", "кот", "иммунитет"]
print(shortest_word(words))

# ищем слово с длиной ближе к среднему значению
words = ["машина", "телефон", "кот","планета","дом"]
print(closest_to_average(words))

# удвоение числа
print(double(10))
print(double(7))

# параметр по умолчанию
print(power(3))
print(power(2, 5))

# суммируем все числа с *args
print(sum_all(1, 2, 3, 4, 5))
print(sum_all(10, 20, 30))

# ищем сумму всех четных чисел
numbers = [3, 10, 7, 4, 12, 5, 8, 21, 6, 14]
print(sum_even_all(numbers))

# ищем произведение всех нечетных чисел
numbers = [2, 3, 5, 7, 8, 10, 11, 13, 15]
print(multiply_odd_all(numbers))

# ищем максимальную разницу между числами
numbers = [20, 5, 15, 30, 50, 10]
print(max_difference(numbers))

# ищем среднее арифметическое 
numbers = [10, 15, 20, 25, 30, 35]
print(average_arifmetic(numbers))

# ищем среднее квадратичное отклонение 
numbers = [10, 20, 30, 40, 50]
print(average_square(numbers))

# фильтруем строки по количеству гласных
words = ["погода", "кот", "машина", "окно", "стол"]
print(filter_by_vowels_count(words, 2))

# удаляем дубликаты в списке
numbers = [1, 2, 3, 2, 4, 1, 5]
print(remove_duplicates(numbers)) 

# удаляем из списка элементы, которые встречаются больше 1 раза
numbers = [1, 2, 3, 2, 4, 1, 5]
print(remove_repeated(numbers))

# фильтрация строк, содержащихся гласные буквы
words = ["дом", "крт", "мост", "стул", "яблоко"]
print(filter_vowel_words(words))

# фильтрация слов, которые начинаются и заканчиваются на согласную букву
words = ["мост", "река", "груша", "стол", "лист"]
print(filter_consonant_words(words)) 

# фильтруем слова, которые содержат больше/= 2 гласных в слове
words = ["мост", "река", "груша", "стол", "лист", "океан"]
print(filter_two_vowels(words))

# фильтруем слова, еоторые содержат четное количество букв в слове
words = ["кот", "стол", "мост", "дверь", "окно"]
print(filter_even_length(words))

# фильтрация слов, где первая и последняя буквы одинаковые
words = ["мама", "кокос", "стол", "ананас", "река", "топот"]
print(filter_same_first_last(words))

# фильтрация слов, которые содержат только уникальные буквы
words = ["кот", "мама", "лист", "сосна", "дом"]
print(filter_unique_letters(words))

# фильтрация слов с повторяющимися буквами
words = ["кот", "мама", "лист", "сосна", "дом", "река", "шар"]
print(filter_repeated_letters(words)) 

# фильтрация чисел по сумме цифр
numbers = [10, 23, 34, 47, 58, 99]
print(filter_by_digits_sum(numbers, 10))

# фильтрация слов по количеству уникальных букв
words = ["папа", "ананас", "книга", "дом", "программист"]
print(filter_by_unique_letters(words, 5))

# функция для суммы цифр числа
print(sum_of_digits(123))  
print(sum_of_digits(789))

# подсчет количества слов в строке
print(count_words("Привет, как дела?"))  # 3
print(count_words("Python лучший язык"))  # 3
print(count_words("Один"))  # 1

# ищем самое длинное слово в строке
print(longest_word("Солнце светит ярко"))  # "Солнце"
print(longest_word("Я изучаю программирование"))  # "программирование"

# проерка на палиндроме
print(is_palindrome("топот"))  # True
print(is_palindrome("казак"))  # True
print(is_palindrome("дом"))  # False

# ищем самое короткое слово в тексте
print(shortest_word("Я люблю программирование"))  # "Я"
print(shortest_word("Python лучший язык"))  # "язык"
print(shortest_word(12345))  # "Ошибка: не строка"

# ищем слово с максимальным количеством гласных
print(most_vowels_word("Алиса любит математику"))  # "математику"
print(most_vowels_word("Программирование это искусство"))  # "Программирование"
print(most_vowels_word(12345))  # "Ошибка: не строка"

# замена букв в тексте
print(replace_letters("Привет, мир!", "и", "ы"))  # "Прывыт, мыр!"
print(replace_letters("hello world", "o", "0"))   # "hell0 w0rld"

# считаем количество букв в каждом слове
print(word_lengths("Привет мир"))  # [6, 3]
print(word_lengths("Это тестовая строка"))  # [3, 9, 6]

# выбираем самое частое слово в тексте
print(most_frequent_word("кот собака кот кот собака дом")) # "кот"

# ищем самое редкое слово в тексте
print(least_frequent_word("ягода малина ягода  ягода")) # малина

# считаем количество предложений в тексте
print(count_sentences("Я изучаю программирование? Да, верно! Это очень сложно, но нужно."))

# замена всех цифр в тексте на *
print(replace_digits("Привет, 98! Мой номер 123-456."))  # Ожидаем: "Привет, **! Мой номер ***-***."

# делим текст по ,.!
print(divided_sentences("Привет, как дела! Всё хорошо. Увидимся позже!"))

# замена всех букв "а" и "о" на * в тексте
print(replace_words("Моя кошка обожает апельсины"))

# извлекаем из строки только числа
print(extract_numbers("Мой номер 456-789, а твой 123-456?"))

# ищем слова с длиной от 4 до 6 букв
print(find_words("апельсин, яблоко, якорь, машина"))

# ищем все даты в формате ДД.ММ.ГГГГ
text = "Сегодня 12.03.2024, а завтра 13.03.2024. А ещё 01.01.2025."
print(find_dates(text))  # ['12.03.2024', '13.03.2024', '01.01.2025']

# проверяем, как функция возвращает кортеж
print(get_user_info("Анна", 25, "Москва"))

# фильтруем уникальные числа из списка
print(filter_unique([1, 2, 2, 3, 4, 4, 5]))

# добавляем ключи в словарь
print(update_dict({"name": "Иван", "age": 30}))

# возвращаем строку из словаря
print(dict_summary({"name": "Ksenia", "age": 25}))

print("\n get_skills")
print(get_skills("ksenia"))
print(get_skills("anna"))

print("\n get_task_count")
print(get_task_count("ksenia"))
print(get_task_count("lena"))

print("\n know_python")
print(knows_python("ksenia"))
print(knows_python("lena"))

print("\n top_users")
# словарь передаем извне
tasks_data = { 
    "ksenia": 5,
    "dima": 3,
    "lena": 7
}
print(top_user(tasks_data))

print("\n all_skills")
print(all_skills({
    "ksenia": ["Python", "SQL"],
    "dima": ["HTML", "CSS", "SQL"],
    "anna": ["Python", "Postman"]
}))

print("\n has_tasks")
print(has_tasks("dima"))   
print(has_tasks("anna"))   
print(has_tasks("oleg"))   


# проверяем поиск только уникальных слов
print(find_unique_words("Я люблю Python. Python - это круто!"))

# проверяем множество уникальных значений 
print(unique_numbers([1, 2, 2, 3, 4, 4, 5]))

# ищем количество уникальных чисел в списке
print(count_unique([1, 2, 2, 3, 4, 4, 5]))

# ищем только те числа, которые есть одновременно в двух списках
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7]
print(common_numbers(list1, list2))

# ищем элементы из первого списка, которых нет во втором 
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
print(unique_from_first(list1, list2))

# ищем числа которе есть ТОЛЬКО в одном из двух списков
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
print(unique_numbers_from_both(list1, list2))

# ищем пересечение, если в списках есть хотя бы 1 общий элемент
list1 = [10, 20, 30]
list2 = [40, 50, 30]
print(has_common_elements(list1, list2))

# ищем подмножество
list1 = [1, 2]
list2 = [1, 2, 3, 4]
print(is_subset(list1, list2))

# проверяем не имеют ли два списка общие элементы
print(is_disjoint([1, 2, 3], [4, 5, 6]))  #True  
print(is_disjoint([1, 2, 3], [3, 4, 5]))  #False

# проверка на дубликаты
print(has_duplicates([1, 2, 3, 4, 5]))      # False — всё уникально
print(has_duplicates([1, 2, 2, 3, 4, 5]))   # True — есть повтор

# считаем количество уникальных посещенных страниц
visited_pages = ["/home", "/about", "/home", "/products", "/contact", "/products", "/home"]
print(count_unique_pages(visited_pages))

# ищем уникальные имена, отсортированные по алфавит
users = ["Аня", "Борис", "Аня", "Глеб", "Борис", "Ева"]
print(unique_users(users))

# ищем кто не сдал работу, отсортируем по алфавиту
all_students = ["Аня", "Борис", "Глеб", "Ева", "Дима"]
submitted = ["Глеб", "Аня", "Ева"]
print(who_didnt_submit(all_students, submitted))

#проверяем уникальность email
emails = ["a@test.com", "b@test.com", "a@test.com", "c@test.com"]
print(unique_email(emails))

# ищем общие товары в корзине
cart1 = ["молоко", "хлеб", "сыр", "сок"]
cart2 = ["чай", "хлеб", "сыр", "вода"]
print(common_products(cart1, cart2))

# ищем уникальные слова в тексте (отсортированы и в нижнем регистре)
text = "Hello world hello Python python code"
print(unique_words(text))

# ищем кто пропустил лекцию(отсортированы по алфавиту)
group = ["Аня", "Борис", "Вика", "Глеб", "Данил"]
present = ["Вика", "Глеб", "Аня"]
print(who_skipped(group, present))


users = {
    101: "Аня",
    102: "Борис",
    103: "Глеб",
    104: "Ева"
}
print(get_user_names(users))# получаем имена пользователей из словаря(+сортируем по алфавиту)
print(keys_list(users))# получаем список всех ключей(id)
print(name_id_pairs(users))# получаем пары в виде "имя - id"
print(names_id(users)) # получаем строки "ID: имя", сортируем по имени


users = {
    "Аня": True,
    "Борис": False,
    "Глеб": True,
    "Ева": False,
    "Данил": True
}
print(get_active_users(users))# ищем пользователей, у которых активность = True
print(get_inactive_users(users))# ищем неактивных пользователей == False



users = {
    "Аня": {"role": "admin", "active": True},
    "Борис": {"role": "user", "active": False},
    "Глеб": {"role": "admin", "active": True},
    "Ева": {"role": "user", "active": False},
    "Данил": {"role": "user", "active": True}
}
print(find_admins(users))# ищем пользователей по роли
print(find_role_active(users))# ищем активных пользователей с ролью "user"
print(format_user_roles(users))# собираем строки "Имя (роль)"
print(count_roles(users))# считаем количество пользователей по ролям
# Ищем пользователей с определенной ролью и активностью:
print(find_users(users, role="user", only_active=True)) 
print(find_users(users, role="user", only_active=False))  
print(find_users(users, role="admin", only_active=True))  

# ищем пользователей с определенным заказом еды(+ vegan)
orders = {
    "Аня": {"dish": "пицца", "is_vegan": False},
    "Борис": {"dish": "салат", "is_vegan": True},
    "Глеб": {"dish": "бургер", "is_vegan": False},
    "Ева": {"dish": "овощной боул", "is_vegan": True},
}

print(find_orders(orders, dish="салат", only_vegan=True)) # ['Борис']
print(find_orders(orders, dish="пицца", only_vegan=False)) # ['Аня']

# ищем псов и их имена
pets = {
    "Мурзик": {"type": "кот", "age": 2},
    "Шарик": {"type": "пёс", "age": 5},
    "Рекс": {"type": "пёс", "age": 3},
}
print(find_pets(pets))


class_a = ["Аня", "Борис", "Глеб", "Ева"]
class_b = ["Глеб", "Данил", "Ева", "Жанна"]
print(find_class(class_a, class_b))# Ищем учеников, которые учатся в обоих классах
print(find_only_class(class_a, class_b))# Ищем учеников, которые учатся ТОЛЬКО  в одном из 2х классов 


# ищем имена, которые встречаются в списке больше 1 раза
names = ["Аня", "Борис", "Аня", "Глеб", "Ева", "Глеб", "Аня"]
print(find_repeated_names(names))

users = {
    "Аня": {"role": "admin", "active": True},
    "Борис": {"role": "user", "active": False},
    "Глеб": {"role": "admin", "active": True},
    "Ева": {"role": "user", "active": False},
    "Данил": {"role": "user", "active": True},
    "Жанна": {"role": "manager", "active": True}
}
print(find_repeated_roles(users)) # ищем повторяющиеся роли пользователей
print(find_unique_roles(users))# ищем роли, которые встречаются только 1 раз
print(find_users_with_unique_roles(users))# ищем пользователей с уникальной ролью


orders = {
    "Аня": {"dish": "пицца", "vegan": False},
    "Борис": {"dish": "салат", "vegan": True},
    "Глеб": {"dish": "пицца", "vegan": False},
    "Ева": {"dish": "салат", "vegan": True},
    "Данил": {"dish": "овощной боул", "vegan": True},
    "Жанна": {"dish": "тофу", "vegan": True}
}
print(find_unique_vegan_dishes(orders))

# получаем список всех ключей в словаре, отсортируем по алфавиту
data = {
    "orange": 3,
    "apple": 5,
    "banana": 2
}
print(find_all_keys(data))


# ищем медиану
print(find_median(10, 20, 30, 40, 50))
print(find_median(1, 3, 5, 7))
print(find_median(2, 8, 10, 12, 14))
print(find_median(4, 6, 8, 10))
# Ищем, кто не заходил на сайт сегодня
all_users = ["Аня", "Борис", "Глеб", "Ева", "Данил"]
active_today = ["Глеб", "Ева"]
print(find_inactive_users(all_users, active_today))

# ищем пользователей с уникальной ролью, которые сегодян не заходили на сайт
users = {
    "Аня": {"role": "admin"},
    "Борис": {"role": "user"},
    "Глеб": {"role": "admin"},
    "Ева": {"role": "user"},
    "Данил": {"role": "user"},
    "Жанна": {"role": "manager"}
}

active_today = ["Глеб", "Ева"]
print(find_unique_role_today(users, active_today))  

# удаляем четные числа
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(remove_even(numbers))


names = ["Аня", "Борис", "Аня", "Глеб", "Ева", "Глеб", "Аня"]
print(clean_names(names)) # ищем дубликаты и сортируем
print(find_duplicates(names)) # Ищем элементы, которые встречаются больше 1 раза
print(find_unique_names(names)) # ищем имена, которые встречаются ТОЛЬКО один раз

words = ["кот", "бегемот", "слон", "анаконда", "мышь"]
print(find_longest_word(words))# ищем самую длинную строку в списке
print(find_shortest_word(words)) # самая короткая строка
print(filter_long_words(words)) # ищем слова с длиной больше 4 символов
print(remove_words_with_a(words)) # удаляем слова с "а"
print(words_starting_with_m(words)) # ищем слова, начинающиеся на "м"
print(same_first_last_letter(words)) # ищем слова, начинающиеся и заканчивающиейся одной и той же буквой
print(difficult_filtered_words(words))



numbers = [3, 7, 2, 10, 5]
print(average_num(numbers)) # ищем среднее значение 
print(more_that_5(numbers)) # ищем числа, которые больше 5

words = ["кот", "молоко", "арбуз", "мышь", "дом", "мак", "мама"]
print(transform_m_words(words)) # сложная фильтрация (начинается на "м", длина не меньше 4, в верхний регистр, сортируем по алфавиту)

print("\n capitalize_long_words")
print(capitalize_long_words(words)) # капитализация слов по длине

print("\n remove_even_length")
print(remove_even_length(words)) # удаляем слова с четной длиной

print("\n word_lengths")
print(word_lengths(words)) # преобразуем слова в длины

allowed_lengths = [3, 5]
print("\n filter_by_allowed_lengths")
print(filter_by_allowed_lengths(words, allowed_lengths)) # оставляем слова с "разрешенной" длиной 

allowed_lengths = [3, 4]
allowed_starts = ["м", "ч"]
print("\n filter_by_lengths_and_start")
print(filter_by_lengths_and_start(words, allowed_lengths, allowed_starts))

print("\n is_even") # проверяем четность числа
print(is_even(5))
print(is_even(8))

print("\n is_long_word") # проверка, что длина слова больше 5
print(is_long_word("арбуз"))
print(is_long_word("паламера"))


print("\n is_big_and_divisible") # проверка, что число больше 10 и делится на 3
print(is_big_and_divisible(9))
print(is_big_and_divisible(90))
print(is_big_and_divisible(12))


print("\n is_title_and_multiple_words")# проверка, что строка начинается с заглавной буквы и содержит больше 1 слова
print(is_title_and_multiple_words("привет"))
print(is_title_and_multiple_words(" привет пока"))
print(is_title_and_multiple_words("Привет"))
print(is_title_and_multiple_words("Привет пока"))

print("\n is_alpha_only")# проверка, что строка содержит только буквы, без цифр и символов
print(is_alpha_only("Привет"))
print(is_alpha_only("привет:)"))
print(is_alpha_only("выпей воды"))
print(is_alpha_only("113"))

print("\n total_sum") # ищем сумму всех переданных чисел
print(total_sum(1, 2, 3))
print(total_sum(10, 20, 30))
print(total_sum())

print("\n filter_strings") # возвращаем только строки
print(filter_strings(name="Anna", age=25, city="Moscow"))

print("\n filter_numbers_kwargs") # возвращаем только числа
print(filter_numbers_kwargs(name="Anna", age=30, height=1.68, active=True))

print("\n count_strings")#считаем количество строк
print(count_strings(name="Anna", age=30, city="Moscow", height = 1.7))

print("\n summarize_and_collect_strings") # суммируем *args, а из **kwargs берем только строки
print(summarize_and_collect_strings(1, 2, 3, name="anna", age=30, city="Perm"))

print("\n find_booleans") # ищем ключи, значения которыз булевые
print(find_booleans(active=True, name="Аня", verified=False, age=25))

print("\n count_booleans") # считаем количество булевых значений
print(count_booleans(active=False, name="Anna", age=30, verified=True))

print("\n multiply_all") # перемножаем все переданные числа
print(multiply_all(2, 3, 4))
print(multiply_all(11, 5))

print("\n add_all") # возвращаем сумму всех переданных чисел
print(add_all(1, 2, 3))
print(add_all(10, 5))
print(add_all(0, 0))
print(add_all(-10, -20))

print("\n max_from_args")
print(max_from_args(3, 5, 1))
print(max_from_args(10))
print(max_from_args(-10))
print(max_from_args())

print("\n count_positives")
print(count_positives(1, -2, 3, -4, 0))
print(count_positives(-1, -2))
print(count_positives())

print("\n greet_user_kwargs")
print(greet_user_kwargs(name = "Ksenia", age = 25))
print(greet_user_kwargs(name="Dima"))
print(greet_user_kwargs())

print("\n is_qa_user")
print(is_qa_user(name = "Ksenia", is_qa = True))
print(is_qa_user(name="Dima", is_qa = False))
print(is_qa_user(name="Anna"))

print("\n describe_user")
print(describe_user(name="Ksenia", city="Perm", is_active = True))
print(describe_user(name = "Dima", is_active = False))

print("\n user_summary")
print(user_summary("Ksenia", "Python", "SQL", city = "Perm", experience = 2))

print("\n summarize_person")
print(summarize_person("Ksenia", "Python", "SQL", city = "Perm", age = 25, is_active = True))

print("\n profile_summary")
print(profile_summary("Ksenia", "Fitness", "Dance", country = "Russia", verified = True))
# ПОВТОРЕНИЕ
print(greet_user("Max"))

print(count_vowels_practice("Привет"))
print(count_vowels_practice("Солнце ясное"))

