counter = 0

def login():
    global counter
    counter = counter + 1
    print(f"it is my {counter} time execution")
    if counter < 7:
        raise Exception("It is less than 3 network lag")
    print("you passed exception section")

attempts = 0
while attempts < 10:
    try:
        login()  
        break
    except Exception as e:
        attempts += 1
        print(e)