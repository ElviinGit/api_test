import time
from datetime import datetime


def session(func):
    def inner(*args, **kwargs):
        start = datetime.now()
        print(f"Session Started...{start}")
        product = func(*args, **kwargs)
        end = datetime.now()
        print(f"Session Ended. at this time{end}")
        return product
    return inner


def login():
    print("Login Process Starting...")

def authenticate():
    time.sleep(3)
    print("Authenticating")

def greet(name):
    print(f"hi {name}")

@session
def workflow(name="guest"):
    login()
    authenticate()
    greet(name)

workflow("Tupac")