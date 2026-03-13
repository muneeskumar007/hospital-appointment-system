


CREATE DATABASE hospital_db;
USE hospital_db;

CREATE TABLE users(
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100),
email VARCHAR(100),
password VARCHAR(100),
role VARCHAR(20)
);

CREATE TABLE doctors(
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100),
specialty VARCHAR(100),
experience INT
);

CREATE TABLE slots(
id INT AUTO_INCREMENT PRIMARY KEY,
doctor_id INT,
slot_time VARCHAR(50)
);

CREATE TABLE appointments(
id INT AUTO_INCREMENT PRIMARY KEY,
patient_id INT,
doctor_id INT,
slot_id INT,
token INT,
status VARCHAR(20)
);





INSERT INTO doctors (name, specialty, experience, fee)
VALUES
('Dr. Kumar','Cardiologist',10,500),
('Dr. Meena','Dermatologist',7,400),
('Dr. Raj','Orthopedic',12,600);