##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv`, genera una lista de tuplas que asocien las 
##  columnas 0 y 1. Cada tupla contiene un valor posible de la columna 2 y una
##  lista con todas las letras asociadas (columna 1) a dicho valor de la 
##  columna 2.
##
##  Rta/
##  ('0', ['C'])
##  ('1', ['E', 'B', 'D', 'A', 'A', 'E'])
##  ('2', ['A', 'E', 'D'])
##  ('3', ['A', 'B', 'D', 'E', 'E'])
##  ('4', ['E', 'B'])
##  ('5', ['B', 'C', 'D', 'D', 'E', 'E', 'E'])
##  ('6', ['C', 'E', 'A', 'B'])
##  ('7', ['A', 'C', 'E', 'D'])
##  ('8', ['E', 'E', 'A', 'B'])
##  ('9', ['A', 'B', 'E', 'C'])
##
##  No puede usar pandas en este ejercicio
##
##  >>> Escriba su codigo a partir de este punto <<<
##

datos = open('data.csv', 'r')
registros = [linea.split() for linea in datos]
datos.close()

columnas = [e[0:2] for e in registros]

#print(columnas)
frecuencia = {}
elemento = ''

for col in columnas:
    #print(col)
    for c in col[1]:
        elemento = col[0]
        if c in frecuencia:
            frecuencia[c].append(elemento)
        else:
            frecuencia[c] = []
            frecuencia[c].append(elemento)

frecuencia_ordenada = dict(sorted(frecuencia.items()))

#imprimir = (clave, valor for clave, valor in frecuencia_ordenada.items())
for clave, valor in frecuencia_ordenada.items():
     imprimir = (clave, valor)
     print(imprimir)