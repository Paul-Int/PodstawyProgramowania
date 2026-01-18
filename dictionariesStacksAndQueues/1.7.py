products = {
    'Laptop': 15,
    'Desktop PC': 10,
    'Monitor': 25,
    'Keyboard': 50,
    'Mouse': 60,
    'External Hard Drive': 30,
    'Printer': 12,
    'Router': 20,
    'USB Flash Drive': 100,
    'Graphics Card': 8
}

# a list of products and their quantities
print("PRODUCT - QUANTITY")
for product, quantity in products.items():
    print(product, "-", quantity)

# total number of products in the store
total_products = sum(products.values())
print("Total number of products in the store:", total_products)