import random

while True:
    level = input("Level: ")
    if not level.isdigit() or int(level) <= 0:
        continue
    else:
        break
correct_number = random.choice(range(1, int(level) + 1))

while True:
    guess = input("Guess: ")
    if not guess.isdigit():
        continue
    guess = int(guess)
    if guess != correct_number:
        if guess < correct_number:
            print("Too small!")
        elif guess > correct_number:
            print("Too large!")
        continue
    else:
        print("Just right!")
        break
