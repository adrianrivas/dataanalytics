##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv`, imprima una tabla en formato CSV que contenga 
##  por registro, la letra de la columna 1 y la cantidad de elementos de las 
##  columnas 4 y 5. 
## 
##  Rta/
##  E,3,5
##  A,3,4
##  B,4,4
##  ...
##  C,4,3
##  E,2,3
##  E,3,3
##
##  No puede usar pandas en este ejercicio
##
##  >>> Escriba su codigo a partir de este punto <<<
##
datos = open('data.csv', 'r')
registros = [linea.split() for linea in datos]
datos.close()

columnas = [[e[0],e[3],e[4]] for e in registros]

for i in columnas:
        print(i[0] + ',' + str(len(i[1].split(','))) + ',' + str(len(i[2].split(','))))


