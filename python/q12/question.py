##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv`, imprima por cada fila, la columna 1 y la suma 
##  de los valores de la columna 5.
##
##  Rta/
##  E,22
##  A,14
##  B,14
##  ....
##  C,8
##  E,11
##  E,16
##
##  No puede usar pandas en este ejercicio
##
##  >>> Escriba su codigo a partir de este punto <<<
##
datos = open('data.csv', 'r')
registros = [linea.split() for linea in datos]
datos.close()

columnas = [[e[0],e[4]] for e in registros]

def sumar(var):
    import re
    for i in var:
        num = re.findall('\d+', i[1])
        #print(num)
        num = [int(n) for n in num]
        print(i[0]+','+str(sum(num)))

sumar(columnas)



