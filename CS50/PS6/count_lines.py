import sys

def main():
    if check_command_line_argument():
        try:
            files = open(sys.argv[1],"r")
            lines = files.readlines()
        except FileNotFoundError:
            sys.exit("File does not exist")
        no_of_lines = sum(1 for line in lines if not (line.isspace() or line.lstrip().startswith("#")))
        print(no_of_lines)

def check_command_line_argument():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if ".py" not in sys.argv[1]:
        sys.exit("Not a python file")
    return True

if __name__ == "__main__":
    main()
