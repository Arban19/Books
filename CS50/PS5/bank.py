def main():
    greeting = input("Greeting: ")
    print("$", value(greeting), sep = "")

def value(greeting):
    z = greeting.strip().lower()
    if z.startswith("hello"):
        return 0
    elif z.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
