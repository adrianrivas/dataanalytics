-- 
-- Pregunta
-- ===========================================================================
-- 
-- Para responder la pregunta use el archivo `data.csv`.
-- 
-- Cuente la cantidad de personas nacidas por año.
-- 
-- Escriba el resultado a la carpeta `output` del directorio actual.
-- 
fs -rm -f -r output;
-- 
data = LOAD 'data.csv' USING PigStorage(',') 
    AS (id:int, 
        firstname:CHARARRAY, 
        surname:CHARARRAY, 
        birthday:CHARARRAY, 
        color:CHARARRAY, 
        quantity:INT);
--
-- >>> Escriba su respuesta a partir de este punto <<<
--
data_selected = FOREACH data GENERATE id, ToDate(birthday) as fecha;
data_year = FOREACH data_selected GENERATE id, GetYear(fecha) as ano;
data_grouped = GROUP data_year by ano;
conteo = FOREACH data_grouped GENERATE FLATTEN(group) as ano, COUNT($1);
STORE conteo INTO 'output' USING PigStorage(',');