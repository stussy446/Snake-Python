from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.length = 3
        self.segments = []
        self.setup()
        self.head = self.segments[0]

    def setup(self):
        x = -20
        for i in range(0, self.length):
            new_snake_piece = Turtle(shape='square')
            new_snake_piece.penup()
            new_snake_piece.color('white')
            new_snake_piece.setx(x)
            x += 20

            self.segments.append(new_snake_piece)

    def move(self):
        for i in range(self.length - 1, 0, -1):
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
