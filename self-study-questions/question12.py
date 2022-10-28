"""
A mathematician lives on a street where house numbers are consecutive starting from 1.
She says that the sum of the house numbers less than her house number is equal to the sum of the house numbers
greater than her house number.

Knowing that his house number contains 3 digits design an algorithm and write a python script to find her house number.
"""
for house_number in range(100, 999):
    sum_of_house_numbers_left = 0
    for i in range(1, house_number):
        sum_of_house_numbers_left += i
    sum_of_house_numbers_right = 0
    for i in range(house_number, 999):
        sum_of_house_numbers_right += i
        number_of_houses = i
        if sum_of_house_numbers_right >= sum_of_house_numbers_left:
            break
    if sum_of_house_numbers_left == sum_of_house_numbers_right:
        print(f"The mathematician lives on {house_number} and there {number_of_houses} houses on the street.")
        break
