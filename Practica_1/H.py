def contar_vocales(name):
    vocales = 'aeiou'
    return sum(name.lower().count(vocal) for vocal in vocales)

resultados = []

numero_candidatos_str = input().strip()
if not numero_candidatos_str:
        numero_candidatos = 0
else:
        numero_candidatos = int(numero_candidatos_str)


if not(0<= numero_candidatos <= 1000):
    numero_candidatos = 0


nombre_usuario  = input().strip()
numero_vocales_usuario = contar_vocales(nombre_usuario)

for i in range(numero_candidatos):
    candidato = input().strip()
    numero_vocales_candidato = contar_vocales(candidato)
    if numero_vocales_usuario == numero_vocales_candidato:
        resultados.append("ITS A MATCH!")
    else:
        resultados.append("NEXT!")

for resultado in resultados:
    print(resultado)
