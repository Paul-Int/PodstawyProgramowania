###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

# Read temperature in degrees Celsius from the keyboard
celsius = float(input('Enter temperature in degrees Celsius: '))
# Convert temperature to degrees Fahrenheit and Kelvin
fahrenheit = celsius * 9 / 5 + 32
kelvin = celsius + 273.15
# Print the result
print(f'Temperature in Fahrenheit: {fahrenheit} °F') 
print(f'Temperature in Kelvin: {kelvin} K')