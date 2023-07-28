-- This SQL script creates the 'unique_id' table on the MySQL server
-- The table has an 'id' column of type INT with the default value 1 and must be unique,
-- and a 'name' column of type VARCHAR(256)

CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
