import sys
#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
if __name__ == '__main__':
    
    frecuencia = []
    frecuencia_sorted = []
    
    for line in sys.stdin:
        key, val = line.split(",") #Divide la linea en clave y valor
        #if key in frecuencia:
        frecuencia.append([int(val), key])
    
    frecuencia.sort()
    
    for i in frecuencia:
        frecuencia_sorted.append([i[1],i[0]])
    
    for k in frecuencia_sorted:
            sys.stdout.write(",".join(map(str,k)) + "\n")
   
        