# Write your MySQL query statement below
SELECT 
    CASE 
        WHEN COUNT(num) = 0 THEN NULL
        ELSE MAX(num)
    END AS num
FROM (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(num) = 1
) AS unique_nums;