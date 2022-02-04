import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#

if __name__ == "__main__":
    
    for line in sys.stdin:
        columnas = line.split(',')
        col1 = columnas[0]
        col2 = columnas[1]
        sys.stdout.write("{},{}".format(col1, col2))