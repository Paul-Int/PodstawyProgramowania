for row in range(1, 8):
    number = row
    for _ in range(7):
        print(number, end=" ")
        number += 7
    print()