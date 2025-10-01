entrada = int(input())
if entrada <= 10: 
    print("CRUZCAMPO")
if entrada in range(11,20):
    print("MALA")
if entrada in range(21,35): 
    print ("REGULAR")
if entrada in range(36,45): 
    print("BUENA")
if entrada >=46:
    print("MUY BUENA")