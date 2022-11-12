def take_sum(nums):  # pure function
    result = 0
    for n in nums:
        result += n
    return result


def is_odd(m):  # pure function
    return m % 2 == 1


def is_even(m):  # pure function
    return m % 2 == 0


def count(nums, criteria):  # higher-order function
    counter = 0
    for num in nums:
        if criteria(num):
            counter += 1
    return counter


def to_cube(n):
    return n * n * n
