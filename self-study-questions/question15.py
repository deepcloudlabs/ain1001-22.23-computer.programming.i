"""
Find the zero crossings of the following list:
numbers = [12, 15, 7, 3, -1, -3 ,-7, -2, 3, 4, -2, -10]
                     /\              /\    /\
                     |               |     |
     zero crossings__|_______________|_____|
"""
numbers = [12, 15, 7, 3, -1, -3, -7, -2, 3, 4, -2, -10]
for i in range(1, len(numbers)):
    if numbers[i - 1] * numbers[i] < 0:
        print(f"Zero crossings at {i}: {numbers[i - 1]}, {numbers[i]}")
