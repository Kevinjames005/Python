from turtle import Turtle
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
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
        for position in STARTING_POSITIONS:
            self.add_element(position)

    def add_element(self , position):
        new_block = Turtle(shape="square")
        new_block.penup()
        new_block.color("white")
        new_block.setposition(position)
        self.blocks.append(new_block)

    def extend(self):
        last_position = self.position_of_last_block()
        self.add_element(last_position)

    def position_of_last_block(self):
        return self.blocks[len(self.blocks)-1].position()




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



