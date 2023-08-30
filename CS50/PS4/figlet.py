import sys
import random
import pyfiglet

def get_font():
    return pyfiglet.FigletFont.getFonts()

def main():
    args = sys.argv[1:]

    if len(args) == 0:
        user_font = random.choice(get_font())
    elif len(args) == 2 and (args[0] == "-f" or args[0] == "--font"):
        user_font = args[1]
        if user_font not in get_font():
            sys.exit("Invalid Input")
    else:
        sys.exit("try [-f/--font <font_name>]")

    font_needed = input("Input: ")
    figlet_instance = pyfiglet.Figlet(user_font)
    output = figlet_instance.renderText(font_needed)
    print(output)

main()
