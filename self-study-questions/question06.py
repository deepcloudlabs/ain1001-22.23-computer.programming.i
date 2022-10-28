"""
How can you decide whether a number is a multiple of 5 or 7, but not both ?
"""
x = int(input("Enter an integer: ").strip())
if x % 5 == 0 and x % 7 != 0:
    print(f"{x} is multiple of 5.")
elif x % 7 == 0 and x % 5 != 0:
    print(f"{x} is multiple of 7.")
