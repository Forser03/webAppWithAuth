CREATE SCHEMA service;
CREATE TABLE service.users(id SERIAL PRIMARY KEY, full_name VARCHAR NOT NULL, login VARCHAR NOT NULL, password VARCHAR NOT NULL);

INSERT INTO service.users (full_name, login, password) VALUES 
('FirstName1 SecondName1','user1','123'),
('FirstName2 SecondName2','user2','1234'),
('FirstName3 SecondName3','user3','12345');
