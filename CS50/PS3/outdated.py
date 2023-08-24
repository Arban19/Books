months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
        date = input("Date: ")
        if "/" in date:
            month, day, year = date.split("/")
            day = int(day)
            month = int(month)
        elif "," in date:
            date = date.replace(",","")
            month, day, year = date.split(" ")
            day = int(day)
            if month in months:
                month = months.index(month) + 1
        try:
            if int(month) > 12 or int(day) > 31:
                raise ValueError
            else:
                break
        except (ValueError, AttributeError, NameError, KeyError):
            pass

print(f"{year}-{int(month):02}-{int(day):02}")
