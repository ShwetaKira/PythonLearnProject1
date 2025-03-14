import time


def time_decorator(func):
    def wrapper():
        start_time = time.time()
        print("Start time is : ", start_time)
        func()
        End_time = time.time()
        print("End time is :", End_time)
        total_time = End_time - start_time
        print("total time taken is :", total_time)

    return wrapper()


def print_log_decorator(func):
    def wrapper():
        print("Starting Log")
        func()
        print("Ending Log")

    return wrapper()


@time_decorator
@print_log_decorator
def test_UI_1():
    print("Add a function, time taken by function1")
    time.sleep(2)


@time_decorator
def test_UI_2():
    print("Add a function, time takem by function2 ")
    time.sleep(3)

test_UI_1()
test_UI_2()
