import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#

if __name__ == "__main__":
    for line in sys.stdin:
        columnas = line.split(',')
        col4 = columnas[3]
        col5 = columnas[4]
        sys.stdout.write("{}\t{}\n".format(col4, col5))