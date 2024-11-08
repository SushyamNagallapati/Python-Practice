from turtle import Turtle, Screen

sai = Turtle()
sus = Turtle()
naruto = Turtle()
luffy = Turtle()
kira = Turtle()
muza = Turtle()
tanjiro = Turtle()
hashirama = Turtle()
sai.shape("turtle")

sus.shape("turtle")

naruto.shape("turtle")

luffy.shape("turtle")

kira.shape("turtle")

muza.shape("turtle")

tanjiro.shape("turtle")

hashirama.shape("turtle")


sai.pen(fillcolor="white", pencolor="violet", pensize=5)
sus.pen(fillcolor="white", pencolor="indigo", pensize=5)
naruto.pen(fillcolor="white", pencolor="blue", pensize=5)
luffy.pen(fillcolor="white", pencolor="green", pensize=5)
kira.pen(fillcolor="white", pencolor="yellow", pensize=5)
muza.pen(fillcolor="white", pencolor="orange", pensize=5)
tanjiro.pen(fillcolor="white", pencolor="red", pensize=5)
hashirama.pen(fillcolor="white", pencolor="coral", pensize=5)


turtle.bgcolor("black")

for _ in range(3):
    sai.forward(100)
    sai.right(120)

for _ in range(4):
    sus.forward(100)
    sus.right(90)

for _ in range(5):
    naruto.forward(100)
    naruto.right(72)

for i in range(6):
    luffy.forward(100)
    luffy.right(60)

for i in range(7):
    kira.forward(100)
    kira.right(51.42)

for i in range(8):
    muza.forward(100)
    muza.right(45)

for i in range(9):
    tanjiro.forward(100)
    tanjiro.right(40)

for i in range(10):
    hashirama.forward(100)
    hashirama.right(36)



screen = Screen()
screen.exitonclick()



