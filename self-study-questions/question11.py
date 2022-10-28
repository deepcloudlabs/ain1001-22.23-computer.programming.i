"""
Write a python script that takes an integer value and prints the number with its digits reversed.
For example given the number 7361, the program should print 1637
"""
number = int(input("Enter an integer: ").strip())
reversed_number = 0
while number > 0:
    reversed_number = 10 * reversed_number + number % 10
    number = number // 10
print(reversed_number)
