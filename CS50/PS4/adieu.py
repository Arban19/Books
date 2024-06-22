def name_format(names):
    if len(names) == 1:
        return names[0]
    elif len(names) == 2:
        return f"{names[0]} and {names[1]}"
    else:
        formatted_names = ", ".join(names[:-1]) + f", and {names[-1]}"
        return formatted_names

def main():
    names = []
    while True:
        try:
            name = input("Name: ").title().strip()
        except EOFError:
            break

        names.append(name)

    farewell_message = name_format(names)
    print("Adieu, adieu, to", farewell_message)

main()
