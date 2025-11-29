##  
# write a program that checks whether the vehicle speed is correct
# 
speed = input('Enter vehicle speed in km/h: ')
speed_ok = int(speed) >= 40 and int(speed) <= 140
print(f'Vehicle speed is correct: {speed_ok}')