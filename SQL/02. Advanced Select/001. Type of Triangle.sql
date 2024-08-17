

# https://www.hackerrank.com/challenges/what-type-of-triangle/problem?isFullScreen=true
# Score 20

SELECT
        CASE 
              WHEN A + B <= C  OR A + C  <= B OR C + B <= A THEN 'Not A Triangle'
              WHEN A = B AND B = C THEN 'Equilateral'
              WHEN A <> B AND B <> C AND A <> C THEN 'Scalene'
              ELSE 'Isosceles'
        END 
FROM TRIANGLES;