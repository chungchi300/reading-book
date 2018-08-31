"""
2.2.3

You are given the problem described above. However, assume that your program is
to start out with the variable count initialized to the total number of students
n. On termination, the value of count should again represent the number of
students that passed the examination. If there were more passes than fails why
would this implementation be better than the original one?
"""


def passcount(marks, passmark=50):
    pass_count = len(marks)
    for mark in marks:
        if mark < passmark:
            pass_count -= 1
    return pass_count


if __name__ == '__main__':
    assert passcount([55, 42, 77, 63, 29, 57, 89]) == 5, "List of positive integers"
    assert passcount([50, 50, 50, 50, 50]) == 5, "List of border values"
