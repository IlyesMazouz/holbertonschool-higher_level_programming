-- This SQL script lists all records with a score >= 10 from the 'second_table'
-- in the database 'hbtn_0c_0', displaying both the score and name, ordered by score (top first)

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
