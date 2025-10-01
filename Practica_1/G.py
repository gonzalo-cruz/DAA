numero_palabras = int(input())
if not (0 <= numero_palabras <= 20):
    numero_palabras = 0
ana = 0
monica = 0
loser = None
for i in range(numero_palabras):
    palabra = input().strip()
    if palabra !=palabra[::-1]:
        if loser is None:
            if i%2==0:
                loser = "ANA"
            else:
                loser = "MONICA"
    if palabra == palabra[::-1]:    # Verifica si la palabra es un palíndromo
        if i%2==0:
            ana += 1
        else:
            monica += 1
if loser == "ANA":
    winner = "MONICA"
elif loser == "MONICA":
    winner = "ANA"
else:
    if ana > monica:
        winner = "ANA"
    elif monica > ana:
        winner = "MONICA"
    else:
        winner = "EMPATE"
print(ana, monica, winner)