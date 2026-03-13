import mysql.connector

# Connect to MySQL server (without specifying database)
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123"
)
cursor = conn.cursor()

# Create database if not exists
cursor.execute("CREATE DATABASE IF NOT EXISTS hospital_db")
cursor.execute("USE hospital_db")

# Create tables (with IF NOT EXISTS)
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role ENUM('patient', 'doctor', 'admin') DEFAULT 'patient',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS doctors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    specialty VARCHAR(100) NOT NULL,
    experience INT NOT NULL,
    fee DECIMAL(10,2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

cursor.execute("""
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
)
""")

# Check if doctors table has fee column, if not add it
try:
    cursor.execute("SELECT fee FROM doctors LIMIT 1")
except mysql.connector.Error:
    cursor.execute("ALTER TABLE doctors ADD COLUMN fee DECIMAL(10,2) NOT NULL DEFAULT 0.00")

# Insert sample doctors (only if table is empty)
cursor.execute("SELECT COUNT(*) FROM doctors")
count = cursor.fetchone()[0]
if count == 0:
    cursor.execute("""
    INSERT INTO doctors (name, specialty, experience, fee) VALUES
    ('Dr. John Smith', 'Cardiology', 10, 500.00),
    ('Dr. Sarah Johnson', 'Dermatology', 8, 400.00),
    ('Dr. Michael Brown', 'Orthopedics', 12, 600.00)
    """)

conn.commit()
cursor.close()
conn.close()

print("Database schema created/updated successfully!")