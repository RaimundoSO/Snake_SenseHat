from sense_hat import SenseHat
from random import randrange
from nice_functions import new_apple, border_path

class Snake:
    #The snake.pixels will be a list of coordinates[[x1, y1], [x2, y2], [x3, y3],...]
    def __init__(self, x_init, y_init):
        self.pixels = list([[x_init, y_init]])
        self.apple = [5,1]
    
    def __str__(self):
        return self.pixels

    def snake_length(self):
        return length(self.pixels)

    def move(self, direccion):
        #The direction is up = [0, -1]; down = [0, 1]; right = [1, 0]; left = [-1, 0]
        self.pixels.insert(0, [border_path(self.pixels[0][0]
            + direccion[0]), border_path(self.pixels[0][1] + direccion[1])])
        print(self.pixels)
        a = self.pixels
        b = self.apple
        if self.pixels[0] == self.apple:
            self.apple = new_apple(self)
        else:
            self.pixels.pop()


