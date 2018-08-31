"""
2.1.2

Design an algorithm that makes the following exchanges:
                +-> a -> b -> c +
                |               |
                +---------------+
The arrow indicates that b is to assume the value of a, c the
value of b, and so on.
"""


def triple_cyclic_exchange(a, b, c):
    t = a
    a = c
    c = b
    b = t
    return a, b, c


if __name__ == '__main__':
    assert triple_cyclic_exchange(10, 20, 30) == (30, 10, 20), "All positive values"
    assert triple_cyclic_exchange(-10, -20, -30) == (-30, -10, -20), "All negative values"
    assert triple_cyclic_exchange(10, 10, 10) == (10, 10, 10), "All same values"
    assert triple_cyclic_exchange(0, 10, 20) == (20, 0, 10), "Zero included"
