import turtle as t
import random

sai = t.Turtle()

t.colormode(255)

def change_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    pick_color = (r, g, b)
    return pick_color

sai.shape("turtle")
sai.speed("fastest")
sai.color(change_color())

def draw_spirograph(size_of_gap):

    for _ in range(int(360 / size_of_gap)):
        sai.color(change_color())
        sai.circle(100)
        sai.setheading(sai.heading() + size_of_gap)

draw_spirograph(5)



screen = t.Screen()
screen.exitonclick()

