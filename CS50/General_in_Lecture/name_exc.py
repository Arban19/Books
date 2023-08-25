import sys
try:
    print(f"Hello! My name is {sys.argv[1]}.")
except IndexError:
    z = input("Please type your name: ")
    print(f"Hello! My name is {z}.")
