#Program => If your age >18 -> allowed to vote
#else not allowed to Vote

User_age = int(input("Enter your age: "))

if User_age > 18:
    print("You can Vote")
else:
    print("You can not Vote")


print("You can Vote" if User_age>18 else "You can not vote")