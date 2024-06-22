import random


def main():
    level = get_level()
    score = 0

    for turn in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y

        problem = f"{x} + {y} = "
        attempts = 0

        while attempts < 3:
            try:
                answer = int(input(problem))
                if answer == correct_answer:
                    score +=1
                    break
                if answer != correct_answer:
                    print("EEE")
            except ValueError:
                print("EEE")
            attempts += 1
            if attempts == 3:
                print(f"Correct answer: {correct_answer}")

    print(f"Score = {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
            else:
                continue
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    elif level == 3:
        return random.randint(100,999)

if __name__ == "__main__":
    main()
