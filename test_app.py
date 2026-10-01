from app import add, multiply, greet


def test_add():
    assert add(2, 3) == 5


def test_multiply():
    assert multiply(4, 5) == 20


def test_greet():
    assert greet("Abdullah") == "Hello, Abdullah!"
