names = []

with open("name.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"Hello, {name}")

for name in sorted(names, reverse=True):
    print(f"Hi, {name}")

with open("name.txt") as file:
    for line in sorted(file):
        print(f"Wassup,",line.rstrip())
