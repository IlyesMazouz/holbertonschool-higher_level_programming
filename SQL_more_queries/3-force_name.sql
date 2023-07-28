-- This SQL script creates the 'force_name' table on the MySQL server
-- The table has an 'id' column of type INT and a 'name' column of type VARCHAR(256) which cannot be null

CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
