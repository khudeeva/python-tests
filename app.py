# проверка чётности числа
def is_even(number):
    return number % 2 == 0

# проверка, является ли число простым
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

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

# проверка на палиндром строк
def is_palindrome(text):
    return text==text[::-1]

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

# считаем сколько раз встретилоась буква в строке без регистра
def count_letter_frequency(text, letter):
    text = text.lower()
    letter = letter.lower()
    return sum(1 for char in text if char == letter)