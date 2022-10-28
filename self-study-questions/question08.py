"""
Read an integer from the keyboard.
Make sure that the number is positive, three-digit, and the digits are different
"""
number = int(input("Enter a positive integer: ").strip())
if number < 100 or number > 999:
    print("This is not a three-digit number")
else:
    leastSignificantDigit = number % 10
    centerDigit = (number // 10) % 10
    mostSignificantDigit = number // 100
    if leastSignificantDigit == centerDigit or mostSignificantDigit == centerDigit or leastSignificantDigit == mostSignificantDigit:
        print("Some digits are equal")
    else:
        print(f"{number} is a positive three-digit number.")
