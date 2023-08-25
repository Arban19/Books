import sys

if len(sys.argv) < 2 or len(sys.argv) > 2:
    z = input("What is your name? ")
    print(f"Hello. Pleased to meet you, {z}.")
else:
    print(f"Hello. Pleased to meet you, {sys.argv[1]}.")
