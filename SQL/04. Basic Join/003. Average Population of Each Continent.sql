

# https://www.hackerrank.com/challenges/average-population-of-each-continent/problem?isFullScreen=true
# Score 10

SELECT cotry.Continent, FLOOR(AVG(c.Population))
FROM CITY AS c
INNER JOIN COUNTRY AS cotry
  ON c.CountryCode = cotry.Code
GROUP BY cotry.Continent;