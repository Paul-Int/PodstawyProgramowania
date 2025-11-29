##
Decimal_num = input("Enter a decimal number: ")

if Decimal_num.isdigit():
    Decimal_num = int(Decimal_num)
    Binary_num = bin(Decimal_num)[2:]
    print(f"{Decimal_num}(10) = {Binary_num}(2)")
else:
    print("Invalid input! Please enter a valid decimal number.")

                        # --- IGNORE ---
number = int(input("Enter decimal number: "))

remainders = []          # lista na reszty z dzielenia
n = number               # kopia liczby

# powtarzamy: dziel przez 2 i zapisuj resztę
while n > 0:
    remainder = n % 2       # reszta
    remainders.append(remainder)
    n = n // 2              # część całkowita z dzielenia

# binarny to reszty od końca
binary = ''.join(str(r) for r in reversed(remainders))

print(f"{number}(10) = {binary}(2)")
