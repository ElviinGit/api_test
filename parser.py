import argparse

parser = argparse.ArgumentParser(description="parser demo for learning")

parser.add_argument("name", help="to providing your name to the function")
parser.add_argument("--age", type=int, help="to providing your age to the function")

args = parser.parse_args()

print(f"Hello {args.name}, you are {args.age} years old.")

