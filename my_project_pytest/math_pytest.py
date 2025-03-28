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