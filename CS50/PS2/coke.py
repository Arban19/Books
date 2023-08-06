def amount_due(amount_paid, price):
    return price - amount_paid

def main():
    price = 50
    accepted_coins = [5, 10, 25]
    amount_paid = 0

    while amount_paid < price:
        coin = int(input("Insert coin: "))
        if coin in accepted_coins:
            amount_paid += coin
            print("Amount Due:", price - amount_paid)
        else: 
            print("Amount Due:", price - amount_paid)       
            continue

    change = abs(amount_due(amount_paid, price))
    print("Change Owed:", change)

if __name__ == "__main__":
    main()
