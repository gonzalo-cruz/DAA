
entrada = int(input()) #numero de intentos
puntuacion_1 = 0
puntuacion_2 = 0
num_intento_1 = 0
num_intento_2 = 0
for i in range (0,entrada): 
    num_intentos = input().split()
    num_intento = int(num_intentos[0])
    puntuacion = int(num_intentos[1])

    if(puntuacion>puntuacion_1):
        puntuacion_2 = puntuacion_1 
        puntuacion_1 = puntuacion
        num_intento_2 = num_intento_1
        num_intento_1 = num_intento
    else:
        if(puntuacion>puntuacion_2):
            puntuacion_2 = puntuacion 
            num_intento_2 = num_intento
puntuacion_final = puntuacion_1 + puntuacion_2
print (num_intento_1, num_intento_2, puntuacion_final)

    

