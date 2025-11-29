
speed_limit_min = 40
speed_limit_max = 140

car_speed = int(input("Enter car speed: "))

if speed_limit_min <= car_speed <= speed_limit_max:
    print("The car is within the speed limit.")
else:
    print("Warning! Invalid car speed!")