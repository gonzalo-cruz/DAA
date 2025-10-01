
try: 
    linea = input().strip().split()
    N = int(linea[0])
    C = linea[1]
    B = linea[2]
except:
    N = 0
    C = ""
    B = ""
for i in range(1, N+1):
    numero_c = i
    nummero_b = N-i
    c_string = C*numero_c
    b_string = B*nummero_b
    print(b_string + c_string)