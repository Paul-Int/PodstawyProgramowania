###
# program for calculating the distance to the horizon
###
import math

h = 1.8 # height of the observer in meters
h2 = 20 # height of the window in meters
d = 3.57 * math.sqrt(h)
d2 = 3.57 * math.sqrt(h2)
distance_km = d # distance in kilometers
height_m = h # height in meters
height_window_m = h2 # height of the window in meters
distance_window_km = d2 # distance to the horizon from the window in kilometers
print ("Height of the observer:", height_m, "m")
print ("Distance to the horizon from a person:", distance_km, "km")
print ("Height of the window:", height_window_m, "m")
print ("Distance to the horizon from the window:", distance_window_km, "km")
