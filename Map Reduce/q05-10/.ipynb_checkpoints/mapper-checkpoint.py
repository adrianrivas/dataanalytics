import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#

if __name__ == "__main__":
    for line in sys.stdin:
        columnas = line.split('   ')
        fecha = columnas[1] 
        i = fecha.split("-")
        mes = i[1]
        sys.stdout.write("{}\t1\n".format(mes))