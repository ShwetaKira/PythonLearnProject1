def outer_function():
    var1 = 50 #local variable

    def inner_function1():
        print(var1)

    def inner_function2():
        print(var1)

    inner_function1()
    inner_function2()

outer_function()
