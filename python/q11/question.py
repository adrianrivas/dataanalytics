##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv`, imprima la suma de la columna 2 para cada 
##  letra de la columna 4, ordnados alfabeticamente.
##
##  Rta/
##  a,114
##  b,40
##  c,91
##  d,65
##  e,79
##  f,110
##  g,35
##
##  No puede usar pandas en este ejercicio
##
##  >>> Escriba su codigo a partir de este punto <<<
##
datos = open('data.csv', 'r')
registros = [linea.split() for linea in datos]
datos.close()

columnas = [[e[3].split(','), e[1]] for e in registros]

frecuencia = {}
for i in columnas:
    for m in i[0]:
        if m in frecuencia:
            frecuencia[m] += int(i[1])
        else:
            frecuencia[m] = int(i[1])

for clave in sorted(frecuencia):
    print(str(clave) + ',' + str(frecuencia[clave]))

