price_list = {
    'T-shirt': 19.99,
    'Jeans': 49.99,
    'Jacket': 89.99,
    'Sneakers': 59.99,
    'Hat': 15.99
}

# prices before discount
print("Prices before discount:")
for product, price in price_list.items():
    print(product, "-", price)

total_before = sum(price_list.values())
print("Total value before discount:", round(total_before, 2))

# apply 10% discount
for product in price_list:
    price_list[product] = round(price_list[product] * 0.9, 2)

# prices after discount
print("\nPrices after 10% discount:")
for product, price in price_list.items():
    print(product, "-", price)

total_after = sum(price_list.values())
print("Total value after discount:", round(total_after, 2))