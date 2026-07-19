import argparse

def message(message_type: str, *args):

    if not args:
        args = ("Anonymous")
        
    elif message_type == "greet":
        print(f"Hello! Welcome to the program. {args[0]}")

    elif message_type == "farewell":
        print(f"Goodbye! See you next time. {args[0]}")

    else:
        print("Invalid message type. Please use 'greet' or 'farewell'.")

result_message = message("", "Alice")

argaparser = argparse.ArgumentParser(description="Message Type and Name")

args = argaparser.parse_args()

