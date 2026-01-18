def hotel_list(hotels):
    names = []
    for hotel in hotels:
        names.append(hotel["name"])
    return ", ".join(names)


def avg_price(hotels):
    total = 0
    for hotel in hotels:
        total += hotel["price"]
    return round(total / len(hotels))

hotels_in_Krakow = [
    {"name": "Sky", "price": 320.00},
    {"name": "Metropol", "price": 480.00},
    {"name": "New Port", "price": 420.00},
    {"name": "Aparthotel", "price": 390.00}
]

hotels_in_Sopot = [
    {"name": "Focus", "price": 510.00},
    {"name": "Aqua", "price": 345.00},
    {"name": "La Boutique", "price": 390.00},
    {"name": "Marina", "price": 410.00}
]

avg_krakow = avg_price(hotels_in_Krakow)
avg_sopot = avg_price(hotels_in_Sopot)

print("Hotels in Krakow:", hotel_list(hotels_in_Krakow))
print("Average hotel price in Krakow:", avg_krakow)

print("Hotels in Sopot:", hotel_list(hotels_in_Sopot))
print("Average hotel price in Sopot:", avg_sopot)

if avg_krakow < avg_sopot:
    print("Cheaper hotels in: Krakow")
elif avg_sopot < avg_krakow:
    print("Cheaper hotels in: Sopot")
else:
    print("Hotel prices are the same in both cities")