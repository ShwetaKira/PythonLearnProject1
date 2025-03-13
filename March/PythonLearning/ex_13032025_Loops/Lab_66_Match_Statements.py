
# Python > 3.10

# match variable:
#     case pattern1:
#         # code block
#     case pattern2:
#         # code block


# Write a program to ask the user which browser he wants to run automation.
browser_name = input("Enter Browser Name: ")
match browser_name:
    case "Chrome":
        print("Chrome is Starting!!!")
    case "FireFox":
        print("Fireforx is starting")
    case "Edge":
        print("Edge is starting")
    case _: #_ is a default 
        print("No Browser Found")