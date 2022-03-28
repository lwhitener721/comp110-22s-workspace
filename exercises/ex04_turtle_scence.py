"""A beautiful forest scence."""

__author__ = "730479707"


from turtle import Turtle, colormode, done
michelangelo: Turtle = Turtle()
michelangelo.speed(100)


def tree_trunk() -> None:
    """Draw a stack of squares that creates a tree trunk."""
    colormode(255)
    michelangelo.color(87, 59, 0)
    michelangelo.begin_fill()
    i: int = 0 
    while (i < 4):
        michelangelo.forward(100)
        michelangelo.right(90)
        i = i + 1
    j: int = 0
    while (j < 4):
        michelangelo.forward(100)
        michelangelo.left(90)
        j = j + 1
    michelangelo.penup
    michelangelo.goto(0, 200)
    michelangelo.pendown
    p: int = 0 
    while (p < 4):
        michelangelo.forward(100)
        michelangelo.right(90)
        p = p + 1
    michelangelo.end_fill()


def leaves() -> None:
    """Draw a triangle that is the leaves on a tree."""
    colormode(255)
    michelangelo.color(19, 97, 6)
    michelangelo.begin_fill()
    michelangelo.penup
    michelangelo.goto(-50, 200)
    michelangelo.pendown
    i: int = 0 
    while (i < 3):
        michelangelo.forward(200)
        michelangelo.left(120)
        i = i + 1
    michelangelo.end_fill()


def waterfall() -> None:
    """Draw a stream beneath the trees and rocks."""
    colormode(255)
    michelangelo.color(8, 92, 223)
    michelangelo.begin_fill()
    michelangelo.penup()
    michelangelo.goto(-225, 150)
    michelangelo.pendown()
    k: int = 0 
    while (k < 4):
        michelangelo.forward(130)
        michelangelo.right(90)
        k = k + 1
    michelangelo.end_fill()
    michelangelo.begin_fill()
    michelangelo.penup()
    michelangelo.goto(-225, 50)
    michelangelo.pendown()
    line: int = 0 
    while (line < 4):
        michelangelo.forward(130)
        michelangelo.right(90)
        line = line + 1
    michelangelo.end_fill()
    michelangelo.begin_fill()
    michelangelo.penup()
    michelangelo.goto(-225, -50)
    michelangelo.pendown()
    m: int = 0 
    while (m < 4):
        michelangelo.forward(130)
        michelangelo.right(90)
        m = m + 1
    michelangelo.end_fill()

    michelangelo.begin_fill()
    michelangelo.penup()
    michelangelo.goto(-100, -100)
    michelangelo.pendown()
    a: int = 0 
    while (a < 4):
        michelangelo.forward(50)
        michelangelo.right(90)
        a = a + 1
    michelangelo.end_fill()
    michelangelo.penup()
    michelangelo.goto(-50, -120)
    michelangelo.pendown()
    michelangelo.begin_fill()
    p: int = 0 
    while (p < 4):
        michelangelo.forward(50)
        michelangelo.right(90)
        p = p + 1
    michelangelo.end_fill()
    michelangelo.penup()
    michelangelo.goto(-2, -150)
    michelangelo.pendown()
    michelangelo.begin_fill()
    x: int = 0 
    while (x < 4):
        michelangelo.forward(50)
        michelangelo.right(90)
        x = x + 1
    michelangelo.end_fill()


def rocks() -> None:
    """Rocks at the top of the waterfall."""
    colormode(255)
    michelangelo.color(67, 68, 70)
    michelangelo.begin_fill()
    michelangelo.penup()
    michelangelo.goto(-200, 200)
    michelangelo.pendown()
    michelangelo.circle(40)
    michelangelo.position()
    (-50.00, 10.00)
    michelangelo.end_fill()

    michelangelo.penup()
    michelangelo.goto(-180, 150)
    michelangelo.pendown()

    michelangelo.begin_fill()
    michelangelo.circle(40)
    michelangelo.position()
    (-50.00, 10.00)
    michelangelo.end_fill()

    michelangelo.penup()
    michelangelo.goto(-225, 150)
    michelangelo.pendown()

    michelangelo.begin_fill()
    michelangelo.circle(40)
    michelangelo.position()
    (-50.00, 10.00)
    michelangelo.end_fill()


def main() -> None:
    tree_trunk()
    rocks()
    leaves()
    waterfall()
    done()


if __name__ == "__main__":
    main()