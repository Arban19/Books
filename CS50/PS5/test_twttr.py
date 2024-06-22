import pytest

from twttr import shorten

def test_basic():
    assert shorten("Arsenal") == "rsnl"
    assert shorten("Hello") == "Hll"
    assert shorten("Python") == "Pythn"

def test_alphanum():
    assert shorten("Testing123") == "Tstng123"

def test_special_cases():
    assert shorten("!@#$%^") == "!@#$%^"

def test_all_vowels():
    assert shorten("aeiouAEIOU") == ""

def test_no_vowels():
    assert shorten("rhythm") == "rhythm"
