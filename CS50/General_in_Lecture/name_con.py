import sys

if len(sys.argv) < 2 or len(sys.argv) > 2:
    sys.exit("Proper format not adhered to")

print(f"Hello. Pleased to meet you, {sys.argv[1]}.")
