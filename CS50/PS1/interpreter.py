def interpreter(numbers):
    k = numbers.split()
    x = int(k[0])
    y = k[1]
    z = int(k[2])

    if y == "+":
        return round(float(x + z), 1)
    elif y == "-":
        return round(float(x - z), 1)
    elif y == "*":
        return round(float(x * z), 1)
    elif y == "/":
        if z == 0:
            return "Invalid input"
        else:
            return round(float(x / z), 1)

numbers = input("Expression: ")
print((interpreter(numbers)))
