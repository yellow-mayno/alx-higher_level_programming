-- create a table
-- create table will overwrite the previous
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(id INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, state_id INT NOT NULL, name VARCHAR(256) NOT NULL);
