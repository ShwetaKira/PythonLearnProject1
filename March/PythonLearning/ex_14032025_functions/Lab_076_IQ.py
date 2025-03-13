# sum of 3 num, user does not use any argument then use default arg as 100,200,300

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))


def sum_of_3_num(num1=100, num2=200, num3=300):
    return num1 + num2 + num3


result = sum_of_3_num(num1, num2, num3)
print(result)

result1= sum_of_3_num()
print(result1)