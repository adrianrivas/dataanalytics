##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv`, imprima la suma de la columna 2 por cada letra 
##  de la primera columna, ordneados alfabeticamente.
##
##  Rta/
##  A,37
##  B,36
##  C,27
##  D,23
##  E,67
##
##  No puede usar pandas en este ejercicio
##
##  >>> Escriba su codigo a partir de este punto <<<
##
datos = open('data.csv', 'r')
registros = [linea.split() for linea in datos]
datos.close()

columna1 = [e[0:2] for e in registros]
columna1.sort()

frecuencia = {}

for col in columna1:
    for c in col[0]:
        if c in frecuencia:
            frecuencia[c] += int(col[1])
        else:
            frecuencia[c] = int(col[1])

for clave in frecuencia:
    print(str(clave) + ',' + str(frecuencia[clave]))