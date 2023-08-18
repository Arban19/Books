def interpreter(numbers):
    x = int(numbers.split()[0])
    y = numbers.split()[1]
    z = int(numbers.split()[2])

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
