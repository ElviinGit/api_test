def logger(inner_function):
    def wrapper():
        print("Function started...")
        inner_function()
        print("Function finished")  
    return wrapper

# wiht an syntactic sugar, we can use the @ symbol to apply the decorator to a function. This is equivalent to writing login = logger(login) after the function definition.
# @logger 
def login():
    print("Logging in...")  


# login()

# with older versions of Python, we can use the decorator syntax without the @ symbol. This is equivalent to writing login = logger(login) after the function definition.

decorated_login = logger(login)
decorated_login()