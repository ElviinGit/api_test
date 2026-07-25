from functools import wraps
counter = 0

def retry(func):
    @wraps(func)
    def inner(*args, **kwargs):
        attempts = 0 
        while attempts < 6:
            try:
                print(f"{attempts} time function executing")
                result = func(*args, **kwargs)
                return result

            except Exception as e:
                print(e)
            attempts += 1
        print("Final attempt already done. Now return!")
        raise Exception("last attempt executed")
    return inner
    
@retry
def login():
    global counter
    counter = counter + 1
    print(f"Login Function {counter} time")
    if counter < 6:
        raise Exception("It is less tham '6' that's why i raising") 
    return "You've already logged in big boy"




a = login()
print(a)