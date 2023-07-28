-- This SQL script creates the 'id_not_null' table on the MySQL server
-- The table has an 'id' column of type INT with the default value 1, and a 'name' column of type VARCHAR(256)

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
