from random import randrange
from sense_hat import SenseHat

def new_apple(snake):
    x_manzana = randrange(8)
    y_manzana = randrange(8)
    while [x_manzana, y_manzana] in snake.pixels:
        x_manzana = randrange(8)
        y_manzana = randrange(8)
    return [x_manzana, y_manzana]


def border_path(number):
    if number < 0:
        return 7
    elif number > 7:
        return 0
    else:
        return number

def direcciones(sense, last_direction):
    for event in sense.stick.get_events():
        if event.direction == "right":
            print("Derecha")
            last_direction = [1, 0]
        elif event.direction == "left":
            print("Izquierda")
            last_direction = [-1, 0]
        elif event.direction == "up":
            print("Arriba")
            last_direction = [0, -1]
        elif event.direction == "down":
            print("Abajo")
            last_direction = [0, 1]
        elif event.direction == "middle":
            print("Centro")
            last_direction = [0, 0]
    return last_direction
