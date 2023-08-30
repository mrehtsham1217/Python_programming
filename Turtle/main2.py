import random
from turtle import Turtle, Screen
screen = Screen()


"""def move_forward():
    tk.forward(100)


def move_backward():
    tk.backward(100)


def move_left():
    new_heading = tk.heading()+90
    tk.setheading(new_heading)


def move_right():
    new_heading = tk.heading()-90
    tk.setheading(new_heading)


def clear():
    tk.clear()
    tk.penup()
    tk.home()
    tk.pendown()


screen.listen()
screen.onkey(key="f", fun=move_forward)
screen.onkey(key="b", fun=move_backward)
screen.onkey(key="l", fun=move_left)
screen.onkey(key="r", fun=move_right)
screen.onkey(key="c", fun=clear)"""

is_race_on = False


screen.setup(width=500, height=500)
user_bet = screen.textinput(
    title="Make your Bet", prompt="Which color will win the race? Enter a color")
colors = ['red', 'green', 'yellow', 'blue', 'purple', 'orange']
y_directions = [-80, -40, 0, 40, 80, 120]
Turtle_list = []
for i in range(0, 6):
    tk = Turtle(shape="turtle")
    tk.color(colors[i])
    tk.penup()
    tk.goto(x=-240, y=y_directions[i])
    Turtle_list.append(tk)
print(user_bet)
if user_bet:
    is_race_on = True
while is_race_on:
    for i in Turtle_list:
        if i.xcor() > 230:
            is_race_on = False
            winnig_color = i.pencolor()
            if winnig_color == user_bet:
                print(f"You won {winnig_color} has won the match")
            else:
                print(f"You lost {winnig_color} has won the match")

        random_distance = random.randint(0, 10)
        i.forward(random_distance)

screen.exitonclick()
