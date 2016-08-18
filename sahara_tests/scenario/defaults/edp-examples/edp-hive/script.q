CREATE DATABASE IF NOT EXISTS tests LOCATION '/user/hive/warehouse/tests.db';
CREATE EXTERNAL TABLE IF NOT EXISTS tests.students (name STRING, age INT) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS TEXTFILE;
LOAD DATA INPATH '${INPUT}' INTO TABLE tests.students;
INSERT OVERWRITE DIRECTORY '${OUTPUT}' SELECT name FROM tests.students WHERE age > 30;
DROP TABLE IF EXISTS tests.students;
DROP DATABASE IF EXISTS tests;