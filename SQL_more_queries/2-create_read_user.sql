-- This SQL script creates the database 'hbtn_0d_2' and the user 'user_0d_2'.
-- The 'user_0d_2' user is granted only the SELECT privilege in the 'hbtn_0d_2' database

-- Creating the database if not exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Creating the user if not exists and granting SELECT privilege in the hbtn_0d_2 database
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
