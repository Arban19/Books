import sys

def main():
    no_of_lines = 0
    if check_command_line_argument():
        try:
            files = open(sys.argv[1],"r")
            lines = files.readlines()
        except FileNotFoundError:
            sys.exit("File does not exist")
        for line in lines:
            if not check_if_comment_or_blank(line):
                no_of_lines += 1
        print(no_of_lines)

def check_command_line_argument():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if ".py" not in sys.argv[1]:
        sys.exit("Not a python file")
    return True

def check_if_comment_or_blank(line):
    if line.isspace() or line.lstrip().startswith("#"):
        return True
    return False

if __name__ == "__main__":
    main()
