-- Prepares a MySQL server for the project
-- Creates a database
-- Grant user priviledges on creation
-- Grant SELECT priviledges on the performance schema
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
GRANT ALL ON hbnb_dev_db.*
TO 'hbnb_dev'@'localhost'
IDENTIFIED BY 'hbnb_dev_pwd';
GRANT SELECT ON performance_schema.*
TO 'hbnb_dev'@'localhost';
