from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
# leo.forward(300)
# leo.left(90)
# leo.forward(300)
# leo.left(90)
# leo.forward(300)
# leo.left(90)
# leo.forward(300)
# leo.left(90)

# i: int = 0 
# while (i < 4):
#     leo.forward(300)
#     leo.left(90)
#     i = i + 1

# i: int = 0 
# while (i < 3):
#     leo.forward(300)
#     leo.left(120)
#     i = i + 1

# <turtlevariable>.goto(<x_coordinate>,<y_coordinate>):
# leo.goto(45, 60)
# To prevent the turtle from drawing: <turtlevariable>.penup() or <turtlevariable>.up() To allow the turtle to draw: <turtlevariable>.pendown() or <turtlevariable>.down()

# leo.penup()
# leo.goto(45, 60)
# leo.pendown()

i: int = 0 
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1

# To change the color with a string value: <turtlevariable>.color(“<color>”)

# leo.color("blue")

# colormode(255)

# leo.speed(50)
# leo.hideturtle()

bob: Turtle = Turtle()

done()
