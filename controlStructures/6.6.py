##  
# program that calculates the parking fee based on the number of hours parked.
#

hours_parked = int(input("Enter the number of hours parked: "))
fee = 0 
if hours_parked <=2 >= 1:
    fee = 5
elif hours_parked <=6 >= 3:
    fee = 15
else:
    fee = 20    
    print(f"The parking fee is: ${fee}")