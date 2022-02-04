-- 
-- Pregunta
-- ===========================================================================
-- 
-- Para el archivo `data.tsv` compute la cantidad de registros por letra. 
-- Escriba el resultado a la carpeta `output` del directorio actual.
--
fs -rm -f -r output;
--
-- >>> Escriba su respuesta a partir de este punto <<<

u = LOAD 'data.tsv' USING PigStorage('\t') AS (clave:CHARARRAY, fecha:CHARARRAY, valor:CHARARRAY); 
grupo = GROUP u by clave;
conteo = FOREACH grupo GENERATE FLATTEN(group) as clave, COUNT($1);

STORE conteo INTO 'output' USING PigStorage('\t');