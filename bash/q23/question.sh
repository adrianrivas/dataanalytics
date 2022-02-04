##
##  Gestion de datos con BASH
##  ===========================================================================
##
##  Cuantas tarjetas se vencen en el trimestre Q2 del año?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
awk -F, '$2 ~ /Apr|May|Jun/ {print}' *.txt | wc -l