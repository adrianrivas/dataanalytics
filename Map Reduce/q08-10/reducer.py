import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#

if __name__ == '__main__':
    
    frecuencia = {}
    
    for line in sys.stdin:
        key, val = line.split("\t") #Divide la linea en clave y valor
        
        #key = key.replace("\n","")
        #valor = val.replace("\n", "")
        
        if key in frecuencia: 
            frecuencia[key]['suma'] += float(val)
            frecuencia[key]['elemento'] += 1
            frecuencia[key]['prom'] = frecuencia[key]['suma'] / frecuencia[key]['elemento']
        else:
            frecuencia[key] = {
                'suma':float(val),
                'elemento':1,
                'prom':0
            }
        
    #for clave in frecuencia:
                
    for clave in frecuencia: #Recorre el diccionario e imprime por claves y el valor del parámetro max y min
        if frecuencia[clave]['prom'] == 0:
            frecuencia[clave]['prom'] = frecuencia[clave]['suma']
        sys.stdout.write(str(clave) + "\t" + str(frecuencia[clave]['suma']) + "\t" + str(frecuencia[clave]['prom']) + "\n")