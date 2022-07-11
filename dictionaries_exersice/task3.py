data = input()
products = {}

while data != "statistics":
    product, quantity = data.split(": ")
    quantity = int(quantity)
    if product not in products:
        products[product] = quantity

    else:
        products[product] += quantity

    data = input()

print('Products in stock:')
for prod, quan in products.items():
    print(f"- {prod}: {quan}")

print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")