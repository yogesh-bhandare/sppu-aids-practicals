-- 0. Create a Database
CREATE DATABASE CompanyDB;

-- 1. Switch to the new Database
USE CompanyDB;

-- 2. Create a Table with different constraints (removed emp_hire_date)
CREATE TABLE Employees (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,  
    emp_name VARCHAR(100) NOT NULL,
    emp_email VARCHAR(100) UNIQUE,
    emp_salary DECIMAL(10, 2) CHECK (emp_salary > 0),
    emp_dept VARCHAR(50)
);

-- 3. Create a View
CREATE VIEW EmployeeDetails AS
SELECT emp_name, emp_salary, emp_dept
FROM Employees
WHERE emp_salary > 50000;

-- 4. Create an Index
CREATE INDEX idx_emp_dept ON Employees(emp_dept);

-- 5. Insert data into Employees
INSERT INTO Employees (emp_name, emp_email, emp_salary, emp_dept) VALUES 
('Yogesh Bhandare', 'yogesh.bhandare@example.com', 75000, 'Engineering'),
('Rajat Pawar', 'rajat.pawar@example.com', 60000, 'Engineering'),
('Atharv Thakur', 'atharv.thakur@example.com', 55000, 'Engineering'),
('Aditya Damse', 'aditya.damse@example.com', 50000, 'Marketing');

-- 6. Select all employees
SELECT * FROM Employees;

-- 7. Select employees with salary greater than 50000
SELECT emp_name, emp_salary
FROM Employees
WHERE emp_salary > 50000;

SET SQL_SAFE_UPDATES = 0;

-- 8. Update employee salary
UPDATE Employees
SET emp_salary = emp_salary + 5000
WHERE emp_name = 'Yogesh Bhandare';

-- 9. Delete an employee
DELETE FROM Employees
WHERE emp_name = 'Rajat Pawar';

-- 10. Select with set operators (UNION)
SELECT emp_name, emp_dept
FROM Employees
WHERE emp_dept = 'Engineering'
UNION
SELECT emp_name, emp_dept
FROM Employees
WHERE emp_salary > 60000;

-- 11. Select with functions
SELECT emp_name, UPPER(emp_dept) AS Department, ROUND(emp_salary, 0) AS Salary
FROM Employees;


