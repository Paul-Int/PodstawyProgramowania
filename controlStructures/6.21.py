amount = int(input("Enter the amount in PLN: "))

coins_5 = 0
coins_2 = 0
coins_1 = 0

while amount >= 5:
    coins_5 += 1
    amount -= 5

while amount >= 2:
    coins_2 += 1
    amount -= 2

while amount >= 1:
    coins_1 += 1
    amount -= 1

print("The amount in coins:")
print("5 PLN coins:", coins_5)
print("2 PLN coins:", coins_2)
print("1 PLN coins:", coins_1)