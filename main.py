import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkeypress(player.move_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()


    for car in car_manager.all_cars:
       if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.is_at_finish():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.plus_score()
    



screen.exitonclick()