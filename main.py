from sense_hat import SenseHat
from time import sleep
from nice_functions import *
from objects import Snake

sense = SenseHat()
sense.clear()

ejecucion = True
serpiente = Snake(3, 3)

game_over = False
direccion = [1, 0]

while ejecucion:
    
    direccion = direcciones(sense, direccion)
    print(direccion)
    serpiente.move(direccion)
    sense.clear()

    contador = 0
    for i in serpiente.pixels: 
        if i == serpiente.pixels[0] and contador !=0:
            game_over = True
            ejecucion = False
        contador += 1
    
    for i in serpiente.pixels:
        sense.set_pixel(i[0], i[1], (55, 55, 55))
    

    
    sense.set_pixel(serpiente.apple[0], serpiente.apple[1], (100, 0, 0))



    sleep(0.4)
if game_over:
    sense.show_message("Game Over", text_colour=(255, 20, 20), back_colour=(50, 50, 100), scroll_speed=0.05)
sense.clear()


