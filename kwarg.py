from functools import wraps
# def addition(*args):
#     return sum(args)

# result = addition(5, 3, 8, 2)

# print("The result of addition is:", result)

# def greet_user(**kwargs):
#     name = kwargs.get("name", "anonymous")
#     place = kwargs.get("place", "unknown")
#     return f"Hello, {name} from {place}!"

# greeting_alice = greet_user(name="Alice")
# greeting_default = greet_user() 

# print(greeting_alice)  # Output: Hello, Alice from Wonderland!


# def print_details(**kwargs):
#     age = kwargs.get("age") 
#     print(f"Age is {age}")

# my_details = print_details()  # Output: Age is 30
# # print(my_details)  # Output: Age is 30

# def greet(**kwargs):
#     name = kwargs.get("name", "Guest")
#     age = kwargs.get("age")
#     return f"Hello {name}, age {age}"

# print(greet(name="Elvin"))
# print(greet())  # Hello Guest, age unknown
    
def retry(funcs):
    @wraps(funcs)
    def inner(*args, **kwargs):
        attempts = 0 
        while attempts < 5:
            try:
                print(f"{attempts} time function executing")
                result = funcs(*args, **kwargs)
                return result
            except Exception as e:
                print(e)
            attempts += 1
        print("last attempt almost executeted... now deal with the exception")
        raise Exception("You're done boy!")
    return inner    

counter = 0
@retry
def login():
    global counter
    counter = counter + 1
    print("I am about to login")
    if counter < 5:
        raise Exception("Network Log")
    return "Youre logged in successfully"
b = login()
print(b)