##
##  Gestion de datos con BASH
##  ===========================================================================
##
##  Cual el nombre  completo (fullname) del del dueño de la tarjeta 
##  3608-2968-5750-1980?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
##codigo=$(csvsql --query 'select ssn from bank WHERE ccn = "3608-2968-5750-1980"' bank.csv)
##csvsql --query 'select fullname from person WHERE ssn = $codigo' person 
csvjoin -c ssn person bank.csv | grep "3608-2968-5750-1980" | cut -d"," -f5