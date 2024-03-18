import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()

screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")

game_is_on = True

time_to_sleep = 0.1

while game_is_on:
    time.sleep(time_to_sleep)
    screen.update()
    scoreboard.update_scoreboard()

    car_manager.create_car()
    car_manager.move_cars()

    #detecting collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            
            scoreboard.game_over()


    #Detect succesful crossing
    if player.is_at_finish_line():
        scoreboard.level_up()
        player.go_to_start()
        time_to_sleep *= 0.7
        
    


screen.exitonclick()