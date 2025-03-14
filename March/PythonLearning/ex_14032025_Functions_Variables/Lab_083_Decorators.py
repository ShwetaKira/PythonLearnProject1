# #Decorators => modifies the behaviour of the function without modifying the actual function


def add_Security(func):
    def wrapper():

        print("1.before the function is called")
        print("2.add helmet, license,gloves, shoes")
        func() # called drive_scooty() function
        print("After the function is called")
        print("4. secure driving, leave all the items")
    return wrapper()

@add_Security
def drive_Scooty():
    print("I am a Normal function!")
    print("I am driving scooty")