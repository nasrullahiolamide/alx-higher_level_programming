-- Script to print top scores

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;