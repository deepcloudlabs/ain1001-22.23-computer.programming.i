from utility.math import *

numbers = [4, 8, 23, 16, 15, 42]

solution = sum(numbers)
print(solution)
num_of_odds = count(numbers, is_odd)
print(num_of_odds)
num_of_evens = count(numbers,is_even)
print(num_of_evens)
