

# https://www.hackerrank.com/challenges/weather-observation-station-20/problem?isFullScreen=true
# Score 40

WITH ranked_latitude AS (
  SELECT
    RANK() OVER (ORDER BY LAT_N ASC) AS lat_n_rank,
    LAT_N
  FROM STATION
)
SELECT ROUND(LAT_N, 4)
FROM ranked_latitude
WHERE lat_n_rank = (
  SELECT (COUNT(*) + 1) / 2 
  FROM ranked_latitude);