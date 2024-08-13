

# https://www.hackerrank.com/challenges/more-than-75-marks/problem?isFullScreen=true
# Score 15

SELECT Name
FROM STUDENTS
WHERE Marks > 75
ORDER BY SUBSTRING(Name, -3), ID;