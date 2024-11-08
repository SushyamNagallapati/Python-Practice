from turtle import Turtle, Screen
import random

sai = Turtle()

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
move = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]

sai.pen(speed=10, pensize=10)

for _ in range(1000):
    direction = random.choice(["left", "right"])

    if direction == "left":
        sai.left(90)
    else:
        sai.right(90)
  
    sai.color(random.choice(colors))
    sai.forward(random.choice(move))







screen = Screen()
screen.exitonclick()
