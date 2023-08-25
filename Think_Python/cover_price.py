def main():
    cover_price = 24.95
    bookstore_discount = 0.4
    shipping_cost_1 = 3
    shipping_cost_2on = 0.75
    return round((cover_price * (1 - bookstore_discount))* 60 + (shipping_cost_1*1 + shipping_cost_2on*59), 2)

print(main())



from decimal import Decimal

def wholesale_cost(args):

    d = 1 - args.get('discount')/100
    purchase = Decimal(args.get('cost') * d * 60)
    return purchase + Decimal(args.get('delivery'))

print(wholesale_cost(args =  {'cost': 24.95, 'discount': 40, 'delivery': 3.00+0.75*59}))
