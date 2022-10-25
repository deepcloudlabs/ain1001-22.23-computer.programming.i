for number in range(6, 1000000):
    accumulator = 1
    for divisor in range(2, number // 2 + 1):
        if number % divisor == 0:
            accumulator += divisor
    if accumulator == number:
        print(f"{number} is a perfect number")
        print("{} is a perfect number".format(number))
