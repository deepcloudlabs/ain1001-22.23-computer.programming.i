"""
Take two integers from the user and tell the relation between them
"""
num1 = int(input("Enter an integer: ").strip())
num2 = int(input("Enter an integer: ").strip())
if num1 == num2:
    print(f"{num1} is equal to {num2}")
elif num1 != num2:
    print(f"{num1} is NOT equal to {num2}")

if num1 < num2:
    print(f"{num1} is less than {num2}")
elif num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 <= num2:
    print(f"{num1} is less than or equal to {num2}")
elif num1 >= num2:
    print(f"{num1} is greater than or equal to {num2}")
