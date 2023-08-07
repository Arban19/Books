def camel_to_snake(camelCase):
    snake_case = ""
    for char in camelCase:
        if char.isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char
    return snake_case

def main():
    camelCase = input("camelCase: ")
    snake_case = camel_to_snake(camelCase)
    print("Snake_case: ", snake_case)


if __name__ == "__main__":
    main()