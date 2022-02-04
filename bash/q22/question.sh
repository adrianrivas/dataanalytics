##
##  Gestion de datos con BASH
##  ===========================================================================
##
##  Cuantas tarjetas se vencen en el trimestre Q1 del año?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
##csvsql --query 'select * from Discover WHERE validthru like "%Mar%"' Discover.txt
awk -F, '$2 ~ /Mar|Feb|Jan/ {print}' *.txt | wc -l