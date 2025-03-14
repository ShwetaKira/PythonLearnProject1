global_var =10 #global variable

def variable():
    local_var =20 #local variable within the function
    print(local_var)
    print(global_var)


variable()
print(global_var)