import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == '__main__':
    
    frecuencia = []
    frecuencia_dos = []
    
    for line in sys.stdin:
        val1, val2, val3 = line.split(",") #Divide la linea en clave y valor
        frecuencia.append([str(val1), str(val2), int(val3)])
    
    frecuencia = sorted(frecuencia, key = lambda x: int(x[2]))
    
    for x in range(6):
        frecuencia_dos.append(frecuencia[x])
        
    for k in frecuencia_dos:
        sys.stdout.write("\t".join(map(str,k)) + "\n")