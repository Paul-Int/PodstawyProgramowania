
for i in range(1, 4):
    PIN_code = int(input("Enter the PIN code: "))
    if PIN_code == 1234:
        print("PIN accepted")
        break
    else:
        print("Incorrect PIN")
else:
    print("Sorry, your payment card has been blocked.")