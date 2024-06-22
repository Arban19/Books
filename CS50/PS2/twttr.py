def remove_vowels(text):
    vowels = "AEIOUaeiou"
    for char in vowels:
        text = text.replace(char,"")   
    return text
    
def main():
    text = input("Enter string: ")
    print("Text without vowels:", remove_vowels(text))

if __name__ == "__main__":
    main()