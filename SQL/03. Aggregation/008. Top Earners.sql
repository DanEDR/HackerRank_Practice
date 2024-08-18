

# https://www.hackerrank.com/challenges/earnings-of-employees/problem?isFullScreen=true
# Score 20

SELECT salary*months AS earnings, COUNT(*)
FROM EMPLOYEE
GROUP BY earnings
ORDER BY earnings DESC
LIMIT 1;