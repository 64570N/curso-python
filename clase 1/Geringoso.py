cadena = "hola"

geringoso = ""

for c in cadena:
    geringoso += c
    if c in "AEIOUaeiou":
        
        geringoso += "p"
        geringoso += c
        
        print(geringoso)