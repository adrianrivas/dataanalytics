##
##  Programación en Python
##  ===========================================================================
##
##  La columna 3 del archivo `data.csv` contiene una fecha en formato 
##  `YYYY-MM-DD`. Imprima la cantidad de registros por cada mes separados
##  por comas, tal como se muestra a continuación.
##
##  Rta/
##  01,3
##  02,4
##  03,2
##  04,4
##  05,3
##  06,3
##  07,5
##  08,6
##  09,3
##  10,2
##  11,2
##  12,3
##
##  No puede usar pandas en este ejercicio
##
##  >>> Escriba su codigo a partir de este punto <<<
##
datos = open('data.csv', 'r')
registros = [linea.split() for linea in datos]
datos.close()

columna1 = [e[2] for e in registros]
columna1.sort()
fecha = [e.split("-") for e in columna1]
mes = [f[1] for f in fecha]
mes.sort()

frecuencia = {}

for e in mes:
    if e in frecuencia:
        frecuencia[e] += 1
    else:
        frecuencia[e] = 1

for clave in frecuencia:
    print(str(clave) + ',' + str(frecuencia[clave]))
