"""
A Smith number is a composite number where the sum of whose digits is
the sum of the digits of its prime factors (excluding 1).

Write C++ code to print Smith numbers between 2 and 1000.

Example:
    666 = 2×3×3×37
    6 + 6 + 6 = 2 + 3 + 3 + 37
    6 + 6 + 6 = 2 + 3 + 3 + 3 + 7
         18   =    18
"""
for number in range(2, 1000):
    sum_of_digits = 0
    temp = number
    while temp > 0:
        sum_of_digits += temp % 10
        temp = temp // 10
    divisor = 2
    temp = number
    sum_of_divisors = 0
    while temp > 1:
        sum_of_divisor_digits = divisor
        if divisor > 9:
            sum_of_divisor_digits = 0
            temp_of_divisor = divisor
            while temp_of_divisor > 0:
                sum_of_divisor_digits += temp_of_divisor % 10
                temp_of_divisor = temp_of_divisor // 10
        while temp % divisor == 0:
            sum_of_divisors += sum_of_divisor_digits
            temp = temp // divisor
        divisor += 1
    if sum_of_digits == sum_of_divisors:
        print(f"{number:4} {sum_of_digits:6} {sum_of_divisors:6}")
