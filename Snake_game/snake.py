from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.blocks = []
        self.create_snake()
        self.head = self.blocks[0]

    def create_snake(self):
        y = 0
        x = 0
        for i in range(3):
            new_block = Turtle(shape="square")
            new_block.penup()
            new_block.color("white")
            new_block.setposition(x=x, y=y)
            x += -20
            self.blocks.append(new_block)


    def move(self):
        for seg_num in range(len(self.blocks) - 1, 0, -1):
            new_x = self.blocks[seg_num - 1].xcor()
            new_y = self.blocks[seg_num - 1].ycor()
            self.blocks[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)



