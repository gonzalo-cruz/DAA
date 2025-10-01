counter = [0]*10
i = 0
linea_div = []
while True:
    linea = input()
    linea_div.extend(linea.split())
    if '-1' in linea.split():
        break
for i in linea_div:
    if not i:
        continue
    id = int(i.strip())
    if id == -1:
        break
    if 0 <= id <= 9:
        counter[id] += 1
imprimir = []
for id in range(10):
    if counter[id] >= 3:
        imprimir.append(str(id))
print(" ".join(imprimir))

