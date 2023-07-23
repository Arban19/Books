# this is not the actual code

while True: # condition cannot be false since its always true hence use break
    print("Who are you?")
    name = input().title()
    if name != "Joe":
        continue
    else:
        break
while True:    
    print("Hello Joe. What is your password? (Hint: It is a fish.)")
    password = input()
    if password != "swordfish": # ask Neil why not asking for password
        print("Wrong password. Try again!")
        continue
    else:
        break
print("Access Granted.")