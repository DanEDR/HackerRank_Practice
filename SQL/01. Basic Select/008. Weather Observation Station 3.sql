

# https://www.hackerrank.com/challenges/weather-observation-station-3/problem?isFullScreen=true
# Score 10

SELECT DISTINCT CITY 
FROM STATION
WHERE ID % 2 = 0;