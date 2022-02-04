##
##  Gestion de datos con BASH
##  ===========================================================================
##
##  Cuantas tarjetas tienen el pin entre 980 y 990?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
awk -F, '$4 ~ /980|981|982|983|984|985|986|987|988|989|990/ {print}' *.txt | wc -l
