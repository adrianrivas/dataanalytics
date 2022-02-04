##
##  Programación en Python
##  ===========================================================================
##
##  La columna 5 del archvio `data.csv` codifica un diccionario donde cada
##  cadena de tres letras corresponde a una clave y el valor despues del
##  caracter `:` corresponde al valor asociado a la clave. Por cada clave,
##  obtenga el valor asociado mas pequeño y el valor asociado mas grande 
##  computados sobre todo el archivo. 
##
##  Rta/
##  aaa,0,6
##  bbb,4,7
##  ccc,0,1
##  ddd,5,5
##  eee,0,0
##  fff,4,9
##  ggg,3,3
##  hhh,6,8
##  iii,2,7
##  jjj,2,5
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

elementomax = 0
elementomin = 0

for key in nuevaclave:
    elementomax = int(key[1])
    elementomin = int(key[1])
    if key[0] in frecuencia:
        if elementomax > int(frecuencia[key[0]]['max']):
            frecuencia[key[0]]['max'] = elementomax
        if elementomin < int(frecuencia[key[0]]['min']):
            frecuencia[key[0]]['min'] = elementomin
    else:
        frecuencia[key[0]] = {
            'max':elementomax,
            'min':elementomin
        }

for clave in frecuencia:
    print(str(clave) + ',' + str(frecuencia[clave]['min']) + ',' + str(frecuencia[clave]['max']))

