#Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal), or scalene (no sides are equal).
# Use an if-else statement to classify the triangle

#s1, s2, s3 → int
s1 = int(input("Enter length of Side1: ")) #3,4,3
s2 = int(input("Enter length of Side2: "))#3,4,5
s3 = int(input("Enter length of Side2: "))#3,5,6
#o/p →. iso, eq, scelene
#rough logic
# S1==S2==S3 ===> Equilateral Traingle
# S1!=s2!=s3 ==> Scalence Traingle

if s1 ==s2==s3:
    print("Equilateral Traingle")
elif  s1!=s2!=s3 :
    print("Scalence Traingle")
else:
    print("Isosceles Traingle")

