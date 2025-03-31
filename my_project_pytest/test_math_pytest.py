from math_pytest import (is_even, is_prime, filter_even, sum_even, square_all, is_divisible_by_5, remainder, is_multiple_of, is_between, is_even_and_gt_10, safe_divide, check_even_or_odd, round_if_not_integer, check_even_odd_pair)
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
