import json

product = {}

# read product data from keyboard
product["name"] = input("Product name: ").strip()

price_input = input("Price (e.g. 12.34): ").strip()
product["price"] = round(float(price_input), 2)

paid_input = input("Paid (yes/no): ").strip().lower()
product["paid"] = (paid_input == "yes")

# save product data to json file
with open("product.json", "w", encoding="utf-8") as file:
    json.dump(product, file, ensure_ascii=False, indent=2)

print("Saved to product.json")
print(product)