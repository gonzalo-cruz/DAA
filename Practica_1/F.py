entrada = input().strip().split()
numero_jugador = int(entrada[0])
color = entrada[1]
activado = entrada[2]
if not (0 <= numero_jugador <= 999):
    numero_jugador = 0
if activado == '0':
    print ("JUGADOR ",numero_jugador, " CONTINUAR")
else:
    print("JUGADOR ", numero_jugador, " ELIMINADO")