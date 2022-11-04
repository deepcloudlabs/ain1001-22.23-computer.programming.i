from random import randint


def create_digit(lower=0, upper=9):
    global x
    x = x + 1
    return randint(lower, upper)


def includes(numbers, element):
    for number in numbers:
        if number == element:
            return True
    return False


def create_secret(numberOfDigits=3):
    digits = []
    digits.append(create_digit(1, 9))
    while len(digits) < numberOfDigits:
        candidate = create_digit(0, 9)
        if not includes(digits, candidate):
            digits.append(candidate)
    secret = 0
    for digit in digits:
        secret = 10 * secret + digit
    return secret


def evaluate_move(secret, guess):
    # TODO: implement the function
    pass
