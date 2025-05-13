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
# ПРОВЕРКА ИСКЛЮЧЕНИЙ 
# проверка исключения(KeyError)
def get_price(product):
    return product["price"]

# ищем автора книги, с помощью with pytest.raises()
def get_author(book):
    return book["author"]

# проверяем рейтинг фильма
def get_rating(movie):
    rating = movie["rating"] # может вызвать KeyError
    if not isinstance(rating,(int, float)):
        raise TypeError("Rating must be a number")
    if rating < 0 or rating > 10:
        raise ValueError("Rating must be between 0 and 10")
    return rating

# проверка страниц книги
def get_pages(book):
    pages = book["pages"]  # KeyError
    if not isinstance(pages,(int, float)): # TypeError
        raise TypeError("Pages must be a number")
    if pages <= 0 or pages > 2000: # ValueError
        raise ValueError("Pages must be between 1 and 2000")
    return pages

# тестируем список пользователей (фикстура+ параметризация)
@pytest.fixture(scope="module")
def users_list():
    return [
    {"username": "admin", "age": 35, "email": "admin@example.com"},
    {"username": "guest", "age": 15, "email": ""},
    {"username": "manager", "age": "unknown", "email": "manager@example.com"}
]

# проверка возраста с исключениями
def get_age(user):
    age = user["age"]
    if not isinstance(age,(int, float)):
        raise TypeError("Age must be a number")
    if age < 0:
        raise ValueError("Age must be between 1 and 60")
    return age
    
# проверка объединения на списке книг
@pytest.fixture(scope="module")
def books_list_by_pages():
    return [
    {"title": "Dune", "pages": 412, "available": True},
    {"title": "1984", "pages": 328, "available": False},
    {"title": "Brave New World", "pages": "many", "available": True}
]
#работа с исключениями по страницам книг
def get_pages_of_book(books):
    pages = books["pages"]
    if not isinstance(pages,(int, float)):
        raise TypeError("Pages must be a number")
    if pages <= 0:
        raise ValueError("Pages must be more than 0")
    return pages

# параметризация + исключения
def get_discounted_price(product):
    # получаем price, discount из словаря
    price = product["price"]
    discount = product["discount"]
    # проверка, что price - число, иначе - ошибка
    if not isinstance(price, (int, float)):
        raise TypeError("Price must be a number")
    # проверка, что discount - число, иначе - ошибка
    if not isinstance(discount, (int, float)):
        raise TypeError("Discount must be a number")
    # проверка, что price > 0(положительное число)
    if price <= 0:
        raise ValueError("Price  must be positive")
    # проверка, что скидка от 0 до 1, иначе - ошиибка
    if discount < 0 or discount >1:
        raise ValueError("Discount must be be between 0 and 1")
    # возвращаем стоимость со скидкой 
    return price - (price * discount)

# ищем возраст (параметризация + проверка исключений)
def get_age_person(user):
    age = user["age"]
    # проверяем, что это число
    if not isinstance(age, (int, float)):
        raise TypeError("Age must be a number")
    if age <= 0 :
        raise ValueError("Age must be positive")
    return age

# проверка пароля пользователя
def validate_password(password_list):
    password = password_list["password"]
    # проверяем, что это строка
    if not isinstance(password, str):
        raise TypeError("Password must be a string")
    if len(password) < 6:
        raise ValueError("Password must be after 6 symbols")
    if not any(char.isdigit() for char in password):
        raise ValueError("Password must contain at least one digit")
    
    return "Password accepted"

# проверка стоимости доставки
def calculate_shipping(order):
    weight = order["weight"]
    destination = order["destination"]

    if not isinstance(weight,(int, float)):
        raise TypeError("Weight must be a number")
    if weight <=0:
        raise ValueError("Weight must be positive")
    if destination not  in ["local", "international"]:
        raise ValueError("Destination must be 'local' or 'internationsl'")
    if destination == "local":
        return weight * 5
    else:
        return weight * 10

# налог на покупку
def calculate_tax(item):
    price = item["price"]
    tax_rate = item["tax_rate"]

    if not isinstance(price, (int, float)):
        raise TypeError("Price must be a number")
    if not isinstance(tax_rate, (int, float)):
        raise TypeError("Tax_rate must be a number")
    if price < 0:
        raise ValueError("Price must be positive")
    if tax_rate < 0:
        raise ValueError("Tax_rate must be positive")
    return price + (price * tax_rate)
# ПОВТОРЕНИЕ
def count_vowels_practice(text):
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    return sum(1 for letter in text if letter in vowels)
def reverse_text_practice(text):
    return text[::-1]
def normalize_text_practice(text):
    return text.strip().lower()

def count_words_practice(text):
    words = text.split()
    return len(words)

def is_title_case(text):
    stripped = text.lstrip()
    if not stripped:
        return False
    return stripped[0].isupper()
def count_unique_words_practice(text):
    words = text.lower().split()
    unique_words = set(words)
    return len(unique_words)
def contains_only_letters_practice(text):
    return text.isalpha()
# считаем количество заглавных букв в строке
def count_uppercase(text):
    return sum(1 for letter in text if letter.isupper())

@pytest.fixture
def user_data_fixture():
    return {"name": "Марина", "role": "QA", "age": 25}

@pytest.fixture
def qa_skills():
    return ["Postman", "PyTest", "Selenium", "SQL"]

@pytest.fixture(scope="module")
def project_info():
    return {"project": "Autotest", "version": 1.0}
     


def check_user_role(role, valid_roles):
    if role in valid_roles:
        return "OK"
    else:
        raise ValueError("Недопустимая роль")
    
def validate_age(age, min_age):
    if age >= min_age:
        return "Допущен"
    else:
        raise ValueError("Слишком молодой")
    
