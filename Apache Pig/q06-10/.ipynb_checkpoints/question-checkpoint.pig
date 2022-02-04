-- 
-- Pregunta
-- ===========================================================================
-- 
-- Para el archivo `data.tsv` Calcule la cantidad de registros por clave de la 
-- columna 3. En otras palabras, cuántos registros hay que tengan la clave 
-- `aaa`?
-- 
-- Escriba el resultado a la carpeta `output` del directorio actual.
-- 
fs -rm -f -r output;
--
-- >>> Escriba su respuesta a partir de este punto <<<
--
data = LOAD  'data.tsv' USING PigStorage('\t') AS (mayuscula:CHARARRAY, minuscula:CHARARRAY, clave:CHARARRAY);
data_selected = FOREACH data GENERATE FLATTEN(STRSPLITTOBAG(clave,',')) as key;
data_modified = FOREACH data_selected GENERATE REPLACE(key,'([^a-zA-Z\\s]+)','') as key;
data_divided = FOREACH data_modified GENERATE key, SUBSTRING(key, 0, 3) as new_key;
new_data = FOREACH data_divided GENERATE new_key;
new_data_grouped = GROUP new_data BY new_key;
new_data_counted = FOREACH new_data_grouped GENERATE FLATTEN(group) as new_key, COUNT($1);
STORE new_data_counted INTO 'output' USING PigStorage(',');