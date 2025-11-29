from datetime import datetime

time_input = input("Enter time (24-hour format HH:MM): ")
time_24 = datetime.strptime(time_input, "%H:%M")
time_12 = time_24.strftime("%I:%M %p")

print(f"Time in 12-hour format: {time_12}")
