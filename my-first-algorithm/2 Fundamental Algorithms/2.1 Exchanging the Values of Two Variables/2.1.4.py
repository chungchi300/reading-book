"""
2.1.4

Given two variable of integer type a and b, exchange their values without using
a third temporary variable.
"""


# Pythonic way
def exchange1(a, b):
    a, b = b, a
    return a, b


# Using + and -
def exchange2(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b


# using * and /
def exchange3(a, b):
    a = a * b
    b = a / b
    a = a / b
    return a, b


# using ^
def exchange4(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b


if __name__ == '__main__':
    assert exchange1(10, 20) == (20, 10), "Two positive values"
    assert exchange2(10, 20) == (20, 10), "Two positive values"
    assert exchange3(10, 20) == (20, 10), "Two positive values"
    assert exchange4(10, 20) == (20, 10), "Two positive values"
