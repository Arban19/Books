def main():
    fraction = input("Fraction: ")
    result = convert(fraction)
    print(gauge(result))

def convert(fraction):
    try:
        num, den  = fraction.split("/")
        x = int(num)
        y = int(den)
        percentage = (x/y)*100
        if percentage <= 100:
            return percentage
        else:
            raise ValueError
    except (ValueError, ZeroDivisionError):
        raise

def gauge(percentage):
    if percentage <= 1:
        return "E"
    if percentage >= 99:
        return "F"
    else:
        return str(round(percentage)) + "%"

if __name__ == "__main__":
    main()
