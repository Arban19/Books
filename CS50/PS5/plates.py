def main():
    s = input("Plate: ").upper()
    if is_valid(s):
        print("Valid")
    else:
        print("Invalid")

def not_zero(s):
    i = 0
    while i < len(s):
        if s[i].isdigit():
            if s[i] == "0":
                return False
            else:
                break
        i += 1
    return True

def does_not_end_with_str(s):
    if len(s) > 2:
        return not s[-1].isalpha()
    else:
        return True

def is_valid(s):
    return (2 <= len(s) <= 6) and s[:2].isalpha() and not_zero(s) and s.isalnum() and does_not_end_with_str(s)


if __name__ == "__main__":
    main()
