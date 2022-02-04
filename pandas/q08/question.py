##
##  Programación con Pandas
##  ===========================================================================
##
##  Construya una tabla que contenga _c1 y una lista
##  separada por ':' de los valores de la columna _c2
##  para el archivo `tbl0.tsv`.
##
##  Rta/
##    _c0                        lista
##  0   A              1:1:2:3:6:7:8:9
##  1   B                1:3:4:5:6:8:9
##  2   C                    0:5:6:7:9
##  3   D                  1:2:3:5:5:7
##  4   E  1:1:2:3:3:4:5:5:5:6:7:8:8:9
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
import pandas as pd

datos = pd.read_csv(
    "tbl0.tsv",
    sep="\t",  # separador de campos
    thousands=None,  #  separador de miles para números
    decimal=".",
) 

a = datos.groupby('_c1')['_c2'].apply(list)
a = a.reset_index()
a.columns = ['_c0', 'lista']
s = ':'
for index, row in a.iterrows():
    row['lista'] = sorted(row['lista'])
    row['lista'] = [str(x) for x in row['lista']]
    row['lista'] = s.join(row['lista'])
print(a)