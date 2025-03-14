def add_before_uI_after_UI(func):
    def wrapper():
        print("Before running the UI TC")
        print("start the browser")
        func()
        print("End the execution")
        print("Quit the broser")

    return wrapper()

@add_before_uI_after_UI
def test_UI():
    print("**** I will run the TC's*****")

@add_before_uI_after_UI
def test_1():
    print("1st TC is passed")

@add_before_uI_after_UI
def test_2():
    print("Second test case is passed")