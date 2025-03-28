import re

# 🔣подсчет символов
# считаем гласные в строке
def count_vowels(text):
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    return sum(1 for letter in text if letter in vowels)

#подсчет количества слов в строке
def count_words(text):
    if not isinstance(text, str):
        return "Ошибка: не строка"
    words = text.split()
    return len(words)
# считаем количество предложений в тексте
def count_sentences(text):
    if not isinstance(text, str):
        return "Ошибка: не строка"
    sentences = re.split(r'[.!?]', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    return len(sentences)

# 🔤проверки
# проверка, что строка начинается с заглавной буквы и содержит больше 1 слова
def is_title_and_multiple_words(text):
    return text[0].isupper() and len(text.split()) > 1
# проверка, что строка содержит только буквы
def is_alpha_only(text):
    return text.isalpha()
# проверка палиндрома
def is_palindrome(word):
    word = word.lower().replace(" ", "") # делаем буквы маленькими, удаляем пробелы между ними
    return word == word[::-1] # сравниваем слово с его перевернутой версией



# 🧹удаление символов
# замена всех цифр в тексте на *
def replace_digits(text):
    if not isinstance(text, str):
        return "Ошибка: не строка"
    return re.sub(r'\d','*', text)
# замена всех букв "а" и "о" на * в тексте
def replace_words(text):
    if not isinstance(text, str):
        return "Ошибка: не строка"
    return re.sub(r'[ао]', '*', text) # несколько букв заключи в []


# 📏фильтрация по длине и другим признакам
# проверка длины слова
def is_long_word(word):
    return len(word) > 5
# Сортируем слова по последней букве
def sort_by_last_letter(words):
    return sorted(words, key=lambda word: word[-1]) #сортируем по последнему символу слова
# ищем самое длинное слово в строке
def longest_word(text):
    if not isinstance(text, str):
        return "Ошибка: не строка"
    words = text.split()
    return max(words, key=len)
# ищем самое короткое слово в тексте
def shortest_word(text):
    if not isinstance(text, str):
        return "Ошибка: не строка"
    words = text.split()
    return min(words, key=len)
# ищем слово с длиной ближе к среднему значению
def closest_to_average(words):
    avg_length = sum(len(word) for word in words) / len(words)
    return min(words, key=lambda word: abs(len(word) - avg_length))
# фильтруем слова по начальной букве
def filter_by_first_letter(words, letter):
    return[word for word in words if word.startswith(letter)]
# фильтрация строк, содержащихся гласные буквы
def filter_vowel_words(words):
    vowels = "аеёиоуыэюя"
    return [word for word in words if any( letter in vowels for letter in word)] 
# фильтрация слов по количеству уникальных букв
def filter_by_unique_letters(words, max_unique):
    return[word for word in words if len(set(word)) <= max_unique]


# 📊Фильтрация списков слов
 #фильтрация строк по количеству гласных
def filter_by_vowels_count(words, min_vowels):
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    return [word for word in words if sum(1 for letter in word if letter in vowels) >=min_vowels]
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


# 📚Работа с текстом 
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
# оставляем в тексте слова длиной от 4 до 6 символов
def filtered_words_len(text):
    if not isinstance(text, str):
        return "Ошибка: не строка"
    words = text.split()
    return [word for word in words if 4 <= len(word) <= 6]
# ищем слово с максимальным количеством гласных
def most_vowels_word(text):
    if not isinstance(text, str):
        return "Ошибка: не строка"
    
    vowels = "аеёиоуыэюя"
    words = text.split()

    return max(words, key=lambda word: sum(1 for letter in word if letter in vowels))



# 📥Работа с регулярками
# делим текст по ,.!
def divided_sentences(text):
    if not isinstance(text, str):
        return "Ошибка: не строка"
    sentences = re.split(r'[,.!]', text) # разделяем текст по знакам препинания
    sentences = [s.strip() for s in sentences if s.strip()] # убираем пустые строки
    return(sentences)
# извлекаем из строки только числа
def extract_numbers(text):
    if not isinstance(text, str):
        return "Ошибка: не строка"
    return re.findall(r'\d+', text) # находим все группы цифр
# ищем все даты в формате ДД.ММ.ГГГГ
def find_dates(text):
    if not isinstance(text, str):
        return "Ошибка: не строка"
    return re.findall(r'\b\d{2}\.\d{2}\.\d{4}\b', text)
# ищем слова с длиной от 4 до 6 букв
def find_words(text):
    if not isinstance(text, str):
        return "Ошибка: не строка"
    return re.findall(r'\b\w{4,6}\b', text)


# 🌈Прочее
# ищем только уникальные слова(без повторений, в нижнем регистре)
def find_unique_words(text):
    if not isinstance(text, str):
        return "Ошибка: не строка"
    words = re.findall(r'\b\w+\b', text.lower())
    return list(set(words))
# фильтрация строк по длине и наличию букв (lambda)
def filtered_words(words, condition):
    return[word for word in words if condition(word)]
# проверяем как функция возвращает кортеж
def get_user_info(name, age, city):
    return(name, age, city)