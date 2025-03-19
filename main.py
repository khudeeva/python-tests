# main.py
from utils.math_utils import multiply, greet, multiply_all, user_profile, apply_operation, apply_multiple_operations, filter_numbers, sort_by_key, filtered_words, apply_operations, sort_by_last_letter, longest_word, filter_by_first_letter, sum_of_squares, is_palindrome, count_vowels, average, shortest_word, closest_to_average, double, power, sum_all, sum_even_all, multiply_odd_all, max_difference, average_arifmetic, average_square, filter_by_vowels_count, remove_duplicates, remove_repeated, filter_vowel_words, filter_consonant_words, filter_two_vowels, filter_even_length, filter_same_first_last, filter_unique_letters, filter_repeated_letters, filter_by_digits_sum, filter_by_unique_letters, sum_of_digits, count_words, longest_word, most_vowels_word, replace_letters, word_lengths, most_frequent_word, least_frequent_word, count_sentences, replace_digits, divided_sentences, replace_words,  extract_numbers, find_words, find_dates, get_user_info, filter_unique, update_dict # Импортируем функцию из пакета utils
from math import prod

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