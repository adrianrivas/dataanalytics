##
##  Gestion de datos con BASH
##  ===========================================================================
##
##  Cuantas personas tienen 'AA' como iniciales de su nombre?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
cut -d"," -f5 person | sed 's/"//g' | awk '/^A/' | sed 's/ /,/g' | awk -F, '$2 ~ /^A/' | wc -l