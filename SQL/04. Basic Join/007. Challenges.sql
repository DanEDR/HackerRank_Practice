

-- https://www.hackerrank.com/challenges/challenges/problem?isFullScreen=true
-- Score 30

WITH HackerChallenges AS (
  SELECT
   h.hacker_id, 
   h.name, 
   COUNT(*) AS number_challenges
  FROM Hackers h
  INNER JOIN Challenges c
   ON h.hacker_id = c.hacker_id
  GROUP BY h.hacker_id, h.name
  ),
UniqueChallenges AS (
  SELECT 
   number_challenges, 
   COUNT(*)
  FROM HackerChallenges
  GROUP BY number_challenges
  HAVING COUNT(*) = 1
  ),
MaxChallenges AS (
  SELECT 
   MAX(number_challenges) AS max_challenges
  FROM HackerChallenges
  )
SELECT 
 hc.hacker_id, 
 hc.name, 
 hc.number_challenges
FROM HackerChallenges hc
WHERE hc.number_challenges IN (SELECT number_challenges FROM UniqueChallenges)
  OR hc.number_challenges IN (SELECT max_challenges FROM MaxChallenges)
ORDER BY hc.number_challenges DESC, hc.hacker_id;