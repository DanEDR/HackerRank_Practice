

# https://www.hackerrank.com/challenges/the-report/problem?isFullScreen=true
# Score 20

# Solution 1
WITH StudensGrade AS (
SELECT
    ID, Name, Marks,
    CASE 
        WHEN 0 <= Marks AND Marks <= 9 THEN 1
        WHEN 10 <= Marks AND Marks <= 19 THEN 2
        WHEN 20 <= Marks AND Marks <= 29 THEN 3
        WHEN 30 <= Marks AND Marks <= 39 THEN 4
        WHEN 40 <= Marks AND Marks <= 49 THEN 5
        WHEN 50 <= Marks AND Marks <= 59 THEN 6
        WHEN 60 <= Marks AND Marks <= 69 THEN 7
        WHEN 70 <= Marks AND Marks <= 79 THEN 8
        WHEN 80 <= Marks AND Marks <= 89 THEN 9
        ELSE 10
    END AS Grade
FROM Students
)
SELECT 
    CASE
     WHEN Grade > 7 THEN Name
     ELSE NULL
    END AS Name,
    Grade, Marks
FROM StudensGrade
ORDER BY Grade DESC, Name;

# Solution 2

SELECT 
    IF(Grade < 8, NULL, Name),
    Grade, Marks
FROM Students, Grades
WHERE Marks BETWEEN Min_Mark AND Max_Mark
ORDER BY Grade DESC, Name;