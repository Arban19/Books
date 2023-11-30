vowels = "AEIOUaeiou"
def shorten(word):
    for char in vowels:
        word = word.replace(char,"")
    return word

def main():
    text = input("Enter string: ")
    print("Shortened string:", shorten(text))

if __name__ == "__main__":
    main()
