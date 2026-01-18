import json


def load_reservations(filename):
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data["reservations"]


def number_of_rooms(reservations):
    rooms = set()
    for r in reservations:
        rooms.add(r["room_number"])
    return len(rooms)


def count_paid(reservations):
    paid = 0
    for r in reservations:
        if r["paid"] is True:
            paid += 1
    return paid


def count_unpaid(reservations):
    unpaid = 0
    for r in reservations:
        if r["paid"] is False:
            unpaid += 1
    return unpaid


def total_value_paid(reservations):
    total = 0.0
    for r in reservations:
        if r["paid"] is True:
            total += r["nights"] * r["price_per_night"]
    return total


def total_value_unpaid(reservations):
    total = 0.0
    for r in reservations:
        if r["paid"] is False:
            total += r["nights"] * r["price_per_night"]
    return total


reservations = load_reservations("reservations.json")

print("Number of rooms:", number_of_rooms(reservations))
print("Number of paid reservations:", count_paid(reservations))
print("Number of unpaid reservations:", count_unpaid(reservations))
print("Total value of paid reservations:", round(total_value_paid(reservations), 2))
print("Total value of unpaid reservations:", round(total_value_unpaid(reservations), 2))