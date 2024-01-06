import pytest

from plates import is_valid

def main():
    test_valid_plate()
    test_invalid_length()
    test_invalid_start_with_number()
    test_invalid_contains_space()
    test_invalid_contains_period()
    test_invalid_ends_with_letter()
    test_valid_ends_with_number()

def test_valid_plate():
    assert is_valid("CS50") == True
    assert is_valid("CS") == True
    assert is_valid("11") == False
    assert is_valid("ABCDEF") == True
    assert is_valid("ABCDEFGH") == False
    assert is_valid("ABC012") == False
    assert is_valid("ABC102") == True

def test_invalid_length():
    assert is_valid("CS") == True

def test_invalid_start_with_number():
    assert is_valid("   12CS") == False

def test_invalid_contains_space():
    assert is_valid("CS 50") == False

def test_invalid_contains_period():
    assert is_valid("CS.50") == False

def test_invalid_ends_with_letter():
    assert is_valid("CS501J") == False

def test_valid_ends_with_number():
    assert is_valid("CS5010") == True
