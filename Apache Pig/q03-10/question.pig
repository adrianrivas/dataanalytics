-- Pregunta
-- ===========================================================================
-- 
-- Obtenga los cinco (5) valores más pequeños de la 3ra columna.
-- Escriba el resultado a la carpeta `output` del directorio actual.
-- 
fs -rm -f -r output;
--
-- >>> Escriba su respuesta a partir de este punto <<<
--
data = LOAD 'data.tsv' USING PigStorage ('\t') AS (clave:CHARARRAY, fecha:CHARARRAY, valor:INT); --Cargo el archivo en una bolsa de pig
data_selected = FOREACH data GENERATE valor; --Extrae el campo valor y genera una nueva bolsa
data_ordered = ORDER data_selected BY valor; --Ordena el campo valor de forma ascendente
data_limited = LIMIT data_ordered 5; --Imprime los cinco primeros valores

STORE data_limited INTO 'output' USING PigStorage('\t'); --Almacena la información en disco