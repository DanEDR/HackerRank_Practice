

# https://www.hackerrank.com/challenges/occupations/problem?isFullScreen=true
# Score

WITH OCCUPATIONS_RANKED AS (
  SELECT *,
  RANK() OVER(PARTITION BY Occupation ORDER BY Name) AS RK
  FROM OCCUPATIONS
)
SELECT
 MAX(CASE WHEN Occupation = 'Doctor' THEN Name END )AS d_name,
  MAX(CASE WHEN Occupation = 'Professor' THEN Name END) AS p_name,
  MAX(CASE WHEN Occupation = 'Singer' THEN Name END) AS s_name,
  MAX(CASE WHEN Occupation = 'Actor' THEN Name END) AS a_name
FROM OCCUPATIONS_RANKED
GROUP BY RK;