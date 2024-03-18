from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 265


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        new_y_cord = self.ycor() + MOVE_DISTANCE
        if new_y_cord < 280:
            self.goto(self.xcor(), new_y_cord )

    def move_down(self):
        new_y_cord = self.ycor() - MOVE_DISTANCE
        if new_y_cord > -280:
            self.goto(self.xcor(), new_y_cord )

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False