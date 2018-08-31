"""
2.2.0

Given a set of n students' examination marks (in the range 0 to 100) make a
count of the number of students that passed the examination. A pass is awarded
for all marks of 50 and above.
"""


def passcount1(marks, passmark=50):
    pass_count = 0
    for mark in marks:
        if mark >= passmark:
            pass_count += 1
    return pass_count


# Pythonic way 1
def passcount2(marks, passmark=50):
    return sum(1 for mark in marks if mark >= passmark)


# Pythonic way 2
def passcount3(marks, passmark=50):
    return len(filter(lambda mark: mark >= passmark, marks))


if __name__ == '__main__':
    assert passcount1([55, 42, 77, 63, 29, 57, 89]) == 5, "List of positive integers"
    assert passcount1([50, 50, 50, 50, 50]) == 5, "List of border values"
    assert passcount2([55, 42, 77, 63, 29, 57, 89]) == 5, "List of positive integers"
    assert passcount2([50, 50, 50, 50, 50]) == 5, "List of border values"
    assert passcount3([55, 42, 77, 63, 29, 57, 89]) == 5, "List of positive integers"
    assert passcount3([50, 50, 50, 50, 50]) == 5, "List of border values"
