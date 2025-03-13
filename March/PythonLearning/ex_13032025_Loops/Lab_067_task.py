# Write a program that prints numbers from 1 to 100.
# However, for multiples of 3, print "Fizz" instead of the number,
# and for multiples of 5, print "Buzz."
# For numbers that are multiples of both 3 and 5, print "FizzBuzz." ( for, if)

# step1: I/p: 1 to 100>For loop range
# step 2: o/p :
# num*3 = fizz
# num*5 = Buzz
# num*3 and num*5 == fizzbuzz
# rough logic

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
