##
##  Gestion de datos con BASH
##  ===========================================================================
##
##  Cuantos registros quedan en el archivo 'person' si se eliminan los 
##  registros con 'city' = 'Albuquerque (New Mexico)'?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##

csvsql --query 'select * from person WHERE city != "Albuquerque (New Mexico)"' person | tail +2 | wc -l  