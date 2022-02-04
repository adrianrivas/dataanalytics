##
##  Programación en Python
##  ===========================================================================
##
##  Imprima la suma de la segunda columna del archivo `data.csv`.
##
##  Rta/
##  190
##
##  No puede usar pandas en este ejercicio
##
##  >>> Escriba su codigo a partir de este punto <<<
##
datos = open('data.csv', 'r')
#lineadividida=[]
#for linea in datos:
    #lineadividida.append(linea.split())
lineadividida = [linea.split() for linea in datos]
datos.close()

#print(lineadividida)
acu=0
for linea in lineadividida[:]:
    acu += int(linea[1])
print(acu)