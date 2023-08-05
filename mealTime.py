def convert(time):
    time_hrsmin = time.split(":")
    if len(time_hrsmin) != 2 or not time_hrsmin[0].isdigit() or not time_hrsmin[1].isdigit():
        print("Invalid input.")
        return None
    
    hours = int(time_hrsmin[0])
    minutes = int(time_hrsmin[1])

    if not (0 <= hours <= 24) or not (0 <=minutes<= 59):
        return None

    return hours + minutes/60.0
    
def main():
    time = input("What time is it? ")
    time_hrs = convert(time)

    if time_hrs is not None:
        breakfast_start = 7.0
        breakfast_end = 8.0
        lunch_start = 12.0
        lunch_end = 13.0
        dinner_start = 18.0
        dinner_end = 19.0

        if breakfast_start <= time_hrs <= breakfast_end:
            print("It's breakfast time!")
        elif lunch_start <= time_hrs <= lunch_end:
            print("It's lunch time!")
        elif dinner_start <= time_hrs <= dinner_end:
            print("It's dinner time!")
        else:
            pass

if __name__ == "__main__":
    main()

