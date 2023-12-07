import pytest

from bank import value

def test_basic():
    assert value("hey") == "$20"
    assert value("Hello") == "$0"
    assert value("Yolo") == "$100"
    assert value("") == "$100"
    assert value("        Yello           ") == "$100"
