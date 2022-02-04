##
##  Programación con Pandas
##  ===========================================================================
##
##  Si la columna _c0 es la clave en los archivos `tbl0.tsv`
##  y `tbl2.tsv`, compute la suma de tbl2._c5b por cada
##  valor en tbl0._c1.
## 
##  Rta/
##  _c1
##  A    146
##  B    134
##  C     81
##  D    112
##  E    275
##  Name: _c5b, dtype: int64
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import pandas as pd

a = pd.read_csv(
    "tbl0.tsv",
    sep="\t",  # separador de campos
    thousands=None,  #  separador de miles para números
    decimal=".",
)

b = pd.read_csv(
    "tbl2.tsv",
    sep="\t",  # separador de campos
    thousands=None,  #  separador de miles para números
    decimal=".",
) 

c = pd.merge(a,b, on='_c0') #Combino ambas tablas .csv
d = c.groupby('_c1').sum()['_c5b'] #Agrupo por la columna _c1 y sumo los valores de _c5b
print(d) #Imprimo el nuevo dataframe

