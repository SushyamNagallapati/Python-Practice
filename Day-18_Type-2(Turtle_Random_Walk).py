from turtle import Turtle, Screen
import random

sai = Turtle()

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

direction = [0, 90, 180, 270]

sai.pensize(10)
sai.speed("fastest")
sai.shape("turtle")

for _ in range(200):
    sai.color(random.choice(colors))
    sai.forward(30)
    sai.setheading(random.choice(direction))








screen = Screen()
screen.exitonclick()
