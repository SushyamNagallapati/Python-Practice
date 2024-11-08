from turtle import Turtle, Screen
import random

sai = Turtle()

colors = ["red", "pink", "orange", "purple", "blue", "black", "green", "pale green"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        sai.forward(100)
        sai.right(angle)

for shape in range(3, 11):
    sai.color(random.choice(colors))
    draw_shape(shape)




screen = Screen()
screen.exitonclick()



