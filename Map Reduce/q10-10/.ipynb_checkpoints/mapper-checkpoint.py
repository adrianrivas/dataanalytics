import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == "__main__":
    columnas = []
    for line in sys.stdin:
        line = line.replace('\t', ',')
        line = line.replace('\n', '')
        sys.stdout.write("{}\n".format(line))     