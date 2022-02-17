"""For figuring out the magnitude of the sum of a set of cosines."""

from turtle import Turtle, done, tracer, update
import math
from ex04_turtle import move


def ellipse(turtle: Turtle, x: float, y: float, w: float, h: float, rl: bool, full: bool = True, d: float = 0) -> None:
    """Draws a part of a circle, either half or whole. Takes a width and a height as parameters. Can also go right or left."""
    move(turtle, x, y)
    turtle.setheading(d)
    
    sum_cosines: float = 57.7943
    i: int = 0
    while i < 90:
        if rl:
            turtle.setheading(d)
            turtle.forward((w * math.cos(math.radians(i))) / sum_cosines)
            turtle.setheading(d - 90) 
            turtle.forward((h * math.sin(math.radians(i)) / (sum_cosines - 1)))
        else:
            turtle.setheading(d)
            turtle.forward((w * math.cos(math.radians(i))) / sum_cosines)
            turtle.setheading(d + 90) 
            turtle.forward((h * math.sin(math.radians(i)) / (sum_cosines - 1)))
        i += 1
    if rl:  # So it'll fill in, and won't not fill for a stupid reason
        turtle.goto(x + w, y - h)
    else:
        turtle.goto(x + w, y + h)
    if full:
        while i < 180:  
            if rl:
                turtle.setheading(d)
                turtle.forward((w * math.cos(math.radians(i))) / sum_cosines)
                turtle.setheading(d - 90) 
                turtle.forward((h * math.sin(math.radians(i)) / (sum_cosines - 1)))
            else:
                turtle.setheading(d)
                turtle.forward((w * math.cos(math.radians(i))) / sum_cosines)
                turtle.setheading(d + 90) 
                turtle.forward((h * math.sin(math.radians(i)) / (sum_cosines - 1)))
            i += 1
    if full:
        if rl:
            turtle.goto(x, y - 2 * h)
        else:
            turtle.goto(x, y + 2 * h)


tracer(0, 0)
turtle: Turtle = Turtle()
ellipse(turtle, 0, 0, 50, 20, False, True)
ellipse(turtle, turtle.xcor(), turtle.ycor(), 50, 20, False, True, 90)
print(turtle.xcor())
print(turtle.ycor())
update()
done()