-- This SQL script lists all records of the 'second_table' from the database 'hbtn_0c_0',
-- excluding rows without a name value, and orders the records by descending score

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
