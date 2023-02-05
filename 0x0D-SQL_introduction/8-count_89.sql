-- script to display the number of records
SELECT SQL_CALC_FOUND_ROWS *
FROM   first_table
WHERE  id = 89;

SELECT FOUND_ROWS();