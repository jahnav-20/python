-- 1. Create employee table with 2 columns
CREATE TABLE employee (
    emp_name CHAR(20),
    location VARCHAR(50)
);


-- 2. Add column address at last position
ALTER TABLE employee
ADD add_emp VARCHAR(100);


-- 3. Add column emp_id at first position
ALTER TABLE employee
ADD emp_id INT FIRST;


-- 4. Add column email at specific position (after emp_name)
ALTER TABLE employee
ADD email VARCHAR(25) AFTER emp_name;


-- 5. Modify emp_name CHAR to VARCHAR
ALTER TABLE employee
MODIFY emp_name VARCHAR(20);


-- 6. Add sid and department columns at a time
ALTER TABLE employee
ADD sid INT,
ADD department VARCHAR(50);


-- 7. Rename emp_name to employeeName
ALTER TABLE employee
CHANGE emp_name employeeName VARCHAR(20);


-- 8. Drop sid column
ALTER TABLE employee
DROP COLUMN sid;