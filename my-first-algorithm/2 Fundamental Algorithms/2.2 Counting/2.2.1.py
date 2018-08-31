"""
2.2.1

Modify the algorithm above so that marks are read until and end-of-file is
encountered. For this set of marks determine the total number of marks, the
number of passes, and the percentage pass rate.
"""


def passcount1(file, passmark=50):
    total_count = 0
    pass_count = 0
    with open(file) as f:
        for line in f.readlines():
            total_count += 1
            if int(line) >= passmark:
                pass_count += 1
    return total_count, pass_count, pass_count * 100.0 / total_count


# Pythonic way 1
def passcount2(file, passmark=50):
    marks = map(int, open(file).read().splitlines())
    pass_count = sum(1 for mark in marks if mark >= passmark)
    return len(marks), pass_count, pass_count * 100.0 / len(marks)


# Pythonic way 2
def passcount3(file, passmark=50):
    marks = map(int, open(file).read().splitlines())
    pass_marks = filter(lambda mark: mark >= passmark, marks)
    return len(marks), len(pass_marks), len(pass_marks) * 100.0 / len(marks)


if __name__ == '__main__':
    assert passcount1('2.2.1.1.test') == (100, 55, 55.0), "100 integers"
    assert passcount2('2.2.1.1.test') == (100, 55, 55.0), "100 integers"
    assert passcount3('2.2.1.1.test') == (100, 55, 55.0), "100 integers"
