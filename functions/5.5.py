###
# Draws each of the figures (square, triangle, rectangle) twice,
# in different locations
#
import turtle
import figures

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)

# move without drawing
def move_to(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()

# SQUARE twice
move_to(-200, 150)
figures.draw_square(pen, 80)

move_to(50, 150)
figures.draw_square(pen, 80)

# TRIANGLE twice
move_to(-200, 0)
figures.draw_triangle(pen, 80)

move_to(50, 0)
figures.draw_triangle(pen, 80)

# RECTANGLE twice
move_to(-200, -150)
figures.draw_rectangle(pen, 120, 60)

move_to(50, -150)
figures.draw_rectangle(pen, 120, 60)

# finish
pen.hideturtle()
window.mainloop()