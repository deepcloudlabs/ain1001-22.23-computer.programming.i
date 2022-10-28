"""
A leap year is a year in which an extra day is added to the calendar in order to synchronize it with the seasons.
Since the tropical year is 365.242190 days long, a leap year must be added roughly once every four years.

The following pseudocode determines whether a year is a leap year or a common year in the Gregorian calendar
if (year is not divisible by 4) then (it is a common year)
else if (year is not divisible by 100) then (it is a leap year)
else if (year is not divisible by 400) then (it is a common year)
else (it is a leap year)
"""
year = int(input("Enter a year: ").strip())
if year % 4 != 0:
    print(f"{year} is a common year")
elif year % 400 == 0:
    print(f"{year} is a leap year")
elif year % 100 != 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is a common year")
