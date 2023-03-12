from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.start_length = 3
        self.segments = []
        self.head = None
        self.tail = None
        self.setup()

    def setup(self):
        for i in range(0, self.start_length):
            new_segment = self.add_segment()
            new_segment.goto(STARTING_POSITIONS[i])

        self.head = self.segments[0]
        self.update_tail()

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)

        self.head.forward(20)

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

    def grow(self):
        new_segment = self.add_segment()

        start_x = self.tail.xcor()
        start_y = self.tail.ycor()
        new_segment.goto(start_x, start_y)

        self.update_tail()

    def add_segment(self):
        new_segment = Turtle(shape='square')
        new_segment.penup()
        new_segment.color('white')
        self.segments.append(new_segment)

        return new_segment

    def update_tail(self):
        self.tail = self.segments[len(self.segments) - 1]
