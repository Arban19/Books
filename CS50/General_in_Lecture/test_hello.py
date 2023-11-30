from hello import hello

def test_default():
    assert hello() == "Hello, World"

def test_argument():
    assert hello("David") == "Hello, David"

def test_hogwarts():
    for name in ["Harry","Hermoine","Ron"]:
        assert hello(name) == f"Hello, {name}"
