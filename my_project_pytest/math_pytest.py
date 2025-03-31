#  проверка четности числа
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

# возвращаем список только четных чисел
def filter_even(numbers):
    return [x for x in numbers if x % 2 == 0]

# возвращаем сумму всез четных чисел из списка
def sum_even(numbers):
    return sum(x for x in numbers if x % 2 == 0)


# возвращаем список, где каждое число возведено в квадрат
def square_all(numbers):
    return [x ** 2 for x in numbers]

# проверка на делимость на 5
def is_divisible_by_5(n):
    return n % 5 == 0

# возврат остатка от деления
def remainder(a, b):
    return a % b

# проверка кратности числа
def is_multiple_of(a, b): 
    if a % b == 0:
        return  True  # либо return a % b == 0
    else:
        return False

# проверяем находится ли число между low, high
def is_between(n, low, high):
    return low < n <  high

# проверяем четность числа + больше 10
def is_even_and_gt_10(n):
    return n % 2 == 0 and n > 10

# делим a/b, если b=0 - возвращаем ошибку, если после деления целое число - Int, иначе float
def safe_divide(a, b):
    if b == 0:
        return "Деление на ноль невозможно"
    else:
        result = a / b
        if result.is_integer():
                return int(result)
        else:
                return result
# вернуть строку четное или нечетное (+ тернарный оператор)
def check_even_or_odd(n):
    return "Чётное" if n % 2 == 0 else "Нечётное"

# если целое число - округляем его, иначе возвращаем int
def round_if_not_integer(n):
    return int(round(n)) if n.is_integer() else int(n)

# обрабатываем 2 числа и возвращаем строку
def check_even_odd_pair(a, b):
     if a % 2 == 0 and b % 2 == 0:
        return "Оба чётные"
     elif a % 2 == 1 and b % 2 == 1:
        return "Оба нечётные"
     else: 
        return "Разные" 





