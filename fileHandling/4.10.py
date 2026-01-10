file = open("clothing.csv", "r", encoding="utf-8")

header = file.readline()  # pomijamy nagłówek

print("PRODUCTS WITH PRICE < 60 AND STOCK < 40")
print("----------------------------------------")

for line in file:
    line = line.strip()
    parts = line.split(",")

    product_name = parts[1]
    price = float(parts[5])
    stock = int(parts[6])

    if price < 60 and stock < 40:
        print(f"Product: {product_name}")
        print(f"  Price: {price} PLN")
        print(f"  Stock: {stock}")
        print("----------------------------------------")

file.close()