from app import is_even

def test_even_number():
    assert is_even(4) == True

def test_odd_number():
    assert is_even(5) == False
