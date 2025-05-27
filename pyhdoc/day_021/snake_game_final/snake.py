# Snake class for snake game

from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.color("green")
        self.direction = RIGHT
        self.can_change_direction = True

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        # Allow direction change only AFTER moving
        self.can_change_direction = True
        

    def up(self):
        if self.head.heading() != DOWN and self.can_change_direction:
            self.head.setheading(UP)
            self.direction = UP
            self.can_change_direction = False

    def down(self):
        if self.head.heading() != UP and self.can_change_direction:
            self.head.setheading(DOWN)
            self.direction = DOWN
            self.can_change_direction = False

    def left(self):
        if self.head.heading() != RIGHT and self.can_change_direction:
            self.head.setheading(LEFT)
            self.direction = LEFT
            self.can_change_direction = False

    def right(self):
        if self.head.heading() != LEFT and self.can_change_direction:
            self.head.setheading(RIGHT)
            self.direction = RIGHT
            self.can_change_direction = False

