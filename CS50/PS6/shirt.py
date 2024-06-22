import sys
from PIL import Image, ImageOps

def main():
    if len(sys.argv) != 3:
        sys.exit("Revise command-line arguments")
    if sys.argv[1].split('.')[-1].lower() != sys.argv[2].split('.')[-1].lower():
        sys.exit("Input and output have different extensions")
    try:
        image = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")
    if image.format.lower() not in ["jpg", "jpeg", "png"]:
        sys.exit("Invalid entry")
    shirt = Image.open("shirt.png")
    size = shirt.size
    output = ImageOps.fit(image,size)
    output.paste(shirt, shirt)
    output.save(sys.argv[2])

if __name__ == "__main__":
    main()
