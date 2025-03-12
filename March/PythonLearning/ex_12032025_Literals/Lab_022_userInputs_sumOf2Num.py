#write a  program to take 2 user inputs
#sum the numbers
#div

#Login Building
#step 1 : Input -> num1 , num2 -> Int or Float ?
#step 1 : Output ->sum -> int , sub-> int , div-> float
num1 = input("Fist Number is: ") #input is a String
num2 = input("Second Number is: ")
print(type(num1))

#step 2: Convert the string into integer

SumOf2Num = int(num1)+ int(num2)
print(SumOf2Num)

mulof2Num = int(num1)*int(num2)
print(mulof2Num)

divof2Num = int(num1)/int(num2)
print(divof2Num)

subof2Num = int(num1)-int(num2)
print(subof2Num)

num3 = float(input("Number 3 is : "))
num4 = float(input("Number 4 is : "))
sum = num3 +num4
sub = num3 - num4
mul = num3 * num4
div = num3 / num4

print(sum)
print(sub)
print(mul)
print(div)
