import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#

if __name__ == '__main__':
    
    frecuencia = {}
    mayor = 0
    menor = 0
    for line in sys.stdin:
        key, val = line.split("\t") #Divide la linea en clave y valor
        
        key = key.replace("\n","")
        valor = val.replace("\n", "")
        
        mayor = float(valor)
        menor = float(valor)
        
        if key in frecuencia: 
            if mayor > float(frecuencia[key]['max']): 
                frecuencia[key]['max'] = mayor 
            if menor < float(frecuencia[key]['min']):
                frecuencia[key]['min'] = menor
        else: 
            frecuencia[key] = { 
                'max':mayor, 
                'min':menor
            }
                
    for clave in frecuencia: #Recorre el diccionario e imprime por claves y el valor del parámetro max y min
        sys.stdout.write(str(clave) + "\t" + str(frecuencia[clave]['max']) + "\t" + str(frecuencia[clave]['min']) + "\n")