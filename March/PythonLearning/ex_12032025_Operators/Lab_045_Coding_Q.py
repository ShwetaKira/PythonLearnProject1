# Write a Python program to calculate the
# area of a circle given its radius using the formula
# ``` area=π×r^2``` ( Take pie as 3.14)


# Logic Building Formula

# || Step 1 ||
# Figure out the inputs and output
# input -> r ->  data type -> float
# pi = 3.14
# power -> pow or ** -> any
# o/p -> float - area , print area


# || Step 2 ||
# rough logic =  area = 3.14 * pow(r,2)


# || Step 3 ||

radius = float(input("Enter the r:"))
print(radius)
area = 3.14 *(radius ** 2)
print(f"are of the circle is:{area}")

#** -> pow
