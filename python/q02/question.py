##
##  Programación en Python
##  ===========================================================================
##
##  Imprima la cantidad de registros por letra para la primera columna del 
##  archivo `data.csv`, ordenados alfabeticamente por la letra.
##
##  Rta/
##  A,8
##  B,7
##  C,5
##  D,6
##  E,14
##
##  No puede usar pandas en este ejercicio
##
##  >>> Escriba su codigo a partir de este punto <<<
##
datos = open('data.csv', 'r')
registros = [linea.split() for linea in datos]
datos.close()

columna1 = [e[0] for e in registros]
columna1.sort()

frecuencia = {}

for e in columna1:
    if e in frecuencia:
        frecuencia[e] += 1
    else:
        frecuencia[e] = 1

for clave in frecuencia:
    print(str(clave) + ',' + str(frecuencia[clave]))