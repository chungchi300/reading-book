"""
2.1.0

Given two variables, a and b, exchange the values assigned to them.
"""


def exchange(a, b):
    t = a
    a = b
    b = t
    return a, b


if __name__ == '__main__':
    assert exchange(10, 20) == (20, 10), "Two positive values"
    assert exchange(-10, 20) == (20, -10), "One positive value and one negative value"
    assert exchange(-10, -20) == (-20, -10), "Two negative values"
    assert exchange(0, 10) == (10, 0), "One value is zero"
    assert exchange(10, 10) == (10, 10), "Same values"
