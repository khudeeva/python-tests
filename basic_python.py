# -*- coding: utf-8 -*-

# Переменная
name = "Anna"
age = 25
height = 1.68
is_student = True

print(name, age, height, is_student)

# Операторы
x = 10
y = 3

print(x + y)
print (x - y)
print(x * y)
print(x / y)
print(x // y)
print(x % y)
print(x ** y)

# Условные конструкции (if-elif-else)
age = 18

if age >= 18:
    print("Вы совершенолетний. ")
else:
    print("Вы еще ребенок. ")

# условные конструкции (много условий)
score = 75

if score >= 90:
    print("Отлично!")
elif score >= 70:
    print("Хорошо.")
elif score >= 50:
    print("Удовлетворительно. ")
else:
    print("Неудовлетворительно. ")

# Циклы (for, while)
fruits = ["Яблоко", "Банан", "Апельсин"]

for fruit in fruits:
    print(fruit)

# for + range()
for i in range(1, 6):
    print(i)

# while
x = 5

while x > 0:
    print(x)
    x -= 1

# списки (list)
numbers = [1, 2, 3, 4, 5]
print(numbers[0])
numbers.append(6)
numbers.remove(2)
print(numbers)

# словари (dict)
user = {"name": "Anna", "age": 25}
print(user["name"])
user["city"] = "Moscow"
print(user)

# Генераторы списков( List Comprehension)

# создаем список квадратов чисел от 1 до 5
squares = [x ** 2 for x in range(1, 6)]
print(squares)

# фильтруем четные числа
numbers = [1, 2, 3, 4, 5, 6]
even_number = [x for x in numbers if x % 2 == 0]
print(even_number)

# фильтруем нечетные числа
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
even_number = [x for x in numbers if x % 2 == 1]
print(even_number)

# фильтруем нечетные числа (используем range)
numbers = list(range(1, 22))
odd_numbers = [x for x in numbers if x % 2 == 1]
print(odd_numbers)

# фильтруем числа, которые делятся на 5
numbers = list(range(1, 51))
divisible_by_5 = [x for x in numbers if x % 5 == 0]
print(divisible_by_5)

# фильтрует числа, которые делятся на 3 и 7 одновременно
numbers = list(range(1, 101))
divisible_by_3_and_7 = [x for x in numbers if x % 3 == 0 and x % 7 == 0]
print(divisible_by_3_and_7)

# фильтруем числа, которые делятся на 4 или 9
numbers = list(range(1, 201))
divisible_by_4_or_9 = [x for x in numbers if x % 4 == 0 or x % 9 == 0]
print(divisible_by_4_or_9)

# фильтруем числа, которые делятся на 5 и не делятся на 10
number = list(range(1, 301))
divisible_by_5_not_10 = [x for x in numbers if x % 5 == 0 and x % 10 != 0]
print(divisible_by_5_not_10)

# фильтруем числа, которые делятся либо на 7, либо на 11, но не делятся на 3
number = list(range(1, 1001))
divisible_by_7_and_11_or_not_3 = [x for x in numbers if (x % 7 == 0 or x % 11 == 0) and x % 3 !=0]
print(divisible_by_7_and_11_or_not_3)

# фильтруем числа, которые делятся на 5 или 9, но не делятся одновременно на 4 и 6
number = list(range(1, 1001))
divisible_by_5_and_9_or_not_3_and_6 = [x for x in numbers if (x % 5 == 0 or x % 9 == 0) and not (x % 4 == 0 and x % 6 == 0)]
print(divisible_by_5_and_9_or_not_3_and_6)

# фильтруем числа, которые делятся на 7 или 13, но НЕ делятся ни на 5, ни на 11
number = list(range(1, 1001))
divisible_by_7_or_13_not_5_and_11 = [x for x in numbers if(x % 7 == 0 or x % 13 ==0) and not (x % 5 == 0 or x % 11 == 0)]
print(divisible_by_7_or_13_not_5_and_11)

# фильтруем числа, которые делятся на 4 ИЛИ 7, но НЕ делится на 5
numbers = list(range(1, 101))
divisible_4_or_7_not_5 = [x for x in numbers if (x % 4 == 0 or x % 7 == 0) and x % 5 != 0]
print(divisible_4_or_7_not_5)

# фильтруем строки по длине и наличию символов
words = ["привет", "дом", "здравствуй", "кот", "арбуз", "погода", "лес123", "ананас", "солнце"]
filtered_words = [word for word in words if len(word) > 5 and "а" in word and not any(char.isdigit() for char in word)]
print(filtered_words)

# фильтруем слова, которые начинаются на "с" или "п", оканчиваются на "а", не содержат букву "е"
words = ["собака", "природа", "погода", "работа", "семья", "персона", "панда"]

filtered_words_position = [
    word for word in words 
    if word.startswith(("с", "п")) and word.endswith("а") and "е" not in word
]
print(filtered_words_position)

# фильтруем слова, которые содержат "и", не содержат "а" и длина слова больше 5 символов
words = ["машина", "лист", "письмо", "игра", "коробка", "мечта", "виноград", "компьютер"]
filtered_words = [
    word for word in words 
    if "и" in word and len(word) > 5 and  "а" not in word
]
print(filtered_words)

# фильтруем слова, которые начинаются на "м" или "г", содержат "о", НЕ заканчивается на "а", длина больше 4
words = ["город", "мост", "гора", "молоко", "гриб", "погода", "мечта", "гром", "монитор"]
filtered_words = [
    word for word in words
    if word.startswith(("м", "г")) and "о" in word and not word.endswith("а") and len(word) > 4
]
print(filtered_words)

# фильтруем слова,которые НЕ содержат "р", начинаются на "п" или "в", заканчиваются на "а" или "о", длина не больше 7 символов
words = ["погода", "работа", "ваза", "ветер", "пламя", "вино", "поле", "волна"]
filtered_words = [
    word for word in words
    if not "р" in word 
    and word.startswith(("п", "в")) 
    and word.endswith(("а","о")) 
    and len(word) < 7
]
print(filtered_words)

# фильтруем слова, котрые содержат "с" или "д", НЕ содержат "я", длина от 5до 8 символов включительно
words = ["сосна", "дуб", "машина", "солнце", "груша", "дорога", "песок", "осень"]
filtered_words = [
    word for word in words
    if ("с" in word or "д" in word)
    and not word.endswith("я") 
    and  5 <= len(word) <= 8
]
print(filtered_words)

# фильтруем слова, котопые содержат либо "м", либо "г", НЕ содержит "е", заканчивается на "а" или "о", дина от 6 до 9 включительно
words = ["молоко", "гора", "мяч", "магнолия", "морковь", "гранат", "груша", "глобус"]
filtered_words = [
    word for word in words
    if ("м" in word or "г" in word)
    and not "е" in word
    and word.endswith(("а", "о"))
    and  6 <= len(word) <= 9
]
print(filtered_words)
# повторение 
# переменные и типы данных
name = "Ksenia"
age = 25
is_qa = True
print(name, type(age), is_qa)

username = "ksenia_k"
age = 25
is_active = True
print(type(name))
print(type(age))
print(type(is_active))

print("Типы переменных, person_profile")
first_name = "Ksenia"
age= 25
is_student = False
print(type(first_name))
print(type(age))
print(type(is_student))

# список(List)
cities = ["Perm", "Moscow", "Kazan", "Sochi", "Petersburg"]

print(cities)
print(cities[0])
print(cities[4])
print(len(cities))
print("Perm" in cities)

cities.append("Berlin")
cities.remove("Sochi")

print(cities)

# список языков
print("Список языков")
language = ["Python", "Russian", "English"]
print(len(language))
print(language[1])
print("English" in language)

print("Список QA языков, langs")
langs = ["Python", "SQL", "HTML"]
print(len(langs))
print("Python" in langs)
print(langs[2])
langs.append("CSS")
langs.remove("SQL")
print(langs)

print("\n five_cities")
five_cities = ["Perm", "Moscow", "Kazan", "Sochi", "Ekaterinburg"]
print(five_cities[0])
print(five_cities[4])
five_cities.append("Kaluga")
print("Moscow" in five_cities)
print(five_cities)

print("\n qa_list")
qa_list = ["Postman", "Selenium", "Allure"]
qa_list.append("JMeter")
qa_list.insert(1,"Pytest")
qa_list.remove("Allure")
print(qa_list)


# словарь(dict)
print("user")
user ={
    "name": "Ksenia",
    "age": 25,
    "city": "Perm",
    "is_qa": True
}
print(user)
print(user["name"])
user["city"] = "Moscow"
user["experience"] = 1
del user["is_qa"]
print(user)

print("user_profile")
user_profile = {
    "username": username,
    "age": age,
    "active": is_active,
    "skills": language
}
print(user_profile)
print(user_profile["skills"])
user_profile["location"] = "Russia"
del user_profile["age"]
print(user_profile)

print("user_data")
user_data = {
    "name": first_name,
    "age": age,
    "student": is_student,
    "skills": langs
    }
user_data["student"] = True
user_data["city"] = "Perm"
del user_data["age"]
print(user_data["skills"])
print(user_data)

print("\n my_profile")
my_profile = {
    "name": "Ksenia",
    "age": 25,
    "city": "Perm"
}
my_profile["city"] = "Ekaterinburg"
my_profile["is_qa"] = True
del my_profile["age"]
print(my_profile)

print("\n bug_info")
bug_info = {
    "id": "BUG-789",
    "status": "Open",
    "priority": "High"
}
bug_info["status"] = "Closed"
print(bug_info.keys())
print(bug_info.values())
print (bug_info)

# dict + list
print("\n personal_skills")
personal_skills = {
        "ksenia": ["Python", "SQL", "Selenium"],
        "dima": ["HTML", "CSS"],
        "anna": ["Postman", "Python"]
    }
    # выводим список всех пользователей
print(personal_skills.keys())
    # для каждого пользователя - выводим количество навыков
for name, skills in personal_skills.items():
    print(f"{name} знает: {len(skills)} навыков")
    # проверка, есть ли у кого-то навык Selenium, если есть - выводим имя
for name, skills in personal_skills.items():
    if "Selenium" in skills:
        print(f"{name} знает Selenium")

    # добавляем нового пользователя с новыми навыками
personal_skills["lena"] =  ["Java", "PostgreSQL"]
print(personal_skills)
    # удалим у "dima" навык "HTML"
if "HTML" in personal_skills["dima"]:
    personal_skills["dima"].remove("HTML")
    # выводим итоговый словарь
for name, skills in personal_skills.items():
    print(f"{name}: {skills}")

    # dict+list
print("\n qa_tasks")
qa_tasks = {
         "ksenia": ["login test", "form check"],
        "dima": ["API response", "button visibility"],
        "anna": ["page load", "layout check"]
    }
print(qa_tasks.keys())
for name, tasks in qa_tasks.items():
        print(f"{name} имеет: {len(tasks)} задач")
qa_tasks["lena"] = ["registration test"]
print(qa_tasks)

if "form check" in qa_tasks["ksenia"]:
        qa_tasks["ksenia"].remove("form check")
        print(qa_tasks)
for name, tasks in qa_tasks.items():
        print(f"{name}: {tasks}")

print("\n tasks")
tasks = {
    "ksenia": ["login test", "form check"],
    "dima": ["API response", "button visibility", "form check"],
    "anna": ["page load", "layout check", "form check"]
}
for name, task in tasks.items():
    if "form check" in task:
        print(f"{name} имеет задачу form check")

# ищем QA с максимальным количеством задач
max_user = ""
max_tasks = 0
for name, task in tasks.items():
    if len(task) > max_tasks:
        max_tasks = len(task)
        max_user = name
print(f"Больше всего задач у {max_user}: {tasks[max_user]}")

# удаляем form check  у всех, у кого она есть
for name, task in tasks.items():
    if "form check" in task:
        task.remove("form check")
      
for name, task in tasks.items():
      print(f"{name}: {task}")

# set
print("\n my_skills")
my_skills = {"Python", "SQL", "API", "Selenium", "Python", "SQL"}
print(set(my_skills))

print("\n names")
names = ["Ksenia", "Dima", "Anna", "Ksenia", "Anna"]
print(set(names))

print("\n total_skills, Общие навыки")
skills_ksenia = {"Python", "SQL", "API", "Postman"}
skills_dima = {"Java", "API", "SQL"}
set1 = set(skills_ksenia)
set2 = set(skills_dima)
print("Общие навыки:", set1&set2)
print("Навыки только у Ксении:", set1-set2)

print("\n Проверка наличия + add")
cities = {"Perm", "Moscow", "Kazan", "Sochi"}
if "Berlin" not in cities:
    cities.add("Berlin")
print(cities)

print("\n Подсчет уникальных букв")
word = "Автоматизация"
print(len(set(word)))

print("\n Проверка пересечений")
errors_qa = {"UI баг", "Кнопка не работает", "Орфография"}
errors_dev = {"500 ошибка", "Кнопка не работает", "Неверная логика"}
set1 = set(errors_qa)
set2 = set(errors_dev)
print("Общие ошибки:", set1&set2)
print("Ошибки только у QA", set1-set2)

print("\n Обновление навыков")
skills = {"Python", "SQL"}
if not "Postman" in skills:
    skills.add("Postman")
if "SQL" in skills:
    skills.discard("SQL")
print("Сотрудник имеет навыки:", skills)

print("\n qa_language")
qa_language = set()
qa_language.add("Python")
qa_language.add("Postman")
qa_language.add("Selenium")
qa_language.discard("Postman")
if "JMeter" in qa_language:
    print("Есть JMeter")
else:
    print("JMeter отсутствует")
print(qa_language)



print("Условные конструкции if/else")
age = 21
is_qa = True
if age >= 18 and is_qa:
    print("Добро пожаловать, QA!")
else:
    print("Доступ ограничен")

print("Проверка балов if/elif/else")
score = 78
if score >= 90:
    print("Отлично")
elif score >=75:
    print("Хорошо")
elif score >=60:
    print("Удовлетворительно")
else:
    print("Неудовлетворительно")

print("Цикл for + range()")
for i in range(1, 6):
    print(i)

print("Выводим только чётные числа")
for i in range(2, 11):
    if i % 2 == 0:
     print(i)
    
print("Цикл for по списку языков")
langs = ["Python", "SQL","HTML", "CSS"]
for lang in langs:
    print(lang)
print(len(langs))
print("JavaScript"in langs)

# обработка ошибок(try/except)
a = 10
b = 0
try:
    x = a / b
    print(f"Результат: {x}")
except ZeroDivisionError:
    print("Ошибка: деление на ноль!")

print("\n Обработка ошибки по наличию ключа")
user = {
    "name": "Ksenia",
    "city": "Perm"
}
try:
        print(f"Возраст пользователя: {user['age']}")
except KeyError:
    print("Ключ 'age' не найден")

# кортеж(tuple)
print("\n Создаем доступ к элементам")
prof_name = ("Marina", 28, "QA")
print(prof_name[0])
print(prof_name[2])
print(len(prof_name))

print("\n Проверка наличия значений в кортеже")
qa_stack = ("Python", "Selenium", "PyTest", "Postman", "SQL")
print("Selenium" in qa_stack)
print("Postman" in qa_stack)
print(qa_stack.index("Postman"))
print(qa_stack.count("Python"))

print("\n Обработка ошибок с .index()")
tools = ("Postman", "JMeter", "Selenium", "Allure")
tool_to_check = "Pytest"
try:
    index = tools.index(tool_to_check)
    print(f"Инструмент найденю Индекс: {index}")
except ValueError:
    print("Инструмент не найден")

print("\n Обработка ошибок finally")
num1 = "abc"
num2 = 0
try:
    x = int(num1) # тут ошибка, идет сразу в except
    y = 10 / num2 # поэтому это не выполянется!
except ValueError:
    print("Ошибка преобразования")
except ZeroDivisionError:
    print("Ошибка деления на ноль")
finally:
    print("Завершено")

print("\n Работа с файлом и try/except/else/finally")
file_name = "testdata.txt"
try:
    f = open(file_name, "r")
    line = f.readline()
except FileNotFoundError:
    print("Файл не найден")
else:
    print("Строка содержит:", line)
finally:
   print("Завершено")

print("\n Кортеж о баге")
bug_info = ("BUG-123", "Open", "Critical")
print(bug_info[1])
print(bug_info[2])

print("\n try/except")
number = "10a"
divisor = 0
try:
    x = int(number)
    y = 100/divisor
except ValueError:
    print("Ошибка преобразования")
except ZeroDivisionError:
    print("Ошибка деления на ноль")
finally:
    print("Проверка завершена")
