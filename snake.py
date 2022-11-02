from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DIST = 16
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)


    def add_segment(self, position):
        new_dot = Turtle("square")
        new_dot.color("white")
        new_dot.penup()
        new_dot.goto(position)
        self.segments.append(new_dot)

    def extend(self):
        self.add_segment(self.segments[-1].position())


    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.segments[0].forward(MOVING_DIST)

    def refresh(self):
        for i in self.segments:
            i.goto(1000,1000)
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments.pop(i)




    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)





