-- This SQL script creates the 'hbtn_0d_usa' database and the 'states' table on the MySQL server
-- The 'states' table has an 'id' column of type INT, unique, auto-generated, cannot be null, and is a primary key
-- The table also has a 'name' column of type VARCHAR(256), which cannot be null

-- Creating the database if not exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Using the 'hbtn_0d_usa' database
USE hbtn_0d_usa;

-- Creating the 'states' table if not exists
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
