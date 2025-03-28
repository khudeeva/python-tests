# функции, связанные с множествами(пересечения, подмножества)

# 📌уникальные значения и подсчеты
# ищем множество уникальных значений
def unique_numbers(numbers):
    unique_numbers = set(numbers)
    return(unique_numbers)

# ищем количество уникальных чисел в списке
def count_unique(numbers):
    unique = set(numbers)
    return len(unique)

# проверка на дубликаты
def has_duplicates(lts):
    return len(lts) != len(set(lts))

# подсчет уникальных посещенных страниц
def count_unique_pages(visited_pages):
    unique_pages = set(visited_pages)
    return len(unique_pages) 

# ищем уникальные слова в тексте(отсортированы по алфавиту и в нижнем регистре)
def unique_words(text):
    words = text.split()
    lower_words = [word.lower() for word in words]
    unique_words = set(lower_words)
    return sorted(unique_words)
# проверяем уникальность email
def unique_email(emails):
    unique_email = set(emails)
    return len(emails) == len(set(emails))

# пересечение, разности, симметрическе разности

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


# 🧩отношение между множествами
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


# 🧾Прикладные задачи(учёба, покупки)

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

# ищем общие товары в корзине
def common_products(cart1, cart2):
    set1 = set(cart1)
    set2 = set(cart2)
    return sorted(list(set1 & set2))

# ищем кто пропустил лекцию
def who_skipped(groups, present):
    set1 = set(groups)
    set2 = set(present)
    return  sorted(list(set1 - set2))