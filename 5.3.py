###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = input('a=')
b = input('b=')
c = input('c=')
volume = int(a) * int(b) * int(c)
surface_area = 2 * (int(a) * int(b) + int(a) * int(c) + int(b) * int(c))
print(f'Volume = {volume}')
print(f'Surface Area = {surface_area}')