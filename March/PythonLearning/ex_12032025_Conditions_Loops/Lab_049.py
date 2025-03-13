#Write a program to take a user age and let him know if he can go the club.  21

#logic Building
#step 1: figure out user input  -. data type : int
#output : string: user can or can not go to cub

#step: rough logic
#age >21: can go to club
#age <21 can not go to club

#step 3: write the logic
age = input("Enter your age :")
age = int(age)

if age>=21:
    print("you can go to club!")
else:
    print(f"You can not got to club with this age :{age} ")

#Step 4: check for edge cases
# negative numbers or alhanumeric or spl characters ---> program will break


# step 5: Optimizes the code
#handle all the edge cases




