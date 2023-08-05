while True: 
    print("Who are you?")
    name = input().title()
    if name != "Joe":
        continue
    else:
        break
while True:    
    print("Hello Joe. What is your password? (Hint: It is a fish.)")
    password = input()
    if password != "swordfish":
        print("Wrong password. Try again!")
        continue
    else:
        break
print("Access Granted.")
