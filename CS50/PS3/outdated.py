months =  ["January","February","March","April","May","June","July","August","September","October","November","December"]

while True:
        try:

            date = input("Date: ").strip()
            if "/" not in date and "," not in date:
                raise ValueError

            if "/" in date:
                month, day, year = date.split("/")
            else:
                date = date.replace(",","")
                month, day, year = date.split(" ")
                if month in months:
                    month = months.index(month) + 1

            if int(month) > 12 or not (1 <= int(day) <= 31):
                raise ValueError
            else:
                break

        except ValueError:
            pass

print(f"{year}-{int(month):02}-{int(day):02}")
