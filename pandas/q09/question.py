##
##  Programación con Pandas
##  ===========================================================================
##
##  Construya una tabla que contenga _c0 y una lista
##  separada por ',' de los valores de la columna _c4
##  del archivo `tbl1.tsv`.
##
##  Rta/
##      _c0    lista
##  0     0    b,f,g
##  1     1    a,c,f
##  ...
##  38   38      d,e
##  39   39    a,d,f
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
import pandas as pd

datos = pd.read_csv(
    "tbl1.tsv",
    sep="\t",  
    thousands=None,  
    decimal=".",
) 

a = datos.groupby('_c0')['_c4'].apply(lambda x: list(x))
a = a.reset_index()
a.columns = ['_c0', 'lista']
a['lista'] = a.lista.map(lambda x: sorted(x))
a['lista'] = a.lista.map(lambda x: ','.join(x))
print(a)
