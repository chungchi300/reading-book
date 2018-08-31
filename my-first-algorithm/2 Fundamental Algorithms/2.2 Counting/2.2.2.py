"""
2.2.2

Design an algorithm that reads a list of numbers and makes a count of the number
of negatives and the number of non-negative members in the set.
"""


def counter(list):
    negative = 0
    non_negative = 0
    for number in list:
        if number < 0:
            negative += 1
        else:
            non_negative += 1
    return negative, non_negative


# Pythonic way 1
def partition_count1(list, pivot=0):
    left_count = sum(1 for number in list if number < pivot)
    right_count = len(list) - left_count
    return left_count, right_count


# Pythonic way 2
def partition_count2(list, pivot=0):
    left_count = len(filter(lambda number: number < pivot, list))
    right_count = len(list) - left_count
    return left_count, right_count


if __name__ == '__main__':
    assert counter([-5, -3, -1, 0, 2, 4, 6]) == (3, 4), "list of negatives and non-negatives"
    assert partition_count1([-5, -3, -1, 0, 2, 4, 6]) == (3, 4), "list of negatives and non-negatives"
    assert partition_count2([-5, -3, -1, 0, 2, 4, 6]) == (3, 4), "list of negatives and non-negatives"
