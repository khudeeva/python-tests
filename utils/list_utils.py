# функции со списками(удаление дубликатов, сортировка, фильтрация )
# 🔢 Работа с числами в списках
# удаление четных чисел
def remove_even(numbers):
    odd_numbers = [x for x in numbers if x % 2 != 0]
    return sorted(odd_numbers, reverse=True)
# ищем среднее значение списка чисел
def average_num(numbers):
    return sum(numbers) / len(numbers)
# ищем числа, которые больше 5
def more_that_5(numbers):
    return [x for x in numbers if x > 5]
# фильтруем уникальные числа из списка
def filter_unique(numbers):
    return list(set(numbers))

#📚 Работа со строками в списках
# ищем самую длинную строку в списке
def find_longest_word(words):
    return max(words, key=len)
# ищем самую короткую строку в списке
def find_shortest_word(words):
    return min(words, key=len)
# оставляем слова, длина которых больше 4 симовлов
def filter_long_words(words):
    long_words = [word for word in words if len(word) > 4]
    return sorted(long_words)
# удаляем слова,в которых есть "а"
def remove_words_with_a(words):
    remove_words = [word for word in words if "а" not in word]
    return sorted(remove_words)
# ищем слова, начинающиеся с "м"
def words_starting_with_m(words):
    words_start = [word for word in words if  word.startswith("м")]
    return sorted(words_start)
# ищем слова, начинающиеся и заканчивающиеся одной и той же буквой
def same_first_last_letter(words):
    same_letter = [word for word in words if word[0]==word[-1]]
    return sorted(same_letter)
# сложная фильтрация(начало с "м", длина больше 3 символов, нет "о")
def difficult_filtered_words(words):
    filter_word = [word for word in words if word.startswith("м") 
                   and len(word) > 3 
                   and "о" not in word
                   ]
    return sorted(filter_word)

# сложная фильтрация (начинается на "м", длина не меньше 4, в верхний регистр, сортируем по алфавиту)
def transform_m_words(words):
    transform_word = [word.upper() for word in words 
                      if word.startswith("м")
                      and len(word) >= 4
                      ]
    return sorted(transform_word)

# капитализация слов по длине
def capitalize_long_words(words):
    capitalize_word = [word.capitalize() for word in words
                       if len(word) > 3
                       ]
    return sorted(capitalize_word)

# удаляем слова с четной длиной
def remove_even_length(words):
    even_length = [word for word in words if len(word)% 2 != 0]
    return sorted(even_length)

# преобразуем слова в длины
def word_lengths(words):
    lengths = [len(word) for word in words]
    return lengths

# 🧩Фильтрация по длине и первым буквам
# оставляем слова с "разрешенной" длиной
def filter_by_allowed_lengths(words, allowed_lengths):
    filter_lengths = [word for word in words 
                      if len(word) in allowed_lengths
                      ]
    return sorted(filter_lengths)

# оставляем слова по длине и первой букве
def filter_by_lengths_and_start(words, allowed_lengths, allowed_starts):
    result = [word for word in words 
              if len(word) in allowed_lengths
              and word[0] in allowed_starts
              ]
    return sorted(result)


# 🔁Работа с дубликатами
# ищем дубликаты и сортируем
def clean_names(names):
    clean = set(names)
    return sorted(clean)

# Ищем элементы, которые встречаются больше 1 раза
def find_duplicates(names):
    seen_once = set()
    duplicates = set()
    
    for name in names:
        if name in seen_once:
            duplicates.add(name)
        else:
            seen_once.add(name)
    return sorted(duplicates)

# ищем имена, которые встречаются ТОЛЬКО один раз
def find_unique_names(names):
    seen_once = set()
    duplicates = set()

    for name in names:
        if name in seen_once:
            duplicates.add(name)
        else:
            seen_once.add(name)
    unique_name = (seen_once - duplicates)
    return  sorted(unique_name)

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

print("\n get_even_numbers")
def get_even_numbers(lst):
    only_even_list = []
    for x in lst:
        if x % 2 == 0:
            only_even_list.append(x)
    return  only_even_list      

