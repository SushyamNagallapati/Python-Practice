import turtle as t
from turtle import Screen
import random

sai = t.Turtle()

t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

direction = [0, 90, 180, 270]

sai.pensize(10)
sai.speed("fastest")
sai.shape("turtle")

for _ in range(200):
    sai.color(random_color())
    sai.forward(30)
    sai.setheading(random.choice(direction))




screen = Screen()
screen.exitonclick()
