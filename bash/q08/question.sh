##
##  Gestion de datos con BASH
##  ===========================================================================
##
##  Cual es el valor del campo 'quota' del archivo 'data.csv' para el 
##  ultimo registro?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
csvcut -c quota data.csv | tail +2 | tail -n 1