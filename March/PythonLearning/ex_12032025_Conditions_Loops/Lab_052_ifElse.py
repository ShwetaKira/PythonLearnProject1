# Program to find the max of 3 numbers
# logic building
# user inputs : num1 , num2 and num 3 integers
# 0/p -> string or int
# Logic? -> if -else - 1 condition  , elif

# Syntax
# if condition 1:
#     print("do 1")
# elif condition 2:
#     print("do 2")
# elif condition 3:
#     print("do 3")
# else:
#     print(" do for else")

num1 = int(input(" enter num1: ")) #5, #3
num2 = int(input(" enter num2: ")) #3,#6
num3 = int(input(" enter num2: "))#2,#1
#rough logic
# 5>3 5>2 => max is 5
# num1>num2 , num1 > num3 , max is num1
#6>3 and 6> 1 m max is num2
# num2> num1 and num2> num3 === max is num2
# if both condition fails num3 will be the max

if num1>=num2 and num1>=num3:
    print(f"max num is{num1}")
elif num2>=num1 and num2>=num3:
    print("max num is: ", num2)
else:
    print("max num is:", num3)

