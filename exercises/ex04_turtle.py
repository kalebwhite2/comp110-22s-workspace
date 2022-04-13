"""A drawing of my desk. To whoever is grading this: it's still a wip because I know there's a submission form for turtle art and I wanted to have the triangle and ellipses functions working before then, since I needed those two things to keep going with other stuff I have on my desk."""

__author__ = "730409578"

from cmath import pi
from turtle import Screen, Turtle, colormode, done, tracer, update

import math

colormode(255)
screen = Screen()
screen.setup(800, 800)


def main() -> None:
    """Scene entrypoint. The background and window functions do a lot of the work, but the main function is still useful for ordering back to front, so the scene will be correctly filled."""
    tracer(0, 0)
    bob: Turtle = Turtle()

    background(bob)
    window(bob)
    desk(bob)
    
    update()
    done()


def move(turtle: Turtle, x: float, y: float) -> None:
    """Moving the turtle without drawing is utilized all the time, so might as well make it its own function."""
    turtle_filling: bool = turtle.filling()
    if turtle_filling:
        turtle.end_fill()
    turtle.up() 
    turtle.goto(x, y)
    turtle.down()
    if turtle_filling:
        turtle.begin_fill()


def triangle(turtle: Turtle, x: float, y: float, a: float, b: float, angl_c: float, h: float = 0) -> None:
    """Draws a triangle."""
    move(turtle, x, y)
    turtle.setheading(h)

    c: float = math.sqrt(a ** 2 + b ** 2 - 2 * b * a * math.cos(math.radians(angl_c)))
    angl_a: float = math.asin(a * math.sin(math.radians(angl_c)) / c)
    angl_b: float = math.acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c))
    
    turtle.forward(a)
    turtle.right(180 - math.degrees(angl_b))
    turtle.forward(c)
    turtle.right(180 - math.degrees(angl_a))
    turtle.forward(b)
    turtle.goto(x, y)


def ellipse(turtle: Turtle, x: float, y: float, w: float, h: float, rl: bool, full: bool = True, d: float = 0) -> None:
    """Draws a part of a circle, either half or whole. Takes a width and a height as parameters. Can also go right or left."""
    move(turtle, x, y)
    turtle.setheading(d)
    
    sum_cosines: float = 57.7943
    i: int = 0
    while i < 90:
        if rl:
            turtle.goto(turtle.xcor() + (w * math.cos(math.radians(i))) / sum_cosines, turtle.ycor() - ((h * math.sin(math.radians(i)) / (sum_cosines - 1))))
        else:
            turtle.goto(turtle.xcor() + (w * math.cos(math.radians(i))) / sum_cosines, turtle.ycor() + ((h * math.sin(math.radians(i)) / (sum_cosines - 1))))
        i += 1
    if rl:  # So it'll fill in, and won't not fill for a stupid reason
        turtle.goto(x + w, y - h)
    else:
        turtle.goto(x + w, y + h)
    if full:
        while i < 180:  
            if rl:
                turtle.goto(turtle.xcor() + (w * math.cos(math.radians(i))) / sum_cosines, turtle.ycor() - ((h * math.sin(math.radians(i)) / (sum_cosines - 1)))) 
            else:
                turtle.goto(turtle.xcor() + (w * math.cos(math.radians(i))) / sum_cosines, turtle.ycor() + ((h * math.sin(math.radians(i)) / (sum_cosines - 1))))
            i += 1
    if full:
        if rl:
            turtle.goto(x, y - 2 * h)
        else:
            turtle.goto(x, y + 2 * h)


def parabola(turtle: Turtle, h: float, w: float, rl: bool, d: int = 180) -> None:
    """Draws part of a circle. h stands for heading, w for width (or diameter), rl for a bool moving right when true and left when false, and d for degrees of the circle to draw, the default being 180."""
    turtle.setheading(h)
    i: int = 0
    step_radius: float = (1 / 432) * w * pi
    while i < d:
        if rl:
            turtle.right(1)
        elif not False:
            turtle.left(1)
        turtle.forward(step_radius)  
        i += 1


def book(turtle: Turtle, x: float, y: float, w: float, h: float, top: str = "#ffffcc", spine: str = "#800000", side: str = "#802b00") -> None:
    """Draws a book of a given width and height, starting from the top-left corner. Optionally, the color of the top, spine, and side can be chosen."""
    tl_spine_x: float = x - w / 6
    tl_spine_y: float = y - h / 6
    tr_spine_x: float = x + 2 * w / 3
    tr_spine_y: float = y - h / 6
    bl_spine_x: float = x - w / 6
    bl_spine_y: float = y - h
    br_spine_x: float = x + 2 * w / 3
    br_spine_y: float = y - h
    tr_x: float = x + 5 * w / 6
    tr_y: float = y
    br_x: float = x + 5 * w / 6 
    br_y: float = y - 5 * h / 6
    
    move(turtle, x, y)

    move(turtle, tl_spine_x, tl_spine_y)
    turtle.fillcolor(spine)  # Drawing the spine.
    turtle.begin_fill()
    turtle.goto(bl_spine_x, bl_spine_y)
    parabola(turtle, 270, w, False)
    turtle.goto(br_spine_x, br_spine_y)
    turtle.goto(tr_spine_x, tr_spine_y)
    parabola(turtle, 270, w, True)
    turtle.goto(tl_spine_x, tl_spine_y)
    turtle.end_fill()

    move(turtle, br_spine_x, br_spine_y)
    turtle.fillcolor(side)  # Drawing the side.
    turtle.begin_fill()
    turtle.goto(br_x, br_y)
    turtle.goto(tr_x, tr_y)
    turtle.goto(tr_spine_x, tr_spine_y)
    turtle.goto(br_spine_x, br_spine_y)
    turtle.end_fill()

    move(turtle, x, y)
    turtle.fillcolor(top)  # Drawing the top. Back to front, so top has to be left. 
    turtle.begin_fill()
    turtle.goto(tl_spine_x, tl_spine_y)
    parabola(turtle, 270, w, False)
    turtle.goto(tr_spine_x, tr_spine_y)
    turtle.goto(tr_x, tr_y)
    turtle.goto(x, y)
    turtle.end_fill()


def p_rectangle(turtle: Turtle, x: float, y: float, h: float, w: float, d: float, ad: float, fill: bool) -> None:
    """Perspective rectangle. Takes a height, width, depth, and angle of depth."""
    move(turtle, x, y)
    
    tr_x: float = x + w
    tr_y: float = y
    bl_x: float = x
    bl_y: float = y - h
    br_x: float = x + w
    br_y: float = y - h
    
    if fill:
        turtle.begin_fill()
    turtle.goto(tr_x, tr_y)
    turtle.goto(br_x, br_y)
    turtle.goto(bl_x, bl_y)
    turtle.goto(x, y)
    if fill:
        turtle.end_fill()

    if ad < 90:  # right side
        move(turtle, br_x, br_y)

        o_br_x: float = br_x + d * math.cos(math.radians(ad))
        o_br_y: float = br_y + d * math.sin(math.radians(ad))
        o_tr_x: float = tr_x + d * math.cos(math.radians(ad))
        o_tr_y: float = tr_y + d * math.sin(math.radians(ad))
        o_tl_x: float = x + d * math.cos(math.radians(ad))
        o_tl_y: float = y + d * math.sin(math.radians(ad))

        if fill:
            turtle.begin_fill()
        turtle.goto(o_br_x, o_br_y)
        turtle.goto(o_tr_x, o_tr_y)
        turtle.goto(o_tl_x, o_tl_y)
        turtle.goto(x, y)

        move(turtle, tr_x, tr_y)

        turtle.goto(o_tr_x, o_tr_y)
        if fill:
            turtle.end_fill()

    elif ad > 90:  # left side
        move(turtle, bl_x, bl_y)

        o_bl_x_l: float = bl_x + d * math.cos(math.radians(ad))  # Outside, position on square, x or y coordinate, left side
        o_bl_y_l: float = bl_y + d * math.sin(math.radians(ad))
        o_tl_x_l: float = x + d * math.cos(math.radians(ad))
        o_tl_y_l: float = y + d * math.sin(math.radians(ad))
        o_tr_x_l: float = tr_x + d * math.cos(math.radians(ad))
        o_tr_y_l: float = tr_y + d * math.sin(math.radians(ad))

        if fill:
            turtle.begin_fill()
        turtle.goto(o_bl_x_l, o_bl_y_l)
        turtle.goto(o_tl_x_l, o_tl_y_l)
        turtle.goto(o_tr_x_l, o_tr_y_l)
        turtle.goto(tr_x, tr_y)

        move(turtle, x, y)

        turtle.goto(o_tl_x_l, o_tl_y_l)
        if fill:
            turtle.end_fill()


def background(turtle: Turtle) -> None:
    """Draws a gradient blue-sky background."""
    move(turtle, -400, 400)
    i: int = 0
    g: int = 100
    turtle.pencolor(0, g, 255)
    while i < 60:
        ii: int = 0
        while ii < 5:
            turtle.forward(800)
            turtle.right(90)
            turtle.forward(1)
            turtle.right(90)
            turtle.forward(800)
            turtle.left(90)
            turtle.forward(1)
            turtle.left(90)
            ii += 1
        g += 2
        turtle.pencolor(0, g, 255)
        i += 1
    turtle.pencolor(0, 0, 0)


def window(turtle: Turtle) -> None:
    """Draws the window and wood surrounding it."""
    p_rectangle(turtle, -240, 320, 400, 560, 0, 0, False)  # Window itself
    turtle.fillcolor(200, 200, 200)
    p_rectangle(turtle, 35, 320, 400, 10, 0, 0, True)
    p_rectangle(turtle, -95, 320, 400, 10, 0, 0, True)
    p_rectangle(turtle, 175, 320, 400, 10, 0, 0, True)
    p_rectangle(turtle, -240, 115, 10, 560, 0, 0, True)

    turtle.fillcolor(224, 224, 224)  # Wood at the bottom of the window
    p_rectangle(turtle, -400, -135, 25, 800, 0, 0, True)
    turtle.fillcolor(230, 230, 230) 
    p_rectangle(turtle, -410, -125, 10, 800, 70, 30, True)
    move(turtle, -400, -125)
    turtle.goto(400, -125)
    turtle.fillcolor(255, 240, 200)
    p_rectangle(turtle, -280, -90, 10, 640, math.cos(math.radians(30)) * 22, 30, True)  
    move(turtle, -300, -90)
    turtle.goto(400, -90)
    move(turtle, 360, -90)
    turtle.goto(360, -100)

    turtle.fillcolor(230, 230, 230)  # Left side wood
    p_rectangle(turtle, -400, 400, 520, 50, 11.547, 30, True)
    move(turtle, -350, 400)
    turtle.goto(-350, -120)
    p_rectangle(turtle, -340, 400, 500, 50, 11.547, 30, True)
    move(turtle, -290, 400)
    turtle.goto(-290, -100)
    turtle.fillcolor(255, 240, 200)
    p_rectangle(turtle, -280, 400, 490, 10, 5.774, 30, True)
    move(turtle, -270, 400)
    turtle.goto(-270, -90)
    p_rectangle(turtle, -265, 400, 480, 25, 0, 0, True)

    turtle.fillcolor(230, 230, 230)  # Right side
    p_rectangle(turtle, 370, 400, 500, 50, 11.547, 150, True)
    move(turtle, 370, 400)
    turtle.goto(370, -100)
    turtle.fillcolor(255, 240, 200)
    p_rectangle(turtle, 350, 400, 490, 10, 5.774, 150, True)
    move(turtle, 350, 400)
    turtle.goto(350, -90)
    p_rectangle(turtle, 320, 400, 480, 25, 0, 0, True)

    turtle.fillcolor(139, 69, 19)  # Blinds TODO: add string
    p_rectangle(turtle, -335, 400, 20, 740, 0, 0, True)  # Top blind
    turtle.fillcolor(165, 42, 42)
    i: int = 0
    height0: int = 380
    while i < 13:  # The part of the blinds that are stacked since the blinds are pulled up
        p_rectangle(turtle, -332, height0, 3, 740, 0, 0, True)
        height0 -= 3
        i += 1
    turtle.fillcolor(224, 111, 31)
    p_rectangle(turtle, -335, 340, 20, 740, 0, 0, True)  # Bottom blind

    def strings(turtle: Turtle, x: float, y: float, h: int) -> None:
        """Draws the strings on the blinds."""  # TODO: Finish
        move(turtle, x, y - h)
        turtle.dot(6, "black")
        move(turtle, x, y - h + 3)
        turtle.pensize(2)
        turtle.pencolor(128, 64, 0)

        turtle.goto(x, y - h + 10)  # Takes the turtle to the top of the lowest blind
        parabola(turtle, 90, 12, False)
        i: int = 0
        while i < 3:  # Janky and not really what I wanted but it'll do
            parabola(turtle, 180, 12, True)
            turtle.goto(turtle.xcor() + 10, turtle.ycor() - 6)
            parabola(turtle, 0, 12, False)
            turtle.goto(turtle.xcor() - 10, turtle.ycor() + 4)
            i += 1
        turtle.goto(turtle.xcor(), turtle.ycor() + 10)
        
        turtle.pencolor(0, 0, 0)
        turtle.pensize(1)

    strings(turtle, -340 + (370 / 6), 400, 70)
    strings(turtle, -340 + (370 / 6) + (370 / 3), 400, 70)
    strings(turtle, -340 + (370 / 6) + 2 * (370 / 3), 400, 70)
    strings(turtle, -340 + (370 / 6) + 3 * (370 / 3), 400, 70)
    strings(turtle, -340 + (370 / 6) + 4 * (370 / 3), 400, 70)
    strings(turtle, -340 + (370 / 6) + 5 * (370 / 3), 400, 70)


def desk(turtle: Turtle) -> None:
    """Draws the desk."""
    turtle.fillcolor(206, 149, 75)  # Desk TODO: If time, add wood patterns
    p_rectangle(turtle, -400, -160, 560, 800, 0, 0, True)
    book(turtle, -380, -100, 20, 100)
    book(turtle, -357, -100, 40, 100)
    book(turtle, -310, -80, 30, 120)
    book(turtle, -280, -80, 30, 120)
    book(turtle, -250, -90, 35, 110)
    book(turtle, -215, -110, 20, 90)

    def sq_pots(turtle: Turtle, x: float, y: float, m: float = 1) -> None:
        """Built to draw two little square pots at the back of the desk. Takes and x-coordinate, y-coordinate, and size multiplier."""
        turtle.fillcolor(169, 169, 169)
        p_rectangle(turtle, x, y, m * 40, m * 60, 5.774, 60, True)
        move(turtle, x, y)
        turtle.goto(x + 60, y)
       
        turtle.fillcolor(81, 21, 21)  # Filling it in
        p_rectangle(turtle, x + m, y - m, m * 35, m * 55, 0, 0, True)
        turtle.fillcolor(169, 169, 169)
        
        p_rectangle(turtle, x - m * 10, y - m * 20, m * 40, m * 5, 22, 60, True)
        p_rectangle(turtle, x + m * 44, y - m * 20, m * 40, m * 5, 22, 60, True)
        p_rectangle(turtle, x - m * 10, y - m * 20, m * 40, m * 60, 5.774, 60, True)
        move(turtle, x - m * 10, y - m * 20)
        turtle.goto(x - m * 10 + m * 60, y - m * 20)
        move(turtle, x - m * 10 + m * 60, y - m * 20)
        turtle.goto(x - m * 10 + m * 60, y - m * 20 - m * 40)

    sq_pots(turtle, -160, -150)
    sq_pots(turtle, -90, -150)

    def bookshelf(turtle: Turtle, x: float, y: float, m: float = 1) -> None:
        """Draws books from right to left, and then shelf pattern in the same way."""
        #  TODO: Change fill color
        p_rectangle(turtle, x + m * 200, y, m * 180, m * 10, 5.774, 150, True)
        move(turtle, x + m * 200, y)  # I am an idiot for not including these in the rectangle function
        turtle.goto(x + m * 200, y - m * 180)
        p_rectangle(turtle, x + m * 150, y, m * 144, m * 10, 5.774, 156, True)
        move(turtle, x + m * 150, y)
        turtle.goto(x + m * 150, y - m * 144)
        p_rectangle(turtle, x + m * 60, y - m * 144, m * 10, m * 140, 5.774, 150, True)
        move(turtle, x + m * 60, y - m * 144)
        turtle.goto(x + m * 200, y - m * 144)
        p_rectangle(turtle, x + m * 50, y - m * 46, m * 134, m * 10, 5.774, 162, True)
        move(turtle, x + m * 50, y - m * 46)
        turtle.goto(x + m * 50, y - m * 180)
        p_rectangle(turtle, x + m * 10, y - m * 36, m * 10, m * 140, 5.774, 150, True)
        move(turtle, x + m * 10, y - m * 36)
        turtle.goto(x + m * 150, y - m * 36)
        p_rectangle(turtle, x, y, m * 180, m * 10, 5.774, 170, True)
        move(turtle, x, y)
        turtle.goto(x, y - m * 180)

    bookshelf(turtle, 100, 20, 1.25)


if __name__ == "__main__":
    main()