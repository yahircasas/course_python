#
# my_num = int(input('Enter a number: '))
# my_num2= int(input('Enter another number: '))
#
# print(my_num+my_num2)

import turtle
import math
window = turtle.Screen()
window.bgcolor("light blue")
window.title("Girasol")

def draw_petal(radius):
    turtle.circle(radius, 60)
    turtle.left(120)
    turtle.circle(radius, 60)
    turtle.left(120)

def draw_sunflower():
    turtle.speed(0)  # Velocidad máxima
    turtle.color("orange")
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()
    turtle.color("yellow")
    num_petals = 18
    angle = 360 / num_petals
    petal_radius = 80

    for _ in range(num_petals):
        turtle.penup()
        turtle.goto(0, 20)
        turtle.pendown()
        draw_petal(petal_radius)
        turtle.left(angle)

    turtle.hideturtle()
draw_sunflower()

window.mainloop()
