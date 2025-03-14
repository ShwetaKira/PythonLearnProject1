# Leap day occurs in each year that is a multiple of 4,
# except for years evenly divisible by 100 but not by 400.
from operator import truediv


# ligic building
# i/p : year int
# o/p : string whether it is leap year or not

# rough logic
# if year is % 4== 0==> leap year
# if year is !%100 == 0

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Test the function
year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

