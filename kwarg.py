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
    

counter = 0

def retry(func):
    @wraps(func)
    def inner(*args, **kwargs):
        attempt = 0 
        while attempt < 3:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                attempt = attempt + 1
                print(e)
                
    return inner
        
@retry
def login():

    global counter
    counter = counter + 1
    if counter < 3:            
        raise Exception("Network lag")      
    else:
        print("You've successfully logged")
login()   
