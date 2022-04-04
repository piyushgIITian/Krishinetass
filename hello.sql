-- Database: flask_db

-- DROP DATABASE IF EXISTS flask_db;

CREATE DATABASE flask_db
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_India.1252'
    LC_CTYPE = 'English_India.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

GRANT ALL ON DATABASE flask_db TO postgres;

GRANT TEMPORARY, CONNECT ON DATABASE flask_db TO PUBLIC;