-- Pregunta
-- ===========================================================================
-- 
-- Para el archivo `data.tsv` genere una tabla que contenga la primera columna,
-- la cantidad de elementos en la columna 2 y la cantidad de elementos en la 
-- columna 3 separados por coma. La tabla debe estar ordenada por las 
-- columnas 1, 2 y 3.
-- 
-- Escriba el resultado a la carpeta `output` del directorio actual.
-- 
fs -rm -f -r output;
--
-- >>> Escriba su respuesta a partir de este punto <<<
--
data = LOAD  'data.tsv' USING PigStorage('\t') AS (mayuscula:CHARARRAY, minuscula:CHARARRAY, clave:CHARARRAY);
data_ordered = ORDER data BY mayuscula;
data_counted = FOREACH data_ordered GENERATE mayuscula, COUNT(TOKENIZE(minuscula,',')) as m, COUNT(TOKENIZE(clave,',')) as c;
newdata_ordered = ORDER data_counted BY mayuscula, m, c;
STORE newdata_ordered INTO 'output' USING PigStorage(',');