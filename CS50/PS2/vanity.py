def is_valid(plate):
    return (2<= len(plate) <= 6) and plate[:2].isalpha() and number_end(plate) and not_zero(plate) and plate.isalnum()

def number_end(plate):
    for index, char in enumerate(plate):
        if char.isdigit():
            return plate[index:].isdigit()
    return True

def not_zero(plate):
    for i in plate:
        if i.isdigit():
            if i == "0":
                return False
            else:
                break
    return True

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

main()
