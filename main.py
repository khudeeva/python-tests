# main.py
from utils.math_utils import multiply, greet, multiply_all, user_profile, apply_operation, apply_multiple_operations, filter_numbers, sort_by_key, filtered_words, apply_operations, sort_by_last_letter, longest_word, filter_by_first_letter, sum_of_squares # Импортируем функцию из пакета utils
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