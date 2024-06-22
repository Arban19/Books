import pytest

from bank import value

def test_basic():
    assert value("hey") == 20
    assert value("Hello") == 0

def test_diff():
    assert value("Yolo") == 100

def test_rand():
    assert value("        Yello           ") == 100
    assert value("") == 100
