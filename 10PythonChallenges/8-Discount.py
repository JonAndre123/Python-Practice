def discount(price: int, sale: int):
    return price - (price*(sale/100))

print(discount(100, 20))
