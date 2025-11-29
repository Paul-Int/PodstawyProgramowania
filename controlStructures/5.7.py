###
# Takes a number from the user and counts down to zero.
#
# Modify the program so that the last five seconds of the counter
# are displayed in words, i.e. five, four, three, two, one.
#
import time

countdown = int(input("Enter the number of seconds to count down: "))

while countdown > 0:
    print(countdown)
    countdown -= 1
    time.sleep(1)  # Wait for 1 second
    if countdown == 5:  
        print("five")
        time.sleep(1)
        print("four")
        time.sleep(1)
        print("three")
        time.sleep(1)
        print("two")
        time.sleep(1)
        print("one")
        time.sleep(1)
        break
print("Time's up!")