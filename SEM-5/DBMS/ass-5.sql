-- 1. Create Database
CREATE DATABASE HotelDB;

-- 2. Use the Database
USE HotelDB;

-- 3. Create a Table for storing hotel guests
CREATE TABLE Guests (
    guest_id INT PRIMARY KEY AUTO_INCREMENT,
    guest_name VARCHAR(100),
    guest_email VARCHAR(100),
    check_in DATE,
    check_out DATE,
    room_number INT
);

-- 4. Insert Sample Data into Guests Table
INSERT INTO Guests (guest_name, guest_email, check_in, check_out, room_number)
VALUES 
('Yogesh Bhandare', 'yogeshbhandare@example.com', '2024-01-15', '2024-01-20', 101),
('Atharv Thakur', 'atharvthakur@example.com', '2024-02-10', '2024-02-14', 102),
('Rajat Pawar', 'rajatpawar@example.com', '2024-03-05', '2024-03-10', 103),
('Sachin Phaps', 'sachinphaps@example.com', '2024-04-01', '2024-04-05', 104);

SELECT * FROM Guests;

DROP table Guests;

SHOW VARIABLES LIKE 'secure_file_priv';

-- 5. Export Data to CSV
-- This query exports the Guests table data into a CSV file.
SELECT *
FROM Guests
INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/hotel_guests.csv'
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n';

-- 6. Export Data to TXT
-- This query exports the Guests table data into a TXT file.
SELECT *
FROM Guests
INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/hotel_guests.txt'
FIELDS TERMINATED BY '\t'
ENCLOSED BY '"'
LINES TERMINATED BY '\n';

-- 7. Import Data from CSV
-- This query imports data from a CSV file into the Guests table.
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/hotel_guests_import.csv'
INTO TABLE Guests
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS; 

-- 8. Import Data from TXT
-- This query imports data from a TXT file into the Guests table.
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/hotel_guests_import.txt'
INTO TABLE Guests
FIELDS TERMINATED BY '\t'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;  
