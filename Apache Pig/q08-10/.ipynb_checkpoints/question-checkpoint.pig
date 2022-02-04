-- Pregunta
-- ===========================================================================
-- 
-- Para el archivo `data.tsv` compute la cantidad de registros por letra de la 
-- columna 2 y clave de al columna 3; esto es, por ejemplo, la cantidad de 
-- registros en tienen la letra `b` en la columna 2 y la clave `jjj` en la 
-- columna 3 es:
-- 
--   ((b,jjj), 216)
-- 
-- Escriba el resultado a la carpeta `output` del directorio actual.
-- 
fs -rm -f -r output;
--
-- >>> Escriba su respuesta a partir de este punto <<<
--
data = LOAD  'data.tsv' USING PigStorage('\t') AS (mayuscula:CHARARRAY, minuscula:CHARARRAY, clave:CHARARRAY);
data_selected = FOREACH data GENERATE FLATTEN(STRSPLITTOBAG(minuscula,',')) as letter, FLATTEN(STRSPLITTOBAG(clave,',')) as key;
data_modified = FOREACH data_selected GENERATE REPLACE(letter,'([^a-zA-Z\\s]+)','') as letra, REPLACE(key,'([^a-zA-Z\\s]+)','') as clave;
grupo = group data_modified by letra;
data_counted = FOREACH grupo GENERATE FLATTEN(group) as letra, COUNT(letra);
dump data_counted;
