numbers = [4, 8, 15, 16, 23, 42]
print(numbers)
print(len(numbers))
result = 0
for number in numbers:
    if number % 2 == 0:
        square_of_number = number * number
        result += square_of_number
print(f"result: {result}")