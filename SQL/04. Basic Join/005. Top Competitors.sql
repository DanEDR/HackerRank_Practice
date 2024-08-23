

# https://www.hackerrank.com/challenges/full-score/problem?isFullScreen=true
# Score 30

SELECT h.hacker_id, h.name
FROM Submissions s
INNER JOIN Challenges c
  ON s.challenge_id = c.challenge_id
INNER JOIN Difficulty d
  ON c.difficulty_level = d.difficulty_level
INNER JOIN Hackers h
  ON s.hacker_id = h.hacker_id
WHERE s.score = d.score
GROUP BY h.hacker_id, h.name
HAVING COUNT(s.score) > 1
ORDER BY COUNT(s.score) DESC, h.hacker_id ASC;