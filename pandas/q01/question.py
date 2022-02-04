##
##  Programación con Pandas
##  ===========================================================================
##
##  Imprima la cantidad de registros por cada letra 
##  de la columna _c1 del archivo `data.tsv` usando pandas.
## 
##  Rta/
##  _c1
##  A     8
##  B     7
##  C     5
##  D     6
##  E    14
##  Name: _c0, dtype: int64
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import pandas as pd

datos = pd.read_csv(
    "data.tsv",
    sep="\t",  # separador de campos
    thousands=None,  #  separador de miles para números
    decimal=".",
) 
conteo = datos.groupby('_c1').count()['_c0']
print(conteo)