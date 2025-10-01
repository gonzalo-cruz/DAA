
linea = input()
linea_div = linea.split()

usos_cupon = [int(n) for n in linea_div[:6]]

max_usos = 0
mejor = -1
for i in range(len(usos_cupon)):
    id = i+1
    usos = int(usos_cupon[i])
    out = f"{id} " + "="*usos
    print(out)
    if usos > max_usos:
        max_usos = usos
        mejor = id
if mejor != -1:
    print(f"El mas usado es el cupon {mejor} con {max_usos} usos")