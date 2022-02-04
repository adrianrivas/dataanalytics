-- 
-- Pregunta
-- ===========================================================================
--
-- Para resolver esta pregunta use el archivo `data.tsv`.
--
-- Compute la cantidad de registros por cada letra de la columna 1.
-- Escriba el resultado ordenado por letra. 
--
-- Escriba el resultado a la carpeta `output` de directorio de trabajo.
--
-- >>> Escriba su respuesta a partir de este punto <<<
--
DROP TABLE IF EXISTS data;

CREATE TABLE IF NOT EXISTS data (clave STRING, fecha DATE, numero INT)
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY '\t';

LOAD DATA LOCAL INPATH './data.tsv' OVERWRITE
INTO TABLE data;

INSERT OVERWRITE DIRECTORY 'output'
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
SELECT clave, count(*) FROM data GROUP BY clave;