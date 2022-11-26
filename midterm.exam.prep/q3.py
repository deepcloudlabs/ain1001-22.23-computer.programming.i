x = int(input("Enter an integer: "))
sum = 0
n = 0
while True:
    odd = 2 * n + 1
    sum += odd
    if x < sum:
        break
    n += 1
print(f"The quare root of {x} is {n}.")
