from decorators.decorators import my_decorator

@my_decorator
def test_login(driver):
    print("Executing test_login")
    print(f"-----driver is {driver}")   
    assert False, "Intentional failure to test screenshot capture"



