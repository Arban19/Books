rate_chart = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    order_cost = 0.0
    try:
        while True:
            item = input("Item: ").title().strip()
            if item in rate_chart:
                order_cost += rate_chart[item]
                print(f"Total: ${order_cost:.2f}")
            else:
                continue
    except EOFError:
        pass

main()
