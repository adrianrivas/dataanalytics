##
##  Programación en Python
##  ===========================================================================
##
##  Genere una lista de tuplas, donde cada tupla contiene en la primera 
##  posicion, el valor de la segunda columna; la segunda parte de la 
##  tupla es una lista con las letras (ordenadas y sin repetir letra) 
##  de la primera  columna que aparecen asociadas a dicho valor de la 
##  segunda columna. Esto es:
##
##  Rta/
##  ('0', ['C'])
##  ('1', ['A', 'B', 'D', 'E'])
##  ('2', ['A', 'D', 'E'])
##  ('3', ['A', 'B', 'D', 'E'])
##  ('4', ['B', 'E'])
##  ('5', ['B', 'C', 'D', 'E'])
##  ('6', ['A', 'B', 'C', 'E'])
##  ('7', ['A', 'C', 'D', 'E'])
##  ('8', ['A', 'B', 'E'])
##  ('9', ['A', 'B', 'C', 'E'])
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
#print(columnas)
frecuencia = {}
elemento = ''

for col in columnas:
    #print(col)
    for c in col[1]:
        elemento = col[0]
        if c in frecuencia:
            if elemento not in frecuencia[c]:
                frecuencia[c].append(elemento)
        else:
            frecuencia[c] = []
            frecuencia[c].append(elemento)

frecuencia_ordenada = dict(sorted(frecuencia.items()))

#imprimir = (clave, valor for clave, valor in frecuencia_ordenada.items())
for clave, valor in frecuencia_ordenada.items():
     imprimir = (clave, valor)
     print(imprimir)