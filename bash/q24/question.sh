##
##  Gestion de datos con BASH
##  ===========================================================================
##
##  Cuantas tarjetas se vencen en el trimestre Q3 del año?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
awk -F, '$2 ~ /Jul|Aug|Sep/ {print}' *.txt | wc -l