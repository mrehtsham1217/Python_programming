from turtle import Turtle, Screen
import time
# Import all the classes here
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
# Make all the Obejcts here
player = Player()
car_manager = CarManager()
score_board = ScoreBoard()


screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_Down, "Down")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()
    for cars in car_manager.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False
            score_board.game_over()
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        score_board.update_level()

screen.exitonclick()
