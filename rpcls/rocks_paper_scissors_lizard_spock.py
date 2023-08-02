import random, sys

print("Hello, welcome to my Rock, Paper, Scissor, Lizard, Spock game.\n")
response = input("If haven't seen TBBT and are unfamiliar with the rules, type n. Else hit any other key to proceed. \n").lower()
if response == "n":
    print(" The rules are as follows:\n Scissors cuts Paper\n Paper covers Rock\n Rock crushes Lizard\n Lizard poisons Spock\n Spock smashes Scissors\n Scissors decapitates Lizard\n Lizard eats Paper\n Paper disproves Spock\n Spock vaporizes Rock\n Rock crushes Scissors\n")
    print(" In simpler terms:\n Scissors > Paper\n Paper > Rock\n Rock > Lizard\n Lizard > Spock\n Spock > Scissors\n Scissors > Lizard\n Lizard > Paper\n Paper > Spock\n Spock > Rock\n Rock > Scissors\n ")

wins = 0
losses = 0
ties = 0

while True:
    print("Hit q or any other key other than the assigned keys at anytime to exit the game.\n")
    print("Score after Current Round: Wins, Losses, Ties\n", (wins, losses, ties))
    print("Enter your move: (r)ock, (p)aper, s(c)issor, (l)izard, (s)pock or (q)uit.\n")
    player_move = input().lower()
    if player_move == "q":
        sys.exit()
        print("Final Score: Wins, Losses, Ties", (wins, losses, ties))
        print("Thank you. Bye-Bye")
    if player_move == "r":
        print("Rock versus...")
    elif player_move == "p":
        print("Paper versus...")
    elif player_move == "c":
        print("Scissors versus...")
    elif player_move == "l":
        print("Lizard versus...")
    elif player_move == "s":
        print("Spock versus...")
    else:
        sys.exit()

    random_number = random.randint(1,5)
    if random_number == 1:
        computer_move = "r"
        print("Rock")
    elif random_number == 2:
        computer_move = "p"
        print("Paper")
    elif random_number == 3:
        computer_move = "c"
        print("Scissors")
    elif random_number == 4:
        computer_move = "l"
        print("Lizard")
    elif random_number == 5:
        computer_move = "s"
        print("Spock")

    win_message = "You win this round!"
    lose_message = "You lose this round!"
    draw_message = "Damn, inspite of all these complex rules, we still somehow managed to tie the game!!"
    if player_move == computer_move:
        print(draw_message)
        ties += 1
    elif player_move == "c" and computer_move == "p":
        print(win_message)
        wins += 1
    elif player_move == "p" and computer_move == "r":
        print(win_message)
        wins += 1
    elif player_move == "r" and computer_move == "l":
        print(win_message)
        wins += 1
    elif player_move == "l" and computer_move == "s":
        print(win_message)
        wins += 1
    elif player_move == "s" and computer_move == "c":
        print(win_message)
        wins += 1
    elif player_move == "c" and computer_move == "l":
        print(win_message)
        wins += 1
    elif player_move == "l" and computer_move == "p":
        print(win_message)
        wins += 1
    elif player_move == "p" and computer_move == "s":
        print(win_message)
        wins += 1
    elif player_move == "s" and computer_move == "r":
        print(win_message)
        wins += 1
    elif player_move == "r" and computer_move == "c":
        print(win_message)
        wins += 1
    else:
        print(lose_message)
        losses +=1
