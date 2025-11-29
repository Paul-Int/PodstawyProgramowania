##
EAN = input("Enter EAN-13 article number: ")


if EAN.isdigit() and len(EAN) == 13:
    print("The EAN-13 article number is valid.")
    if EAN.startswith('590'):
        print("The article is from Poland.")     
else:
    print("The EAN-13 article number is invalid.")    