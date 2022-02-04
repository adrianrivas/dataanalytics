##
##  Gestion de datos con BASH
##  ===========================================================================
##
##  Cuantos registros hay en el archivo 'person' para city = 'New York (New York)'?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
cut -d"," -f3 person | grep "New York (New York)" | wc -l