def fuel():
    while True:
        try:
            number = input("Fraction: ")
            z = number.split("/")
            numerator = int(z[0])
            denominator = int(z[1])
            if numerator > denominator:
                raise ValueError
            answer = (numerator/denominator)*100
            return round(answer)
            break
        except (ValueError, IndexError, ZeroDivisionError) as error:
            continue

def response(answer):
    if answer >= 99:
        return "F"
    elif answer <= 1:
        return "E"
    else:
        return str(answer) + "%"

result = fuel()
print(response(result))
