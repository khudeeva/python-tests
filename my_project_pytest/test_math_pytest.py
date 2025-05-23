from math_pytest import (is_even, is_prime, filter_even, sum_even, square_all, is_divisible_by_5, remainder, is_multiple_of, is_between, is_even_and_gt_10, safe_divide, check_even_or_odd, round_if_not_integer, check_even_odd_pair, even_or_odd, temperature_status, grade_category, password_strength, number_list, word_list, users, user_settings, number_data, numbers, is_even_practice,is_divisible_practice, get_max, sum_list, average_practice,multiply_list_practice, find_min_max, divide, square, add, compare_number, divide_with_raise, safe_int, safe_divide_zero, parse_int_list, divide_raise, double, is_even_example, is_even_save, divide_with_error, safe_divide_with_raise, is_prime_example, number_is_even)
import pytest
def test_even_number():
    assert is_even(4) == True
def test_odd_number():
    assert is_even(5) == False

def test_prime_number():
    assert is_prime(7) == True
def test_small_number():
    assert is_prime(1) == False
def test_negative_number():
    assert is_prime(-3) == False
def test_odd_number():
    assert is_prime(8) == False
def test_difficult_numbers():
    assert is_prime(22) == False

def test_filter_even_246():
    assert filter_even([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
def test_filter_even_none():
    assert filter_even([3, 5, 7]) == []
def test_filter_even_empty():
    assert filter_even([]) == []

def test_sum_even_all():
    assert sum_even([1, 2, 3, 4, 5, 6]) == 12
def test_sum_even_none():
    assert sum_even([1, 3, 5]) == 0
def test_sum_even_empty():
    assert sum_even([]) == 0

def test_square_all_simple():
    assert square_all([1, 2, 3]) == [1, 4, 9]
def test_square_all_negative():
    assert square_all([-2, -4, - 5]) == [4, 16, 25]
def test_square_all_with_zero():
    assert square_all([2, 0, 5]) == [4, 0, 25]
def test_square_all_none():
    assert square_all([]) == []

def test_is_divisible_by_5_10():
    assert is_divisible_by_5(10) == True
def test_is_divisible_by_5_0():
    assert is_divisible_by_5(0) == True
def test_is_divisible_by_5_3():
    assert is_divisible_by_5(3) == False
def test_is_divisible_by_5_negative_5():
    assert is_divisible_by_5(-5) == True


def test_remainder_10_by_3():
    assert remainder(10, 3) == 1
def test_remainder_2_by_2():
    assert remainder(2, 2) == 0
def test_remainder_7_by_4():
    assert remainder(7, 4) == 3

def test_is_multiply_of10_by_2():
    assert is_multiple_of(10, 2) == True
def test_is_multiple_of_9_by_3():
    assert is_multiple_of(9, 3) == True
def test_is_multiple_of_7_by_4():
    assert is_multiple_of(7, 4) == False
def test_is_multople_of_0_by_5():
    assert is_multiple_of(0, 5) == True
def test_is_multiple_of_5_by_0():
    with pytest.raises(ZeroDivisionError):
        is_multiple_of(5, 0)

def test_is_between_5():
    assert is_between(5, 1, 10) == True
def test_is_between_10():
    assert is_between(10, 1, 10) == False
def test_is_between_1():
    assert is_between(1, 1, 10) == False
def test_is_between_7():
    assert is_between(7, 7, 8) == False
def test_is_between_negative():
    assert is_between(-3, -5, -1) == True

def test_is_even_and_gt_10():
    assert is_even_and_gt_10(20) == True
def test_is_even_and_gt_10_21():
    assert is_even_and_gt_10(21) == False
def test_is_even_and_gt_10_8():
    assert is_even_and_gt_10(8) == False
def test_is_even_and_gt_10_10():
    assert is_even_and_gt_10(10) == False
def test_is_even_and_gt_10_negative_even():
    assert is_even_and_gt_10(-20) == False
def test_is_even_and_gt_10_zero():
    assert is_even_and_gt_10(0) == False

def test_safe_divided_int():
    assert safe_divide(10, 5) == 2
def test_safe_divided_float():
    assert safe_divide(7, 2) == 3.5
def test_save_divided_zero():
    assert safe_divide(5, 0) == "Деление на ноль невозможно"
def test_safe_divide_negative():
    assert safe_divide(-10, 2) == -5
def test_safe_divide_float_result():
    assert safe_divide(5, 4) == 1.25

def test_check_even_or_odd_even():
    assert check_even_or_odd(4) == "Чётное"
def test_check_even_or_odd_odd():
    assert check_even_or_odd(7) == "Нечётное"
def test_check_even_or_odd_zero():
    assert check_even_or_odd(0) == "Чётное"
def test_check_even_or_odd_negative_odd():
    assert check_even_or_odd(-5) == "Нечётное"
def test_check_even_or_odd_negative_even():
    assert check_even_or_odd(-4) == "Чётное"

def test_round_if_not_integer_int_like_float():
    assert round_if_not_integer(5.0) == 5
def test_round_if_not_integer_float():
    assert round_if_not_integer(5.7) == 5
def test_round_if_not_integer_negative_int_like_float():
    assert round_if_not_integer(-3.0) == -3
def test_round_if_not_integer_negative_float():
    assert round_if_not_integer(-4.9) == -4


def test_check_even_odd_pair_even():
    assert check_even_odd_pair(2, 4) == "Оба чётные"
def test_check_even_odd_pair_odd():
    assert check_even_odd_pair(3, 5) == "Оба нечётные"
def test_check_even_odd_pair_different():
    assert check_even_odd_pair(7, 10) == "Разные"
def test_check_even_odd_pair_negative_even():
    assert check_even_odd_pair(-4, -8) == "Оба чётные"
def test_check_even_odd_pair_negative_odd():
    assert check_even_odd_pair(-7, -11) == "Оба нечётные"
def test_check_even_odd_pair_with_zero():
    assert check_even_odd_pair(3, 0) == "Разные"

# ПАРАМЕТРИЗАЦИЯ ТЕСТОВ
@pytest.mark.parametrize("input, expected", [
    (2, "Чётное"),
    (3, "Нечётное"),
    (0, "Чётное"),
    (-1, "Нечётное")
])
def test_even_or_odd(input, expected):
    assert even_or_odd(input) == expected

@pytest.mark.parametrize("input, expected", [
    (7, "Холодно"),
    (16, "Тепло"),
    (25, "Тепло"),
    (30, "Жарко"),
    (0, "Холодно"),
    (-1, "Холодно")
])
def test_temperature_status(input, expected):
    assert temperature_status(input) == expected

@pytest.mark.parametrize("input, expected",[
    (100, "Отлично"),
    (95, "Отлично"),
    (80, "Хорошо"),
    (70, "Удовлетворительно"),
    (60, "Удовлетворительно"),
    (50, "Неудовлетворительно"),
    (0, "Неудовлетворительно")
])
def test_grade_category(input, expected):
    assert grade_category(input) == expected

@pytest.mark.parametrize("input, expected",[
    ("abcd", "Слабый"),
    ("abckdh", "Средний"),
    ("jfosmkcy", "Средний"),
    ("djcomeunbds", "Сильный"),
    ("", "Слабый")
])
def test_password_strength(input, expected):
    assert password_strength(input) == expected

# ФИКСТУРА
# фикстура для списка чисел
def test_sum(number_list):
    assert sum(number_list) == 21
def test_max_value(number_list):
    assert max(number_list) == 6
def test_length(number_list):
    assert len(number_list) == 6

# фикстура для строк
def test_word_count(word_list):
    assert len(word_list) == 4 # количество слов
def test_longest_word_length(word_list):
    assert max(len(word) for word in word_list) == 6 # длина самого длинного слова
def test_all_lowercase(word_list):
    assert all(word[0].islower() for word in word_list) # все начинаются со строчной буквы

# фикструра словарь с пользователями
def test_user_count(users):
    assert len(users) == 3 # количество
def test_active_users(users):
    active = [name for name, info in users.items() if info["active"]]
    assert active == ["Анна", "Мария"]
def test_average_age(users):
    age = [info["age"] for info in users.values()]
    assert sum(age) / len(age) == 25.666666666666668

# фикстура настройки пользователя
def test_theme_setting(user_settings):
    assert user_settings["theme"] == "dark"
def test_language_settings(user_settings):
    assert user_settings["language"] == "ru"
def test_notification_settings(user_settings):
    assert user_settings["notifications"] == True

# фикстура числовой набор
def test_max_number(number_data):
    assert max(number_data) == 60
def test_min_number(number_data):
    assert min(number_data) == 8
def test_even_count(number_data):
    evens = [n for n in number_data if n % 2 == 0]
    assert len(evens) == 3
def test_sum_range(number_data):
    total = sum(number_data)
    assert 100 <= total <= 200 #сумма находится в пределах

# фикстура 2 числа
def test_sum(numbers):
    a, b = numbers
    assert a + b == 9
def test_diff(numbers):
    a, b = numbers
    assert a -b == 3
def test_multiply(numbers):
    a, b = numbers
    assert a * b == 18

# ПОВТОРЕНИЕ
def test_is_even_practice():
    assert is_even_practice(4) == True
    assert is_even_practice(7) == False
    assert is_even_practice(0) == True
    assert is_even_practice(-2) == True
    assert is_even_practice(-11)== False

def test_is_divisible_practice():
    assert is_divisible_practice(10, 2) == True
    assert is_divisible_practice(7, 3) == False
    assert is_divisible_practice(5, 0) == False
    assert is_divisible_practice(0, 5) == True
    assert is_divisible_practice(12, 6) == True

def test_get_max():
    assert get_max(5, 10) == 10
    assert get_max(7, 3) == 7
    assert get_max(-1, -5) == -1
    assert get_max(0, 0) == 0

def test_sum_list():
    assert sum_list([1, 2, 3]) == 6
    assert sum_list([0, -5, 10]) == 5
    assert sum_list([]) == 0

def test_average_practice():
    assert average_practice([2, 4, 6]) == 4.0
    assert average_practice([10]) == 10.0
    assert average_practice([-2, -4, -6]) == -4.0
    assert average_practice([]) == 0

def test_multiply_list_practice():
    assert multiply_list_practice([1, 2, 3, 4]) == 24
    assert multiply_list_practice([10]) == 10
    assert multiply_list_practice([]) == 1
    assert multiply_list_practice([5, 0, 7]) == 0

def test_find_min_max():
    assert find_min_max([1, 5, 3, 0]) == (0, 5)
    assert find_min_max([-10, -5, 0]) == (-10, 0)
    assert find_min_max([7]) == (7, 7)
    assert find_min_max([]) == None

# ПОВТОРЕНИЕ
@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (9, 3, 3),
    (8, 4, 2),
])
def test_divide(a, b, expected):
    assert divide(a, b) == expected

@pytest.mark.parametrize("n, expected", [
    (2, 4),
    (3, 9), 
    (5, 25)
])
def test_square(n, expected):
    assert square(n) == expected

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (4, 0, 4),
    (-1, -2, -3)
])
def test_add(a, b, expected):
    assert add(a, b) == expected 

@pytest.mark.parametrize("a, b, expected", [
    (10, 9, "greater"),
    (-1, -3, "greater"),
    (1, 2, "less"),
    (-10, -5, "less"),
    (4, 4, "equal")
])
def test_compare_number(a, b, expected):
    assert compare_number(a, b) == expected

@pytest.mark.parametrize("a, b, expected, expect_error",[
    (10, 5, 2, False),
    (6, 3, 2, False),
    (5, 0, None, True)
])
def test_divide_with_raise(a, b, expected, expect_error):
    if expect_error:
        with pytest.raises(ValueError):
            divide_with_raise(a, b)
    else:
        assert divide_with_raise(a, b) == expected

def test_safe_int():
    value = "abc"
    with pytest.raises(ValueError):
        safe_int(value)

def test_safe_divide_zero():
    a = 10
    b = 0
    with pytest.raises(ZeroDivisionError):
        safe_divide_zero(a, b)

def test_parse_not_int_list():
    lst = ["1", "2", "abc", "4"]
    with pytest.raises(ValueError):
        parse_int_list(lst)

def test_parse_int_list():
    lst = ["1", "2", "3", "4"]
    assert parse_int_list(lst)

@pytest.mark.parametrize("a, b, expected, expect_error",[
    (10, 2, 5, False),
    (9, 3, 3, False),
    (5, 0, None, True)
])
def test_divide_raise(a, b, expected, expect_error):
    if expect_error:
        with pytest.raises(ZeroDivisionError):
            divide_raise(a, b)
    else:
        assert divide_raise(a, b) == expected

@pytest.fixture
def user_name_double():
    return "Ksenia"
@pytest.mark.parametrize("x, expected", [
    (2, 4),
    (5, 25),
    (10, 100)
    ])
def test_double(x, expected, user_name_double):
    assert double(x) == expected
    print(f"{user_name_double} возводит {x} в степень")

@pytest.mark.parametrize("num, expected", [
    (2, True),
    (5, False),
    (10, True),
    (13, False)
]) 
def test_is_even_example(num, expected):
    assert is_even_example(num) == expected

@pytest.mark.parametrize("num, expected, expect_error", [
    (2, True, False),
    (3, False, False),
    ("4", None, True),
    (None, None, True),
    ([], None, True)
])
def test_is_even_save(num, expected, expect_error):
    if expect_error:
        with pytest.raises(TypeError):
            is_even_save(num)
    else:
        assert is_even_save(num) == expected

@pytest.mark.parametrize("a, b, expected, expect_error", [
    (6, 2, 3, False),
    (5, 0, None, True),
    (2, 2, 1, False)
])
def test_divide_with_error(a, b, expected, expect_error):
    if expect_error:
        with pytest.raises(ZeroDivisionError):
            divide_with_error(a, b)
    else:
        assert divide_with_error(a, b) == expected
    

@pytest.mark.parametrize("a, b, expected, error_type", [
    (10, 2, 5.0, None),
    (8, 0, None, "zero"),
    (-2, 2, None, "value"),
    (6, 3, 2.0, None)
])
def test_safe_divide_with_raise(a, b, expected, error_type):
    if error_type == "zero":
        with pytest.raises(ZeroDivisionError) as exc:
            safe_divide_with_raise(a, b)
        assert "на 0" in str(exc.value)
    elif error_type == "value":
        with pytest.raises(ValueError) as exc:
            safe_divide_with_raise(a, b)
        assert "положительными" in str(exc.value)
    else:
        assert safe_divide_with_raise(a, b) == expected

def test_is_prime_example():
    assert is_prime_example(7) == True
    assert is_prime_example(2) == True
    assert is_prime_example(4) == False

@pytest.mark.parametrize("n, expected",[
      (2, True),
      (4, True),
      (5, False),
      (7, False),
      (8, True)                   
])
def test_number_is_even(n, expected):
    assert number_is_even(n) == expected