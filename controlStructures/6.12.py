###
number_of_products = int(input("Number of products purchased: "))
product_price = float(input("Product price: "))

amount_to_pay = number_of_products * product_price

if number_of_products <= 2:
    amount_to_pay = number_of_products * product_price
else:     
    normal_price = 2 * product_price
    
    discounted_products = number_of_products - 2
    discounted_price = product_price * 0.75
    
    amount_to_pay = normal_price + discounted_products * discounted_price
    
print(f"Total amount to pay: {amount_to_pay}")    
    