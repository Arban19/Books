def main():
    grocery_list = {}

    try:
        while True:
            item = input().strip().capitalize()
            if item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1
    except EOFError:
        pass

    for item in sorted(grocery_list.keys()):
        count = grocery_list[item]
        print(f"{count} {item.upper()}")


main()
