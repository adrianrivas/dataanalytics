##
##  Gestion de datos con BASH
##  ===========================================================================
##
##  Cual es el valor del campo 'key' del archivo 'data.csv' para el 
##  registro 3?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
csvcut -c key data.csv | sed -n '4p'