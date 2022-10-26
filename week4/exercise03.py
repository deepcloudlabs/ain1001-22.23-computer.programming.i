number = int(input("Enter an integer: "))
steps = 0
while number > 1:
    if number % 2 == 0:
        number = number // 2
    else:
        number = 3 * number + 1
    steps += 1
print(f"It takes {steps} steps to converge to 1")
