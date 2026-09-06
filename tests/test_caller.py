from decorate import my_decorator

@my_decorator
def test_login(driver):
    print("Executing test_login")
    print(f"-----driver is {driver}")   
    raise Exception("Simulated error in test_login")




