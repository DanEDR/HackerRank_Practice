

# https://www.hackerrank.com/challenges/the-blunder/problem?isFullScreen=true
# Score 15

SELECT CEIL(AVG(salary) - AVG(REPLACE(Salary, '0', '')))
FROM EMPLOYEES;
