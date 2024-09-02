

-- https://www.hackerrank.com/challenges/contest-leaderboard/problem?isFullScreen=true
-- Score 30


SELECT
 h.hacker_id,
 h.name,
 SUM(s.max_score) AS sum_score
FROM (
 SELECT
  hacker_id,
  MAX(score) AS max_score
 FROM Submissions
 GROUP BY hacker_id, challenge_id
  ) AS s
INNER JOIN Hackers h
 ON s.hacker_id = h.hacker_id
GROUP BY h.hacker_id, h.name
HAVING sum_score > 0
ORDER BY sum_score DESC, h.hacker_id ASC;