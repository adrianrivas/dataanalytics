-- Pregunta
-- ===========================================================================
-- 
-- Ordene el archivo `data.tsv`  por letra y valor (3ra columna).
-- Escriba el resultado a la carpeta `output` del directorio actual.
-- 
fs -rm -f -r output;
-- 
--  >>> Escriba el codigo del mapper a partir de este punto <<<
datos = LOAD 'data.tsv' USING PigStorage ('\t') AS (clave:CHARARRAY, fecha:CHARARRAY, valor:INT);
datos_ordered = ORDER datos BY clave, valor;

STORE datos_ordered INTO 'output' USING PigStorage('\t');
