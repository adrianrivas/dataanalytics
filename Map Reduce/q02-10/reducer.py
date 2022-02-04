import sys
#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#

if __name__ == '__main__':
    
    frecuencia = {}
    
    for line in sys.stdin:
        key, val = line.split("\t") #Divide la linea en clave y valor
        
        if key in frecuencia: #pregunta si la clave ya está en el diccionario
            if int(val) > int(frecuencia[key]['max']): #pregunta si el valor de la variable val es mayor que el    valor de la clave en el diccionario
                frecuencia[key]['max'] = val #Si el valor es mayor, lo actualiza en el diccionario dentro de su respectiva clave
        else: #Si la clave no está en el diccionario, la crea
            frecuencia[key] = { 
                'max':val #Le asigna el valor de la variable val a el parametro max
            }
                
    for clave in frecuencia: #Recorre el diccionario e imprime por claves y el valor del parámetro max
        sys.stdout.write("{}\t{}".format(clave, frecuencia[clave]['max']))