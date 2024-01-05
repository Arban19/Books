import pytest

from refueling import convert, gauge

def main():
    test_correct_input()
    test_zero_division()
    test_value_error()

def test_convert():
    assert convert("1/4") == 25
    assert convert("1/100") == 1
    assert convert("99/100") == 99

def test_gauge():
    assert gauge(25) == "25%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        assert convert("1/0")

def test_value_error():
    with pytest.raises(ValueError):
        assert convert("cat/dog")
