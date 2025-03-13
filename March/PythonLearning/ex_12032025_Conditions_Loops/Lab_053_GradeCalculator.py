#Grade Calculator
# Write a program that calculates and displays the letter grade
# for a given numerical score (e.g., A, B, C, D, or F)
# based on the following grading scale

# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

#Rough logic
#score>= 90 and score<=100 ==> A
# score>=80 and score<=89 => B
# score>=70 and score<=79 => C
# score>=60 and score<=69 => D
# score>=0 and score<=59 => F
Score  = int(input("Enter your Score: "))
if Score >= 90 and Score<=100:
    print("Your Grade is:","A")
elif Score >= 80 and Score<=89:
    print("Your Grade is:","B")
elif Score >= 70 and Score<=79:
    print("Your Grade is:","C")
elif Score >= 60 and Score<=69:
    print("Your Grade is:","D")
elif Score>100:
    print(" you can't get this grade")
else:
    print("you have failed!!!")

