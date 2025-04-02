import re
import pytest

# переворачиваем строку 
def reverse_string(text):
    return text[::-1]

# считаем гласные в строке
def count_vowels(text):
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    return sum(1 for letter in text if letter in vowels)

# делаем первую букву заглавной
def capitalize_first(text):
    if not text: #если строка пустая - возвращаем пустую строку
        return ""
    return text[0].upper() + text[1:] # делаем первую букву заглавной, остальное - оставляем как есть 
# проверка, что строка содержит только буквы
def is_alpha_only(text):
    return text.isalpha()

# проверка, является ли первая буква заглавной
def is_upper(text):
    return text[:1].isupper()

# удаляем пробелы из строк
def remove_spaces(text):
    return text.replace(" ", "")

# удаляем все цифры из строки
def remove_digits(text):
   return ''.join(char for char in text if not char.isdigit())

# возвращаем только буквы
def extract_letters(text):
    return ''.join(char for char in text if char.isalpha())

# проверка палиндрома
def is_palindrome(word):
    word = word.lower().replace(" ", "") # делаем буквы маленькими, удаляем пробелы между ними
    return word == word[::-1] # сравниваем слово с его перевернутой версией

#🔍 палиндромы
# проверка на палиндром предложений
def is_palindrome_sentence(text):
    clean = ''.join(c.lower() for c in text if c.isalpha())
    return clean == clean[::-1]


# делаем каждое слово в строке с заглавной буквы, остальные - строчные
def capitalize_word(text):
    return ' '.join(word.capitalize() for word in text.split())

# ищем слова, длина которых больше или равна min_length
def filtered_by_length(text, min_length):
    words = text.split()
    return [word for word in words if len(word) >= min_length]

# фильтруем по длине и первой букве
def filtered_by_length_and_start(text, min_length, start_letter):
    words = text.split()
    return [word for word in words if len(word)>= min_length
            and word.startswith(start_letter)]


# фильтруем слова, которые опредленной длины, начинаются на букву и не содержат букву
def filter_advanced(text, min_length, start_letter, forbidden_letter):
    words = text.split()
    return [word for word in words if len(word)>= min_length
            and word.startswith(start_letter)
            and forbidden_letter not in word
            ]

# разворачиваем каждое слово в строке
def invert_words(text):
    words = text.split()
    return ' '.join (word[::-1] for word in words)


# считаем сколько раз встретилась буква в строке без регистра
def count_letter_frequency(text, letter):
    text = text.lower()
    letter = letter.lower()
    return sum(1 for char in text if char == letter)

# принимаем строку и возвращаем подходящий результат
def analyze_string(text):
    if text.isspace(): # ! важен порядок выполнения 
        return "Только пробелы"
    elif not text.strip():
        return "Пустая строка"
    elif text.isdigit():
        return "Цифры"
    elif text.isalpha():
        return "Буквы"
    elif not any(char.isalnum() for char in text): #нет ни букв, ни цифр
        return "Только спецсимволы"
    else:
        return "Смешанная строка"

# анализ регистра строки
def analyze_case(text):
    if text.isupper():
        return "Все буквы заглавные"
    elif text.islower():
        return "Все буквы строчные"
    elif not any(char.isalpha() for char in text):
        return "Нет букв"
    else:
        return "Смешанный регистр"

# начало строки и точка в конце
def describe_string(text):
    if text[0].isupper() and text.endswith("."):
        return "Корректное предложение"
    elif text[0].isupper() and not text.endswith("."):
        return "Нет точки в конце"
    elif not text[0].isupper() and text.endswith("."):
        return "Нет заглавной буквы в начале"
    else:
        return "Некорректная строка"

# классифицирем слово по гласным,согласным
def classify_word(word):
    vowels = "аеёиоуыэюя"
    consonants = "бвгджзйклмнпрстфчцчшщ"
    letters = [char.lower() for char in word if char.isalpha()]
    
    if not letters:
        return "Нет букв"
    elif all(char in vowels for char in letters):
        return "Только гласные"
    elif all(char in consonants for char in letters):
        return "Только согласные"
    else:
        return "Смешанное"
    
# Ищем "богатое слово"(если больше 3 гласных и меньше 3 одинаковых букв подряд)
def classify_rich_word(word):
     vowels = "аеёиоуыэюя"
     vowels_count = sum(1 for letter in word if letter in vowels)

     for i in range(len(word) - 2):
         if word[i] == word[i+1] == word[i+2]:
             return "Не богатое"
     return "Богатое слово" if vowels_count > 3 else "Не богатое"

# возвращает словарь/строку с 3-мя значениями
def analyze_text(text):
    count_words = len(text.split())
    count_letters = sum(1 for char in text if char.isalpha())
    count_spaces =  text.count(" ")
    return {
        "Слова": count_words,
        "Буквы": count_letters, 
        "Пробелы": count_spaces
    }

# считаем частоту каждой буквы в тексте
def letter_frequency(text):
    result = {}

    for char in text.lower():
        if char.isalpha():
            if char in result:
                result[char] +=1
            else:
                result[char] =1
    return result 

# частота слов в тексте
def word_frequency(text):
    result = {}
    text = text.lower()
    words = text.split()
    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result

# ищем самое частое слово
def most_common_word(text):   
    text = text.lower()
    clean_text = re.sub(r'[^а-яа-zё\s]', '', text)
    words = clean_text.split()
    freq = {}
    
    for word in words:
        if word in freq:
          freq[word] +=1
        else:
            freq[word] = 1

    if not words:
        return None
    
    max_count = max(freq.values())
    for word in words:
        if freq[word] == max_count:
            return word

# удвоение строки        
def repeat_text(text):
    return text + text

# проверка, содержит ли тсрока хотя бы одну заглавную букву
def has_upper(text):
    return any(char.isupper() for char in text)

# проверка все ли слова в списке начинаются с заглавной
def all_capitalized(words):
    return all(word[0].isupper() for word in words if word)
        
def describe_words(words):
    if not words:
        return "Список пуст"
    all_lower = all(word[0].islower() for word in words if word)
    all_upper = all(word[0].isupper() for word in words if word)

    if all_lower:
        return "Все строчные"
    elif all_upper:
        return "Все заглавные"
    else:
        return "Смешанные"
# ФИКСТУРА
# фикстура словарь с данными книги
@pytest.fixture
def book_data():
    return {
        "title": "Мастер и Маргарита", "author": "Булгаков", "pages": 380
    }

# фикстура с данными пользователя
@pytest.fixture
def user_info():
    return {"name": "Анна", "age": 30, "city": "Москва"}

# фикстура со списком слов
@pytest.fixture
def words_list():
    return ["море", "солнце", "пляж", "отдых", "волна"]

# фикстура со списком словарей
@pytest.fixture
def people_data():
    return [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 40}
]

# фикстура со списком товаров
@pytest.fixture
def products_list():
    return [
         {"name": "Laptop", "price": 1200, "category": "electronics"},
         {"name": "Tomato", "price": 320, "category": "product"},
         {"name": "TV", "price": 4200, "category": "electronics"}
    ]

# фикстура список пользоватлей
@pytest.fixture
def users_list():
    return [
         {"username": "katya_01", "age": 25, "email": "katya@example.com"},
         {"username": "ivan_87", "age": 35, "email": "ivan@example.com"},
         {"username": "guest", "age": 15, "email": ""}
    ]
# фикстура: список фильмов
@pytest.fixture
def movies_list():
    return [
        {"title": "Inception", "rating": 8.8, "genre": "Sci-Fi", "year": 2010},
        {"title": "The Godfather", "rating": 9.2, "genre": "Crime", "year": 1972},
        {"title": "Interstellar", "rating": 8.6, "genre": "Sci-Fi", "year": 2014},
        {"title": "Unknown", "rating": 0, "genre": "Comedy", "year": 2023}  # для проверки краевых случаев
    ] 
# фикстура + scope="module"
@pytest.fixture(scope="module")
def film_list():
    print("Создаем список фильмов")
    return [
        {"title": "Matrix", "year": 1999},
        {"title": "Tenet", "year": 2020}
    ]
# фикстура: список пользователей по активности
@pytest.fixture(scope="module")
def users_active():
    print("Создаем список по активности")
    return [
        {"username": "admin", "active": True},
        {"username": "guest", "active": False},
        {"username": "moderator", "active": True}
    ]
# ОБЪЕДИНЕНИЕ ФИКСТУРЫ И ПАРАМЕТРИЗАЦИИ
# фикстура: список книг
@pytest.fixture(scope="module")
def books_list():
    print("Загружаем список книг")
    return [
        {"title": "1984", "author": "George Orwell", "year": 1949},
        {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932},
        {"title": "Dune", "author": "Frank Herbert", "year": 1965}

    ]