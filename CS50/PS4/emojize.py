import emoji

def emojize_string(input_string):
    return emoji.emojize(input_string)

def main():
    user_input = input("Input: ")
    emojized_string = emojize_string(user_input)
    print("Output:", emojized_string)

main()
