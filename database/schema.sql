-- Hospital Appointment System Database Schema

-- Create database
CREATE DATABASE IF NOT EXISTS hospital_db;
USE hospital_db;

-- Users table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role ENUM('patient', 'doctor', 'admin') DEFAULT 'patient',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Doctors table
CREATE TABLE IF NOT EXISTS doctors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    specialty VARCHAR(100) NOT NULL,
    experience INT NOT NULL,
    fee DECIMAL(10,2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Appointments table
CREATE TABLE IF NOT EXISTS appointments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    doctor_id INT NOT NULL,
    slot_id INT,
    token INT,
    status ENUM('Booked', 'Completed', 'Cancelled') DEFAULT 'Booked',
    appointment_date DATE DEFAULT (CURRENT_DATE),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES users(id),
    FOREIGN KEY (doctor_id) REFERENCES doctors(id)
);

<<<<<<< HEAD
-- Insert sample data
INSERT INTO doctors (name, specialty, experience, fee) VALUES
('Dr. John Smith', 'Cardiology', 10, 500.00),
('Dr. Sarah Johnson', 'Dermatology', 8, 400.00),
('Dr. Michael Brown', 'Orthopedics', 12, 600.00);
=======
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

('Dr. Anjali', 'Pediatrician', 8, 450),
('Dr. Suresh', 'Neurologist', 15, 700),
('Dr. Priya', 'Gynecologist', 9, 500),
('Dr. Ramesh', 'ENT Specialist', 11, 550);
>>>>>>> 2e932a59eeff27b756690536fa22e77161f9da5c
