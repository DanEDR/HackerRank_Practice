

# https://www.hackerrank.com/challenges/the-pads/problem?isFullScreen=true
# Score 30

SELECT  CONCAT(Name, '(', SUBSTRING(Occupation, 1, 1), ')') AS name_profession
FROM OCCUPATIONS
ORDER BY name_profession;

SELECT CONCAT('There are a total of ', COUNT(*), ' ',LOWER(Occupation), 's.')
FROM OCCUPATIONS
GROUP BY Occupation
ORDER BY COUNT(*), Occupation;