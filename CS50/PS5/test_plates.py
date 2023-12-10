from plates import is_valid

def test_valid_plate():
    assert is_valid("CS50") == True

def test_invalid_length():
    assert is_valid("CS") == True

def test_invalid_start_with_number():
    assert is_valid("12CS") == False

def test_invalid_contains_space():
    assert is_valid("CS 50") == False

def test_invalid_contains_period():
    assert is_valid("CS.50") == False

def test_invalid_ends_with_letter():
    assert is_valid("CS501J") == False

def test_valid_ends_with_number():
    assert is_valid("CS5010") == True
