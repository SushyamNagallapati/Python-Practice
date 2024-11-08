import turtle as t
import random


color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]


sai = t.Turtle()
t.colormode(255)

sai.speed("fastest")
sai.penup()
sai.hideturtle()

sai.setheading(225)
sai.forward(300)
sai.setheading(0)


number_of_dots = 100


for dot_count in range(1, number_of_dots + 1):
    sai.color(random.choice(color_list))
    sai.forward(50)
    sai.dot(20)
    if dot_count % 10 == 0:

        sai.setheading(90)
        sai.forward(50)
        sai.setheading(180)
        sai.forward(500)
        sai.setheading(0)


screen = t.Screen()
screen.exitonclick()

