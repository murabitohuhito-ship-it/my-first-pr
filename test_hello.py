from hello import greet


def test_greet_with_name():
    assert greet("World") == "Hello, World!"


def test_greet_with_different_name():
    assert greet("Alice") == "Hello, Alice!"
