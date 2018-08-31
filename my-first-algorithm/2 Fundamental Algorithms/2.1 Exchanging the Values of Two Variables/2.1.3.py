"""
2.1.2

Design an algorithm that makes the following exchanges:
                +-> a -> b -> c -> d +
                |                    |
                +--------------------+
"""


def quadruple_cyclic_exchange(a, b, c, d):
    t = a
    a = d
    d = c
    c = b
    b = t
    return a, b, c, d


if __name__ == '__main__':
    assert quadruple_cyclic_exchange(10, 20, 30, 40) == (40, 10, 20, 30), "All positive values"
    assert quadruple_cyclic_exchange(-10, -20, -30, -40) == (-40, -10, -20, -30), "All negative values"
    assert quadruple_cyclic_exchange(10, 10, 10, 10) == (10, 10, 10, 10), "All same values"
