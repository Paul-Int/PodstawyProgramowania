##
# calculating price with discount and the difference between prices
price = float(input('Enter price:  '))
discount = float(input('Enter discount %:  '))
discountedPrice = price - (price * discount / 100)
difference = price - discountedPrice
print(f'Price with discount: {discountedPrice:.2f}')
print(f'Reduction: {difference:.2f}')