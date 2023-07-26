import random
secret_number = random.randint(1,25)
print("I'm thinking of a number between 1 and 25. Guess the number. You get 10 attempts.\n")
print("At any point hit Control + D to exit the game.\n")


for guesses_taken in range(1,11):
    print("Take a guess.")
    guess = int(input())

    if guess < secret_number:
        print("Your guess is too low")
    elif guess > secret_number:
        print("Your guess is too high.")
    else:
        break

if guess == secret_number:
    print("Congratulations, you've taken the correct guess in " + str(guesses_taken) + " attempts. Well done!")
else:
    print("Nope. The correct guess is " + str(secret_number) + ".")
