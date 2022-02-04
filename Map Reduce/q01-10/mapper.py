#! /usr/bin/env python3

import sys

if __name__ == "__main__":
    for line in sys.stdin:
        columnas = line.split(',')
        columna_tres = columnas[2]
        sys.stdout.write("{}\t1\n".format(columna_tres))