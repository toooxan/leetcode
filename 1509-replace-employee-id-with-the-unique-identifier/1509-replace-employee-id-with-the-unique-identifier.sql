# Write your MySQL query statement below
SELECt e.id, eu.unique_id
FROM Employees e
LEFT JOIN EmployeeUNI ON e.id = eu.id