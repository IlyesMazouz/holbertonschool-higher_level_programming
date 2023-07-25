-- This SQL script creates a table called first_table in the current database, if it doesn't already exist
-- The table will have two columns: id (integer) and name (varchar with a length of 256 characters)

CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
