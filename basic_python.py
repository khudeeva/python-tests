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