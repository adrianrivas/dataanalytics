##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv`, imprima el valor maximo y minimo de la columna
##  2 por cada letra de la columa 1.
##
##  Rta/
##  A,9,1
##  B,9,1
##  C,9,0
##  D,7,1
##  E,9,1
##
##  No puede usar pandas en este ejercicio
##
##  >>> Escriba su codigo a partir de este punto <<<
##
datos = open('data.csv', 'r')
registros = [linea.split() for linea in datos]
datos.close()

columnas = [e[0:2] for e in registros]
columnas.sort()

frecuencia = {}

elemento = 0
elementom = 0
for col in columnas:
    #print(col)
    for c in col[0]:
        elemento = int(col[1])
        elementom = int(col[1])
        if c in frecuencia:
            if elemento > int(frecuencia[c]['max']):
                frecuencia[c]['max'] = elemento
            if elementom < int(frecuencia[c]['min']):
                frecuencia[c]['min'] = elementom
        else:
            frecuencia[c] = {
                'max':elemento,
                'min':elementom
            } 

for clave in frecuencia:
    print(str(clave) + ',' + str(frecuencia[clave]['max']) + ',' + str(frecuencia[clave]['min']))

