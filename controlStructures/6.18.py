##
x = int(input("Enter x coordinate of point P: "))
y = int(input("Enter y coordinate of point P: "))

if x > 0:
    if y > 0:
        location = "first quadrant"
    elif y < 0:
        location = "fourth quadrant"
elif x < 0:
    if y > 0:
        location = "second quadrant"
    elif y < 0:
        location = "third quadrant"
else:
    location = "at the origin"    
    
print(f"Point P({x}, {y}) is in the {location}.")
