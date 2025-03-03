-- 0. Create a Database
CREATE DATABASE CompanyDBA;

USE CompanyDBA;

-- Create Departments Table
CREATE TABLE Departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(100) NOT NULL
);

-- Create Employees Table
CREATE TABLE Employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(100) NOT NULL,
    emp_email VARCHAR(100) UNIQUE,
    emp_salary DECIMAL(10, 2),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES Departments(dept_id)
);

-- Insert sample data into Departments
INSERT INTO Departments (dept_id, dept_name)
VALUES (1, 'Engineering'), (2, 'Marketing'), (3, 'Sales');

-- Insert sample data into Employees
INSERT INTO Employees (emp_id, emp_name, emp_email, emp_salary, dept_id)
VALUES
(1, 'Yogesh Bhandare', 'yogesh.bhandare@example.com', 75000, 1),
(2, 'Rajat Pawar', 'rajat.pawar@example.com', 60000, 2),
(3, 'Atharv Thakur', 'atharv.thakur@example.com', 55000, 1),
(4, 'Aditya Damse', 'aditya.damse@example.com', 50000, 3);

-- 1. Inner Join
SELECT e.emp_name, d.dept_name
FROM Employees e
INNER JOIN Departments d ON e.dept_id = d.dept_id;

-- 2. Left Join
SELECT e.emp_name, d.dept_name
FROM Employees e
LEFT JOIN Departments d ON e.dept_id = d.dept_id;

-- 3. Right Join
SELECT e.emp_name, d.dept_name
FROM Employees e
RIGHT JOIN Departments d ON e.dept_id = d.dept_id;

-- 4. Simulated Full Outer Join using UNION
SELECT e.emp_name, d.dept_name
FROM Employees e
LEFT JOIN Departments d ON e.dept_id = d.dept_id
UNION
SELECT e.emp_name, d.dept_name
FROM Employees e
RIGHT JOIN Departments d ON e.dept_id = d.dept_id;

-- 5. Self Join
SELECT a.emp_name AS Employee, b.emp_name AS Manager
FROM Employees a
INNER JOIN Employees b ON a.dept_id = b.dept_id AND a.emp_id != b.emp_id;

-- 6. Sub-Query to find employees with salaries above average
SELECT emp_name, emp_salary
FROM Employees
WHERE emp_salary > (SELECT AVG(emp_salary) FROM Employees);

-- 7. Sub-Query with IN clause
SELECT emp_name
FROM Employees
WHERE dept_id IN (SELECT dept_id FROM Departments WHERE dept_name = 'Engineering');

-- 8. Creating a View for high-salary employees
CREATE VIEW HighSalaryEmployees AS
SELECT emp_name, emp_salary
FROM Employees
WHERE emp_salary > 60000;

-- 9. Selecting from the View
SELECT * FROM HighSalaryEmployees;

-- 10. Sub-Query in SELECT statement
SELECT emp_name, (SELECT dept_name FROM Departments WHERE dept_id = e.dept_id) AS Department
FROM Employees e;
