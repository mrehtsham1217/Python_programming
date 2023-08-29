from turtle import Turtle
STARTING_POS = (0, -280)
MOV_DISTANCE = 10
FINISH_LINE = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("red")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def move_up(self):
        self.forward(MOV_DISTANCE)

    def move_Down(self):
        self.backward(MOV_DISTANCE)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE:
            return True
        else:
            return False

    def go_to_start(self):
        self.goto(STARTING_POS)
