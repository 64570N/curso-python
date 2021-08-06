#rebotes.py
#ejercicio 1.5

x = 100
aux = 0
cont = 0

for i in range(10): 
    aux = x / 5 
    x = round(aux * 3, 4)
    cont = cont + 1
    print( cont, "-", x)
    