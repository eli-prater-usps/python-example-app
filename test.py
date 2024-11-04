from python_example.start import add_numbers, subtract_numbers, multiply_numbers, divide_numbers

def test_add():
    assert add_numbers(5, 3) == 8
    assert add_numbers(5, -3) == 2

def test_subtract():
    assert subtract_numbers(5, 3) == 2
    assert subtract_numbers(5, -3) == 8

def test_multiply():
    assert multiply_numbers(5, 3) == 15
    assert multiply_numbers(5, -3) == -15

def test_divide():
    assert divide_numbers(6, 3) == 2
    assert divide_numbers(10, 2) == 5