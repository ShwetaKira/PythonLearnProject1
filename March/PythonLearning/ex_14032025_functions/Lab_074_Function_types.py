#default argument or Positional argument

def say_hello_to_defualt_argument(name="shweta"):
    print("Hello",name.upper())

say_hello_to_defualt_argument()
say_hello_to_defualt_argument("Kiaan")

def multiple_arguments(name1= "A",name2="B"):
    print("Hello-->", name1, name2)

multiple_arguments()
multiple_arguments(name1 = "Shweta",name2="Kiran")
multiple_arguments(name1="Chandini")
multiple_arguments(name2="Kiaan")
multiple_arguments("Anshu")

# Argument + return type

def sum_of_Two(a,b):
    return a+b

result= sum_of_Two(2,3)
print(result)