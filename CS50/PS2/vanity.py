def is_valid(plate):
    return min_length(plate) and max_length(plate) and letter_start(plate) and number_end(plate) and not_zero(plate) and no_puncs(plate)

def min_length(plate):
    return len(plate) >= 2

def max_length(plate):
    return len(plate) < 6

def letter_start(plate):
    return plate[:2].isalpha()

def number_end(plate):
    return plate[-3:].isdigit()

def not_zero(plate):
    return plate[1] != "0"

def no_puncs(plate):
    return plate.isalnum()

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

main()








