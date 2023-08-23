import math

def fuel():
    while True:
        number = input("Fraction: ")
        z = number.split("/")
        numerator = int(z[0])
        denominator = int(z[1])
        try:
            if numerator > denominator:
                raise ValueError

            answer = math.ceil((numerator/denominator)*100)
            return answer
            break
        except (ValueError, IndexError, ZeroDivisionError) as error:
            continue

def response(answer):
    if answer is None:
        return "Invalid Input"
    elif answer >= 99:
        return "F"
    elif answer <= 1:
        return "E"
    else:
        return str(answer) + "%"

result = fuel()
print(response(result))
