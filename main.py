from sense_hat import SenseHat
from time import sleep
from random import randrange

sense = SenseHat()
sense.clear()

ejecucion = True
serpiente = [[3,3]]

x_manzana =randrange(8)
y_manzana = randrange(8)
comer = False
game_over = False

#direcciones =[derecha, izquierda, subir, bajar]
direcciones =[False, True, False, False]
while ejecucion:
    for event in sense.stick.get_events():
        if event.direction == "right":
            print("Derecha")
            direcciones = [True, False, False, False]
        elif event.direction == "left":
            print("Izquierda")
            direcciones = [False, True, False, False]
        elif event.direction == "up":
            print("Arriba")
            direcciones = [False, False, True, False]
        elif event.direction == "down":
            print("Abajo")
            direcciones = [False, False, False, True]
        elif event.direction == "middle":
            print("Centro")
            ejecucion = False
    
    if direcciones[0] == True:
        serpiente.insert(0, [serpiente[0][0] + 1, serpiente[0][1]])

    elif direcciones[1] == True:
        serpiente.insert(0, [serpiente[0][0] - 1, serpiente[0][1]])

    elif direcciones[2] == True:
        serpiente.insert(0, [serpiente[0][0], serpiente[0][1] - 1])

    elif direcciones[3] == True:
        serpiente.insert(0, [serpiente[0][0], serpiente[0][1] + 1])
   
    if x_manzana == serpiente[0][0] and y_manzana == serpiente[0][1]:
        comer = True

    if serpiente[0][0] > 7:
        serpiente[0][0] = 0
    if serpiente[0][0] < 0:
        serpiente[0][0] = 7
    if serpiente[0][1] > 7:
        serpiente[0][1] = 0
    if serpiente[0][1] < 0:
        serpiente[0][1] = 7
    
    print(serpiente)
    if comer == False:
        serpiente.pop()

    if comer == True:
        comer = False
    
    print(serpiente)    
    sense.clear()

    contador = 0
    for i in serpiente: 
        if i == serpiente[0] and contador !=0:
            game_over = True
            ejecucion = False
        contador += 1
    
    for i in serpiente:
        sense.set_pixel(i[0], i[1], (55, 55, 55))
    

    while [x_manzana, y_manzana] in serpiente:
        x_manzana = randrange(8)
        y_manzana = randrange(8)
    sense.set_pixel(x_manzana, y_manzana, (100, 0, 0))



    sleep(0.4)
if game_over:
    sense.show_message("Game Over", text_colour=(255, 20, 20), back_colour=(50, 50, 100), scroll_speed=0.05)
sense.clear()


