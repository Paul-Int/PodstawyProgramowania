# figures.py
import turtle

def draw_square(pen, length):
    for _ in range(4):
        pen.forward(length)
        pen.right(90)

def draw_triangle(pen, length):
    # trójkąt równoramienny (tu: rysujemy równoboczny, bo "length" jednoznacznie to określa)
    for _ in range(3):
        pen.forward(length)
        pen.left(120)

def draw_rectangle(pen, lenght_a, lenght_b):
    # Uwaga: w poleceniu jest literówka "lenght" — zostawiam jak w zadaniu
    for _ in range(2):
        pen.forward(lenght_a)
        pen.right(90)
        pen.forward(lenght_b)
        pen.right(90)