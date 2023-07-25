
def convert(input_str):
    converted_str = input_str.replace(":)", "🙂").replace(":(","🙁")
    return converted_str

def main():
    user_input = input("Say something I'm giving up on you  ")
    converted_input = convert(user_input)
    print(converted_input)

main()
