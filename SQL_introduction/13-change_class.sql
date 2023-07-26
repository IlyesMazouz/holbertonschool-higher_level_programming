-- This SQL script removes all records with a score <= 5 from the 'second_table'
-- in the database 'hbtn_0c_0'.

DELETE FROM second_table
WHERE score <= 5;
