##
##  Gestion de datos con BASH
##  ===========================================================================
##
##  Cual es el valor del campo 'validthru' del archivo 'data.csv' para 
##  el registro 2?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
csvcut -c validthru data.csv | sed -n '3p'