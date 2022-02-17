"""Turtle."""

from turtle import Turtle, colormode, done
colormode(255)

side_length: float = 300


def triangle(turtlename: Turtle) -> None:
    i: int = 0
    while i < 3:  
        turtlename.forward(side_length)
        turtlename.left(120)
        i += 1


leo: Turtle = Turtle()

leo.color(50, 50, 50)
leo.speed(50)
leo.hideturtle()

leo.penup()
leo.goto(-150, -150)
leo.down()

leo.begin_fill()
triangle(leo)
leo.end_fill()
done()

bob: Turtle = Turtle()

bob.color(0, 0, 0)
bob.speed(50)
bob.hideturtle()

bob.up()
bob.goto(-150, -150)
bob.down()

ind: int = 0
while (ind < 20):
    triangle(bob)
    side_length *= 0.97
    ind += 1
