from sense_hat import SenseHat
from random import randrange
from tools import *

class Snake:
    #The snake.pixels will be a list of coordinates[[x1, y1], [x2, y2], [x3, y3],...]
    def __init__(self, x_init, y_init):
        self.pixels = [[x_init, y_init]]
        self.apple = [randrange(8), randrange(8)]

    def snake_length(self):
        return length(self.pixels)

    def move(self, direction):
        #The direction is up = [0, -1]; down = [0, 1]; right = [1, 0]; left = [-1, 0]
        self.pixels = self.pixels.insert(0, [border_path(self.pixels[0][0] + direction[0]), border_path(self.pixels[0][1] + direction[1])])
        if self.pixels[0] != self.apple:
            self.pixels.pop()
        else:
            self.apple = new_apple(self.pixels)




if __name__ == '__main__':
