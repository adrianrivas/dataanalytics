##
##  Gestion de datos con BASH
##  ===========================================================================
##
##  Cuantas veces aparece el número 1192 en el segundo grupo de digitos de las 
##  tarjetas de  credito?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
cut -d"," -f1 *.txt | sed 's/"//g' | cut -d"-" -f2 | grep "1192" | wc -l