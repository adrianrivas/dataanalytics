##
##  Gestion de datos con BASH
##  ===========================================================================
##
##  Cuantas personas nacieron en el trimestre Q1 del año?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
awk -F, '$6 ~ /-01-|-02-|-03-/ {print}' person | wc -l