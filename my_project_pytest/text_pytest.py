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


 
