-- This SQL script creates the 'hbtn_0d_usa' database and the 'cities' table on the MySQL server
-- The 'cities' table has an 'id' column of type INT, unique, auto-generated, cannot be null, and is a primary key
-- The table also has a 'state_id' column of type INT, which cannot be null and must be a FOREIGN KEY that references to 'id' of the 'states' table
-- It also has a 'name' column of type VARCHAR(256), which cannot be null

-- Creating the database if not exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Using the 'hbtn_0d_usa' database
USE hbtn_0d_usa;

-- Creating the 'cities' table if not exists
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    CONSTRAINT fk_state_id FOREIGN KEY (state_id) REFERENCES states(id)
);
