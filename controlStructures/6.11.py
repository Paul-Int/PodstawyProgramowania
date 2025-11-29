###

current_price = 190.00
previous_price = 200.00

print("Current product price:", current_price)
print("Previous product price:", previous_price)

discount = previous_price - current_price
percent_discount = (discount / previous_price) * 100    

if percent_discount >= 10:
    print("Buy the product!!")
    print(f"You saved {percent_discount:.0f}%")
else:
    print("no recomendation.")
    print(f"Discount is only {percent_discount:.0f}%")