##
##  Programación con Pandas
##  ===========================================================================
##
##  Construya una tabla que contenga _c0 y una lista
##  separada por ',' de los valores de la columna _c5a
##  y _c5b (unidos por ':') de la tabla tbl2.tsv
## 
##  Rta/
##      _c0                                lista
##  0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
##  1     1              aaa:3,ccc:2,ddd:0,hhh:9
##  ...
##  38   38                    eee:0,fff:9,iii:2
##  39   39                    ggg:3,hhh:8,jjj:5
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import pandas as pd

datos = pd.read_csv(
    "tbl2.tsv",
    sep="\t",  # separador de campos
    thousands=None,  #  separador de miles para números
    decimal=".",
) 
datos['_c5c'] = datos["_c5a"].map(str) + ":" + datos["_c5b"].map(str)
a = datos.groupby('_c0')['_c5c'].apply(lambda x: list(x))
a = a.reset_index()
a.columns = ['_c0', 'lista']
a['lista'] = a.lista.map(lambda x: sorted(x))
a['lista'] = a.lista.map(lambda x: ','.join(x))

print(a)
