

# https://www.hackerrank.com/challenges/harry-potter-and-wands/problem?isFullScreen=true
# Score 30

SELECT w.id, min_gold_galleons.age, w.coins_needed, w.power
FROM (
    SELECT 
        w.code, 
        wp.age, 
        w.power, 
        MIN(w.coins_needed) AS coins
    FROM Wands AS w
    INNER JOIN Wands_Property AS wp
      ON w.code = wp.code AND wp.is_evil = 0
    GROUP BY w.code, w.power, wp.age
) AS min_gold_galleons
INNER JOIN Wands w
 ON min_gold_galleons.code = w.code AND min_gold_galleons.coins = w.coins_needed
ORDER BY w.power DESC, min_gold_galleons.age DESC;