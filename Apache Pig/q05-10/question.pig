-- 
-- Pregunta
-- ===========================================================================
-- 
-- Para el archivo `data.tsv` compute Calcule la cantidad de registros en que 
-- aparece cada letra minúscula en la columna 2.
-- 
-- Escriba el resultado a la carpeta `output` del directorio actual.
-- 
fs -rm -f -r output;
--
-- >>> Escriba su respuesta a partir de este punto <<<
--
data = LOAD  'data.tsv' USING PigStorage('\t') AS (mayuscula:CHARARRAY, minuscula:CHARARRAY, clave:CHARARRAY);
data_selected = FOREACH data GENERATE FLATTEN(STRSPLITTOBAG(minuscula,',')) as letter;
data_modified = FOREACH data_selected GENERATE REPLACE(letter,'([^a-zA-Z\\s]+)','') as letra;
data_grouped = GROUP data_modified BY letra;
data_counted = FOREACH data_grouped GENERATE FLATTEN(group) as letra, COUNT($1);

STORE data_counted INTO 'output' USING PigStorage('\t');

