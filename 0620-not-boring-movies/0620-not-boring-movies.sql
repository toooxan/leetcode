# Write your MySQL query statement below
SELECT * FROM Cinema
WHERE MOD(id, 2) = 1 AND Cinema.description NOT LIKE '%boring%'
ORDER BY rating DESC