with open("name.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("Hello,", line.rstrip())


with open("name.txt", "r") as file:
    for line in lines:
        print("Hi,", line, end="")
