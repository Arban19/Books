def add_numbers(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum

total = add_numbers([1,2,3])
print("The sum of these numbers is " + str(total) + ".")