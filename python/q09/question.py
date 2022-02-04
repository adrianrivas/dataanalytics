##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv, imprima una tabla en formato CSV que contenga 
##  la cantidad de registros en que aparece cada clave de la columna 5.
##
##  Rta/
##  aaa,13
##  bbb,16
##  ccc,23
##  ddd,23
##  eee,15
##  fff,20
##  ggg,13
##  hhh,16
##  iii,18
##  jjj,18
##
##  No puede usar pandas en este ejercicio
##
##  >>> Escriba su codigo a partir de este punto <<<
##
datos = open('data.csv', 'r')
registros = [linea.split() for linea in datos]
datos.close()

columnas = [e[4] for e in registros]

columnas.sort()

clave = [claves.split(',') for claves in columnas] 

nuevaclave = [c.split(':') for col in clave for c in col]
nuevaclave.sort()

frecuencia = {}

for key in nuevaclave:
    if key[0] in frecuencia:
         frecuencia[key[0]]['contador'] += 1
    else:
        frecuencia[key[0]] = {
            'contador':1
        }
for clave in frecuencia:
    print(str(clave) + ',' + str(frecuencia[clave]['contador']))



