

# https://www.hackerrank.com/challenges/african-cities/problem?isFullScreen=true
# Score 10

SELECT c.Name
FROM CITY AS c
INNER JOIN COUNTRY AS cotry
  ON c.CountryCode = cotry.Code
WHERE cotry.Continent = 'Africa';