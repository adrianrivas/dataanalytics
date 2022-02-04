import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == '__main__':
    
    #Creación de lista y diccionario utilizados para el código
    columnas = []
    frecuencia = {}
    
    #Recorrido del archivo entrante en un for y agregado en lista
    for line in sys.stdin:
        line = line.replace('\n', '')
        columnas.append(line.split(','))
    
    #Agregación de elementos por clave en diccionario
    for m in columnas:
        valor = int(m[0])
        for j in m:
            if j.isalpha():
                if j in frecuencia:
                    frecuencia[j]['elementos'].append(valor)
                    frecuencia[j]['elementos'].sort()
                else:
                    frecuencia[j] = {
                        'elementos': [valor]
                    }
    
    #Ordenado del diccionario por las claves
    frecuencia = dict(sorted(frecuencia.items()))
    
    #Impresión del contenido del diccionario
    for clave in frecuencia:
        sys.stdout.write(str(clave) + '\t' + ",".join(map(str, frecuencia[clave]['elementos'])) + '\n')