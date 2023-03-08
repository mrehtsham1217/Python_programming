# from turtle import Turtle, Screen
# obj1 = Turtle()
# screen = Screen()
# obj1.shape("circle")
# obj1.color("red")
# obj1.forward(100)
# obj1.forward(100)
# obj1.left(90)
# obj1.forward(100)
# obj1.left(90)
# obj1.forward(100)
# obj1.left(90)
# obj1.forward(100)
# for i in range(4):
#     obj1.forward(100)
#     obj1.left(90)
# screen.exitonclick()

# ---------------------------------------------------------------
# from turtle import Turtle, Screen
# obj = Turtle()
# screen = Screen()
# for i in range(15):
#     obj.forward(10)
#     obj.penup()
#     obj.forward(10)
#     obj.pendown()
# screen.exitonclick()
# ------------------------------------------------------
# from turtle import Turtle, Screen
# obj1 = Turtle()
# screen = Screen()
# for i in range(4):
#     obj1.forward(90)
#     obj1.left(90)

# for i in range(6):
#     obj1.forward(72)
#     obj1.left(72)

# screen.exitonclick()

# ------------------------------------------------------------------------------------------------------
# from turtle import Turtle, Screen
# import turtle as t
# import random
# obj1 = Turtle()
# screen = Screen()
# for i  in range(4):
#     obj1.forward(100)
#     obj1.left(90)
# for i in range(15):
#     obj1.forward(10)
#     obj1.penup()
#     obj1.forward(10)
#     obj1.pendown()
# num_side = 8
# for i in range(num_side):
#     angle = 360/num_side
#     obj1.forward(100)
#     obj1.right(angle)


# def shapes(num_sides):
#     angle = 360/num_sides
#     for i in range(num_sides):
#         obj1.forward(100)
#         obj1.right(angle)


# for i in range(3, 11):
#     shapes(i)

# colors = ["medium aquamarine", "red",
#           "royal blue", "dodger blue", "steel blue", "dark turquoise"]
# direction = [0, 90, 180, 270, 360]
# t.colormode(255)


# def RandomColors():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_colors = (r, g, b)
#     return random_colors

# def Shapes(num_sides):
#     angle = 360/num_sides
#     for i in range(num_sides):
#         obj1.forward(100)
#         obj1.left(angle)

# for i in range(3, 11):
#     obj1.color(random.choice(colors))
#     Shapes(i)
# obj1.pensize(15)
# obj1.speed("fastest")
# for i in range(200):
#     obj1.forward(20)
#     obj1.color(RandomColors())
#     obj1.setheading(random.choice(direction))

# screen.exitonclick()
from turtle import Turtle, Screen
import turtle as t
import random
t.colormode(255)


def rgb():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colors = (r, g, b)
    return random_colors


obj1 = Turtle()
screen = Screen()
obj1.pensize(5)
colors = ["medium aquamarine", "red",
          "royal blue", "dodger blue", "steel blue", "dark turquoise"]
direction = [0, 90, 180, 270, 360]

obj1.pensize(15)
obj1.speed("fastest")
for i in range(200):
    obj1.forward(20)
    obj1.color(rgb())
    # obj1.color(random.choice(colors))
    obj1.setheading(random.choice(direction))

# def random_shapes(num_sides):
#     angle = 360/num_sides
#     for i in range(num_sides):
#         obj1.forward(100)
#         obj1.left(angle)


# for i in range(3, 8):
#     obj1.color(random.choice(colors))
#     random_shapes(i)

# for i in range(4):
#     obj1.forward(100)
#     obj1.right(90)


screen.exitonclick()
