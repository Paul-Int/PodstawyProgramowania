###
# A program that prints your height both in cm and in feet and inches.
#
cm = 181
feet = cm // 30.48
inches = (cm % 30.48) / 2.54
# calculate the number of feet and inches from cm

print(f'I am {cm}cm tall, i.e. {feet:.0f} feet and {inches:.0f} inches')