import csv, sys

def main():
    if len(sys.argv) != 3:
        sys.exit("Invalid input")

    try:
        with open(sys.argv[1],"r") as inputfile, open(sys.argv[2],"w") as outputfile:
            reader = csv.DictReader(inputfile)
            writer = csv.DictWriter(outputfile, fieldnames=["first","last", "house"])
            writer.writeheader()
            for row in reader:
                full_names = row["name"].split(",")
                writer.writerow({
                    "first": full_names[1].lstrip(),
                    "last": full_names[0],
                    "house":row["house"],
                })
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

if __name__ == "__main__":
    main()
