from turtle import Turtle, Screen, colormode
import random
tk = Turtle()
cmood = colormode(255)
# tk.shape("turtle")
# tk.color("red")
# Witout using loop
"""tk.forward(100)
tk.left(90)
tk.forward(100)
tk.left(90)
tk.forward(100)
tk.left(90)
tk.forward(100)
tk.left(90)
# circle with using loops
for i in range(4):
    tk.forward(100)
    tk.left(90)

# desh line
for i in range(10):
    tk.forward(10)
    tk.penup()
    tk.forward(10)
    tk.pendown()

#-----------------------------------
def shapes(sides):
    angle = 360/sides
    for i in range(sides):
        tk.forward(100)
        tk.left(angle)


# sides = int(input("Enter number of sides"))
for i in range(3, 6):
    shapes(i)"""


"""no_of_side = 5
for i in range(no_of_side):
    angle = 360/no_of_side
    tk.forward(100)
    tk.left(angle)"""

# ----------------------make a random walk in python------------------->


def random_colours():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


"""
# colors = ['CornflowerBlue', 'DarkOrchid', 'IndianRed',
    #   'DeepSkyBlue', 'LightSeaGreen', 'wheat']
# tk.colormode(255)
directions = [0, 90, 180, 270]
tk.pensize(10)
tk.speed("fast")
for i in range(100):
    # tk.color(random.choice(colors))
    tk.color(random_colours())
    tk.forward(30)
    tk.setheading(random.choice(directions))"""

# ------------>Drawing the circle---------------->
tk.speed("fastest")


def draw_spirograph(gap):
    for i in range(int(360/gap)):
        tk.color(random_colours())
        tk.circle(100)
        current_head = tk.heading()
        tk.setheading(current_head+gap)


# tk.circle(100)
draw_spirograph(5)

screen = Screen()
screen.exitonclick()
